# Monitor orbi devices

Monitor devices on your netgear orbi network

## Install

`pip install requirements.txt`

`mv config.toml.sample config.toml`

Set the appropriate password in config.toml

## Usage

`python monitor.py 'device-name'`

eg:

`python monitor.py "Orbi Satellite-2"`

If the device is up, the program will exit without any message gracefully, with exit code 0.

if the device is down, the program will exit raising an error and exit code 1.

You can plug this in with https://healthchecks.io/ to get alerts.