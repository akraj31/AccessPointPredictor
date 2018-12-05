import json
from collections import Counter
from data import get_training_data, sample, get_external_sample, aps_to_dict
from access_points import get_scanner

from classifier import get_model
from whereami.compat import cross_val_score


def predict_proba(input_path=None, model_path=None, device=""):
    data_sample = sample(device) if input_path is None else get_external_sample(input_path)
    lp_rf = get_model(model_path)
    lp_xgb = get_model(model_path)
    lp_nn = get_model(model_path)
    print(json.dumps(dict(zip(lp_rf.classes_, lp_rf.predict_proba(data_sample)[0]))))
    print(json.dumps(dict(zip(lp_xgb.classes_, lp_xgb.predict_proba(data_sample)[0]))))
    print(json.dumps(dict(zip(lp_nn.classes_, lp_nn.predict_proba(data_sample)[0]))))


def predict(input_path=None, model_path=None, device=""):
    data_sample = sample(device) if input_path is None else get_external_sample(input_path)
    lp_rf = get_model(model_path)
    lp_xgb = get_model(model_path)
    lp_nn = get_model(model_path)
    print(lp_rf.predict(data_sample)[0])
    print(lp_xgb.predict(data_sample)[0])
    print(lp_nn.predict(data_sample)[0]) 
    return lp.predict(data_sample)[0]


def crossval(clf=None, X=None, y=None, folds=10, n=5, path=None):
    if X is None or y is None:
        X, y = get_train_data(path)
    if len(X) < folds:
        raise ValueError('There are not enough samples ({}). Need at least {}.'.format(len(X), folds))
    clf = clf or get_model(path)
    tot = 0
    print("KFold folds={}, running {} times".format(folds, n))
    for i in range(n):
        res = cross_val_score(clf, X, y, cv=folds).mean()
        tot += res
        print("{}/{}: {}".format(i + 1, n, res))
    print("-------- total --------")
    print(tot / n)
    return tot / n

def locations(path=None):
    _, y = get_train_data(path)
    occurrences = Counter(y)
    for key, value in occurrences.items():
        print("{}: {}".format(key, value))


class Predicter():
    def __init__(self, model=None, device=""):
        self.model = model
        self.device = device
        self.clf = get_model(model)
        self.wifi_scanner = get_scanner(device)
        self.predicted_value = None

    def predict(self):
        aps = self.wifi_scanner.get_access_points()
        self.predicted_value = self.clf.predict(aps_to_dict(aps))[0]
        return self.predicted_value

    def refresh(self):
        self.clf = get_model(self.model)
        self.wifi_scanner = get_scanner(self.device)