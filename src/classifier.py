import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
from data import get_training_data

def train_random_forest():
    model_file = "../data/rf.pkl"
    X, y = get_training_data()
    lp = make_pipeline(DictVectorizer(sparse=False), RandomForestClassifier(n_estimators=100, class_weight="balanced"))
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp

def train_xgb():
    model_file = "../data/xgb.pkl"
    X, y = get_training_data()
    if len(X) == 0:
        raise ValueError("No wifi access points have been found during training")
    #lp = make_pipeline(DictVectorizer(sparse=False), GradientBoostingClassifier(n_estimators=100))
    lp = make_pipeline(DictVectorizer(sparse=False), MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1))
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp


def train_model_neural_network():
    model_file = "../data/nn.pkl"
    X, y = get_training_data()
    if len(X) == 0:
        raise ValueError("No wifi access points have been found during training")
    lp = make_pipeline(DictVectorizer(sparse=False), DecisionTreeClassifier(max_depth=None, min_samples_split=2, random_state=0))
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp

def get_model(model):
    model_file = "../data/" + model + ".pkl"
    with open(model_file, "rb") as f:
        lp = pickle.load(f)
    return lp

def train_all():
    train_random_forest()
    train_xgb()
    train_model_neural_network()