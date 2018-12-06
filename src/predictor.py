import json
from collections import Counter
from data import get_training_data, get_sample, get_external_sample, aps_to_dict
from access_points import get_scanner
from classifier import get_model

def predict_proba(data_sample=None):
    if not data_sample:
        data_sample = get_sample() 
    lp_rf = get_model("rf")
    lp_xgb = get_model("xgb")
    lp_nn = get_model("nn")

    rf = dict(zip(lp_rf.classes_, lp_rf.predict_proba(data_sample)[0]))
    xgb = dict(zip(lp_xgb.classes_, lp_xgb.predict_proba(data_sample)[0]))
    nn = dict(zip(lp_nn.classes_, lp_nn.predict_proba(data_sample)[0]))
    print(rf, xgb, nn)
    final = rf
    for k,v in xgb.items():
        final[k] += v
    for k,v in nn.items():
        final[k] += v

    max_v = -1
    max_k = None
    for k,v in final.items():
        if v>max_v:
            max_v = v
            max_k = k
    print("Final Prediction: ", max_k)

def predict(data_sample=None):
    if not data_sample:
        data_sample = get_sample() 
    data_sample = get_sample()
    lp_rf = get_model("rf")
    lp_xgb = get_model("xgb")
    lp_nn = get_model("nn")
    print(lp_rf.predict(data_sample)[0])
    print(lp_xgb.predict(data_sample)[0])
    print(lp_nn.predict(data_sample)[0]) 

def locations(path=None):
    _, y = get_training_data()
    occurrences = Counter(y)
    for key, value in occurrences.items():
        print("{}: {}".format(key, value))
