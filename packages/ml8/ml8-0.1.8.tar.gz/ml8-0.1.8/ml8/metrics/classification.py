"""

"""
from sklearn import metrics

def accuracy_score(y_true, y_pred, normalize=True, sample_weight=None):
    return metrics.accuracy_score(y_true, y_pred, normalize=normalize, sample_weight=sample_weight)

def confusion_matrix(y_true, y_pred, labels=None, sample_weight=None):
    return metrics.confusion_matrix(y_true, y_pred, labels=labels, sample_weight=sample_weight)

def classification_report(y_true, y_pred, labels=None, target_names=None,
                          sample_weight=None, digits=2):
    return metrics.classification_report(y_true, y_pred, labels=labels, target_names=target_names,
                                         sample_weight=sample_weight, digits=digits)

