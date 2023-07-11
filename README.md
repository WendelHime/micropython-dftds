# micropython-dftds

This repository reproduces the C++ implementation of the [DFRobot Gravity TDS](https://github.com/DFRobot/GravityTDS) sensor with micropython. With this repository, I hope to be able to use a TDS sensor on a Raspberry Pico W.

## Installing

```bash
micropython -m mip install github:WendelHime/micropython-dftds
```

If you're installing through thonny or developing something with another IDE, the package is also available on pypi:
```bash
pip install micropython-dftds
```

## Testing

```bash
micropython -m unittest tests/*
```

## Usage

```python
from machine import ADC

import dftds

# must be an analog pin
TDS_PIN = 28
# create TDS object remembering to set the values according to your device. On raspberry pico the ADC range is 65535.
# another thing to observe, on rasberry pico we have memory flash available, if you need this code to work on another storage device such as EEPROM you might need to create another implementation of KValueRepository. Feel free to open an PR and contribute.
tds_sensor = dftds.GravityTDS(TDS_PIN, adc_range=65535, k_value_repository=dftds.KValueRepositoryFlash('tds_calibration.json'))
tds_sensor.begin()

# you can read the temperature using a dht22 or other device
tds_sensor.temperature = 25.0
tds_value = tds_sensor.update()
print("TDS: {}ppm, EC: {} mS/cm".format(tds_value, tds_value*2))
```
