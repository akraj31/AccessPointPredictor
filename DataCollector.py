import json
import os
import time
import sys
from access_points import get_scanner

def aps_to_dict(aps):
    return {ap['ssid'] + " " + ap['bssid']: ap['quality'] for ap in aps}

def get_sample(device=""):
    wifi_scanner = get_scanner(device)
    if not os.environ.get("PYTHON_ENV", False):
        aps = wifi_scanner.get_access_points()
    else:
        aps = [{"quality": 100, "bssid": "XX:XX:XX:XX:XX:84",
                "ssid": "X", "security": "XX"}]
    return aps_to_dict(aps)


def write_data(label_path, data):
    with open(label_path, "w") as f:
        f.write(json.dumps(data))
        f.write("\n")


def collect_data(label, duration):
    path = "./Data"
    label_path = os.path.join(path, label + ".txt")
    
    for i in range(duration):
        print("Collecting " + str(i) + "th data")
        if i != 0:
            time.sleep(1)
        try:
            new_sample = get_sample()
            if new_sample:
                write_data(label_path, new_sample)
        except KeyboardInterrupt:  # pragma: no cover
            break


if __name__ == "__main__":
    apoint = sys.argv[1]
    duration = int(sys.argv[2])
    print("started collecting data")
    collect_data(apoint, duration)
    print("finished collecting data")