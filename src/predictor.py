import json
from collections import Counter
from data import get_training_data, sample, get_external_sample, aps_to_dict
from access_points import get_scanner
from classifier import get_model

def predict_proba(device=""):
    data_sample = sample(device) 
    lp_rf = get_model("rf")
    lp_xgb = get_model("xgb")
    lp_nn = get_model("nn")
    print(json.dumps(dict(zip(lp_rf.classes_, lp_rf.predict_proba(data_sample)[0]))))
    print(json.dumps(dict(zip(lp_xgb.classes_, lp_xgb.predict_proba(data_sample)[0]))))
    print(json.dumps(dict(zip(lp_nn.classes_, lp_nn.predict_proba(data_sample)[0]))))


def predict(device=""):
    data_sample = sample(device)
    lp_rf = get_model("rf")
    lp_xgb = get_model("xgb")
    lp_nn = get_model("nn")
    print(lp_rf.predict(data_sample)[0])
    print(lp_xgb.predict(data_sample)[0])
    print(lp_nn.predict(data_sample)[0]) 
    return lp.predict(data_sample)[0]

def locations(path=None):
    _, y = get_train_data()
    occurrences = Counter(y)
    for key, value in occurrences.items():
        print("{}: {}".format(key, value))