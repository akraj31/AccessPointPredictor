import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
from data import get_training_data

def train_random_forest(X, y):
    model_file = "../data/rf.pkl"
    X, y = get_training_data(path)
    lp = make_pipeline(DictVectorizer(sparse=False), RandomForestClassifier(n_estimators=100, class_weight="balanced"))
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp

def train_xgb(X, y):
    model_file = "../data/xgb.pkl"
    X, y = get_train_data(path)
    if len(X) == 0:
        raise ValueError("No wifi access points have been found during training")
    lp = make_pipeline(DictVectorizer(sparse=False), RandomForestClassifier(n_estimators=100, class_weight="balanced"))
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp


def train_model_neural_network(X, y):
    model_file = "../data/nn.pkl"
    X, y = get_train_data(path)
    if len(X) == 0:
        raise ValueError("No wifi access points have been found during training")
    lp = make_pipeline(DictVectorizer(sparse=False), RandomForestClassifier(n_estimators=100, class_weight="balanced"))
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp

def get_model(model="rf"):
    model_file = "../data/" + model
    with open(model_file, "rb") as f:
        lp = pickle.load(f)
    return lp