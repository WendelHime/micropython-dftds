"""
Script for TDS calibration, please use once
"""
import time
from machine import Pin

import dht
from dftds import GravityTDS, KValueRepositoryFlash

sensor = dht.DHT22(Pin(0))
tds_sensor = GravityTDS(
    pin=28,
    aref=5.0,
    adc_range=65535,
    k_value_repository=KValueRepositoryFlash("tds_calibration.json")
)
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature: {}C Humidity: {:.0f}% ".format(temp, hum))
    tds_sensor.temperature = temp
    tds_sensor.begin()
    tds_sensor.update()
    if not tds_sensor.calibrated:
        tds_sensor.calibrate(707)
    print(tds_sensor.tds_value)
    time.sleep(2)
