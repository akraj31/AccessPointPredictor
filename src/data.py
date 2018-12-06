import os
import json
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
    with open(label_path, "a") as f:
        f.write(json.dumps(data))
        f.write("\n")

def collect_data(label, duration):
    path = "../data/"
    label_path = os.path.join(path, label + ".txt")
    
    for i in range(duration):
        print("Collecting " + str(i) + "th data")
        if i != 0:
            time.sleep(1)
        try:
            new_sample = get_sample()
            if new_sample:
                write_data(label_path, new_sample)
        except KeyboardInterrupt:
            break

def get_training_data():
    X, y = list(), list()
    files = os.listdir("../data/")
    for fname in files:
        #print("filename", fname)
        if fname[-4:]!=".txt":
            continue
        data = list()
        with open(os.path.join("../data/", fname)) as f:
            for line in f:
                #print(line)
                #print(type(line))
                data.append(json.loads(line))
        X.extend(data)
        y.extend([fname.rstrip(".txt")] * len(data))
    return X, y

def get_external_sample(path):
    data = list()
    with open(os.path.join(path, "current.loc.txt")) as f:
        for line in f:
            data.append(json.loads(line))
    return data
