# The MIT License (MIT)
#
# Copyright (c) 2017 ladyada for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_bme280` - Adafruit BME680 - Temperature, Humidity, Pressure & Gas Sensor
====================================================================================

CircuitPython driver from BME280 Temperature, Humidity and Barometic Pressure sensor

* Author(s): ladyada
"""
import math
import time
from micropython import const
try:
    import struct
except ImportError:
    import ustruct as struct


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BME280.git"

#    I2C ADDRESS/BITS/SETTINGS
#    -----------------------------------------------------------------------
_BME280_ADDRESS = const(0x77)
_BME280_CHIPID = const(0x60)

_BME280_REGISTER_CHIPID = const(0xD0)
_BME280_REGISTER_DIG_T1 = const(0x88)
_BME280_REGISTER_DIG_H1 = const(0xA1)
_BME280_REGISTER_DIG_H2 = const(0xE1)
_BME280_REGISTER_DIG_H3 = const(0xE3)
_BME280_REGISTER_DIG_H4 = const(0xE4)
_BME280_REGISTER_DIG_H5 = const(0xE5)
_BME280_REGISTER_DIG_H6 = const(0xE7)

_BME280_REGISTER_SOFTRESET = const(0xE0)
_BME280_REGISTER_CTRL_HUM = const(0xF2)
_BME280_REGISTER_STATUS = const(0xF3)
_BME280_REGISTER_CTRL_MEAS = const(0xF4)
_BME280_REGISTER_CONFIG = const(0xF5)
_BME280_REGISTER_PRESSUREDATA = const(0xF7)
_BME280_REGISTER_TEMPDATA = const(0xFA)
_BME280_REGISTER_HUMIDDATA = const(0xFD)

_BME280_PRESSURE_MIN_HPA = const(300)
_BME280_PRESSURE_MAX_HPA = const(1100)
_BME280_HUMIDITY_MIN = const(0)
_BME280_HUMIDITY_MAX = const(100)

class Adafruit_BME280:
    """Driver from BME280 Temperature, Humidity and Barometic Pressure sensor"""
    def __init__(self):
        """Check the BME280 was found, read the coefficients and enable the sensor for continuous
           reads"""
        # Check device ID.
        chip_id = self._read_byte(_BME280_REGISTER_CHIPID)
        if _BME280_CHIPID != chip_id:
            raise RuntimeError('Failed to find BME280! Chip ID 0x%x' % chip_id)
        self._write_register_byte(_BME280_REGISTER_SOFTRESET, 0xB6)
        time.sleep(0.5)
        self._read_coefficients()
        self.sea_level_pressure = 1013.25
        """Pressure in hectoPascals at sea level. Used to calibrate `altitude`."""
        # turn on humidity oversample 16x
        self._write_register_byte(_BME280_REGISTER_CTRL_HUM, 0x03)
        self._t_fine = None

    def _read_temperature(self):
        # perform one measurement
        self._write_register_byte(_BME280_REGISTER_CTRL_MEAS, 0xFE) # high res, forced mode

        # Wait for conversion to complete
        while self._read_byte(_BME280_REGISTER_STATUS) & 0x08:
            time.sleep(0.002)
        raw_temperature = self._read24(_BME280_REGISTER_TEMPDATA) / 16  # lowest 4 bits get dropped
        #print("raw temp: ", UT)

        var1 = (raw_temperature / 16384.0 - self._temp_calib[0] / 1024.0) * self._temp_calib[1]
        #print(var1)
        var2 = ((raw_temperature / 131072.0 - self._temp_calib[0] / 8192.0) * (
            raw_temperature / 131072.0 - self._temp_calib[0] / 8192.0)) * self._temp_calib[2]
        #print(var2)

        self._t_fine = int(var1 + var2)
        #print("t_fine: ", self.t_fine)

    @property
    def dew_point(self):
        # pylint: disable=invalid-name
        # Disable: c is a constant used in the Magnus formula
        """The dew point in Celsius using the Magnus formula. Constants from Sontag, 1990."""
        b = 17.62
        c = 243.12
        gamma = (b * self.temperature /(c + self.temperature)) + math.log(self.humidity / 100.0)
        dewpoint = (c * gamma) / (b - gamma)
        return dewpoint
        # pylint: enable=invalid-name

    @property
    def temperature(self):
        """The compensated temperature in degrees celsius."""
        self._read_temperature()
        return self._t_fine / 5120.0

    @property
    def pressure(self):
        """The compensated pressure in hectoPascals."""
        self._read_temperature()

        # Algorithm from the BME280 driver
        # https://github.com/BoschSensortec/BME280_driver/blob/master/bme280.c
        adc = self._read24(_BME280_REGISTER_PRESSUREDATA) / 16  # lowest 4 bits get dropped
        var1 = float(self._t_fine) / 2.0 - 64000.0
        var2 = var1 * var1 * self._pressure_calib[5] / 32768.0
        var2 = var2 + var1 * self._pressure_calib[4] * 2.0
        var2 = var2 / 4.0 + self._pressure_calib[3] * 65536.0
        var3 = self._pressure_calib[2] * var1 * var1 / 524288.0
        var1 = (var3 + self._pressure_calib[1] * var1) / 524288.0
        var1 = (1.0 + var1 / 32768.0) * self._pressure_calib[0]
        if var1 == 0:
            return 0
        if var1:
            pressure = 1048576.0 - adc
            pressure = ((pressure - var2 / 4096.0) * 6250.0) / var1
            var1 = self._pressure_calib[8] * pressure * pressure / 2147483648.0
            var2 = pressure * self._pressure_calib[7] / 32768.0
            pressure = pressure + (var1 + var2 + self._pressure_calib[6]) / 16.0

            pressure /= 100
            if pressure < _BME280_PRESSURE_MIN_HPA:
                return _BME280_PRESSURE_MIN_HPA
            if pressure > _BME280_PRESSURE_MAX_HPA:
                return _BME280_PRESSURE_MAX_HPA
            return pressure
        else:
            return _BME280_PRESSURE_MIN_HPA

    @property
    def humidity(self):
        """The relative humidity in RH %"""
        self._read_temperature()
        hum = self._read_register(_BME280_REGISTER_HUMIDDATA, 2)
        #print("Humidity data: ", hum)
        adc = float(hum[0] << 8 | hum[1])
        #print("adc:", adc)

        # Algorithm from the BME280 driver
        # https://github.com/BoschSensortec/BME280_driver/blob/master/bme280.c
        var1 = float(self._t_fine) - 76800.0
        #print("var1 ", var1)
        var2 = (self._humidity_calib[3] * 64.0 + (self._humidity_calib[4] / 16384.0) * var1)
        #print("var2 ",var2)
        var3 = adc - var2
        #print("var3 ",var3)
        var4 = self._humidity_calib[1] / 65536.0
        #print("var4 ",var4)
        var5 = (1.0 + (self._humidity_calib[2] / 67108864.0) * var1)
        #print("var5 ",var5)
        var6 = 1.0 + (self._humidity_calib[5] / 67108864.0) * var1 * var5
        #print("var6 ",var6)
        var6 = var3 * var4 * (var5 * var6)
        humidity = var6 * (1.0 - self._humidity_calib[0] * var6 / 524288.0)

        if humidity > _BME280_HUMIDITY_MAX:
            return _BME280_HUMIDITY_MAX
        if humidity < _BME280_HUMIDITY_MIN:
            return _BME280_HUMIDITY_MIN
        # else...
        return humidity

    @property
    def altitude(self):
        """The altitude based on current ``pressure`` versus the sea level pressure
           (``sea_level_pressure``) - which you must enter ahead of time)"""
        pressure = self.pressure # in Si units for hPascal
        return 44330 * (1.0 - math.pow(pressure / self.sea_level_pressure, 0.1903))

    def _read_coefficients(self):
        """Read & save the calibration coefficients"""
        coeff = self._read_register(_BME280_REGISTER_DIG_T1, 24)
        coeff = list(struct.unpack('<HhhHhhhhhhhh', bytes(coeff)))
        coeff = [float(i) for i in coeff]
        self._temp_calib = coeff[:3]
        self._pressure_calib = coeff[3:]

        self._humidity_calib = [0]*6
        self._humidity_calib[0] = self._read_byte(_BME280_REGISTER_DIG_H1)
        coeff = self._read_register(_BME280_REGISTER_DIG_H2, 7)
        coeff = list(struct.unpack('<hBBBBb', bytes(coeff)))
        self._humidity_calib[1] = float(coeff[0])
        self._humidity_calib[2] = float(coeff[1])
        self._humidity_calib[3] = float((coeff[2] << 4) |  (coeff[3] & 0xF))
        self._humidity_calib[4] = float(((coeff[3] & 0xF0) << 4) | coeff[4])
        self._humidity_calib[5] = float(coeff[5])

    def _read_byte(self, register):
        """Read a byte register value and return it"""
        return self._read_register(register, 1)[0]

    def _read24(self, register):
        """Read an unsigned 24-bit value as a floating point and return it."""
        ret = 0.0
        for b in self._read_register(register, 3):
            ret *= 256.0
            ret += float(b & 0xFF)
        return ret

    def _read_register(self, register, length):
        raise NotImplementedError()

    def _write_register_byte(self, register, value):
        raise NotImplementedError()

class Adafruit_BME280_I2C(Adafruit_BME280):
    """Driver for BME280 connected over I2C"""
    def __init__(self, i2c, address=_BME280_ADDRESS):
        import adafruit_bus_device.i2c_device as i2c_device
        self._i2c = i2c_device.I2CDevice(i2c, address)
        super().__init__()

    def _read_register(self, register, length):
        with self._i2c as i2c:
            i2c.write(bytes([register & 0xFF]))
            result = bytearray(length)
            i2c.readinto(result)
            #print("$%02X => %s" % (register, [hex(i) for i in result]))
            return result

    def _write_register_byte(self, register, value):
        with self._i2c as i2c:
            i2c.write(bytes([register & 0xFF, value & 0xFF]))
            #print("$%02X <= 0x%02X" % (register, value))

class Adafruit_BME280_SPI(Adafruit_BME280):
    """Driver for BME280 connected over SPI"""
    def __init__(self, spi, cs, baudrate=100000):
        import adafruit_bus_device.spi_device as spi_device
        self._spi = spi_device.SPIDevice(spi, cs, baudrate=baudrate)
        super().__init__()

    def _read_register(self, register, length):
        register = (register | 0x80) & 0xFF  # Read single, bit 7 high.
        with self._spi as spi:
            spi.write(bytearray([register]))  #pylint: disable=no-member
            result = bytearray(length)
            spi.readinto(result)              #pylint: disable=no-member
            #print("$%02X => %s" % (register, [hex(i) for i in result]))
            return result

    def _write_register_byte(self, register, value):
        register &= 0x7F  # Write, bit 7 low.
        with self._spi as spi:
            spi.write(bytes([register, value & 0xFF])) #pylint: disable=no-member
