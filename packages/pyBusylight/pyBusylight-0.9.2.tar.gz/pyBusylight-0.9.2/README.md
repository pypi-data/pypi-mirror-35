# pyBusylight

pyBusylight is a native python library which controls Kuando Busylight devices. It is intented to serve as a foundational component which can be integrated into other higher-level scripts.

pyBusylight makes use of PyUSB to control Busylight and used extensive cues from the [busylight node library](https://github.com/porsager/busylight).

## Dependencies
* signal
* pyusb

_Note: Pyusb requires at least one of the three supported backends to be installed. Install a backend like so._

    If you're on a MAC you can install libusb via:
```
        $ brew install libusb
```
    On Windows you can follow the info here.
        https://github.com/walac/pyusb/blob/master/README.rst#installing

    On Ubuntu 16.04/18.04
```
    sudo apt-get install libusb-1.0-0 """)
```

## Most Simple Use Case
```
user@hostname$ sudo python3

from pybusylight import pybusylight

bl=pybusylight.busylight()

bl.send()
```

## Run the Example.py script to see all supported features
```
sudo python3 ./example.py
```
