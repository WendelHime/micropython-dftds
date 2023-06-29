# micropython-dftds

This repository reproduces the C++ implementation of the [DFRobot Gravity TDS](https://github.com/DFRobot/GravityTDS) sensor with micropython. With this repository, I hope to be able to use a TDS sensor on a Raspberry Pico W.

## Installing dependencies

```bash
pip3 install -r requirements.txt
```

## Testing

```bash
micropython -m unittest tests/*
```

