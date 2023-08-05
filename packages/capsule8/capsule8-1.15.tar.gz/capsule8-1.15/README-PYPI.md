# Capsule8 api-python

This repo is as a wrapper repo around the [Capsule8](https://github.com/capsule8/capsule8) sensor api.

## Install with pip

```
pip install capsule8
```

## Install with virtualenv

```
virtualenv test_capsule8
cd test_capsule8
source bin/activate
pip install capsule8
```

## Examples

In order to run the examples you need to have a running [capsule8](https://github.com/capsule8/capsule8) sensor on your machine. Once you have a running sensor you can run the examples. Be sure that the capsule8 sensor socket chowned by the current user.

```
sudo chown $USER /var/run/capsule8/sensor.sock
```

Then you can run the SensorClient and start streaming capsule8 sensor telemetry. In this example, every process events pid will be printed to stdout

```
from capsule8.sensor import SensorClient
from itertools import islice

s = SensorClient()


s.subscribe({"event_filter": {
    "process_events": [
        {"type": "PROCESS_EVENT_TYPE_FORK"},
        {"type": "PROCESS_EVENT_TYPE_EXEC"},
        {"type": "PROCESS_EVENT_TYPE_EXIT"}
    ]
}})

max_events = 5
for event in islice(s.telemetry(), max_events):
    print(event.events[0].event.process_pid)
```