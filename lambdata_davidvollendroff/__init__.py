"""
Collection of Data Science helper functions
"""


import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import seaborn as sns


def confusion_plot(y_true, y_pred, cmap='viridis'):
    """
    Plots a confusion matrix using the Seaborn library
    """
    labels = unique_labels(y_val)
    columns = [f'Predicted {label}' for label in labels]
    index = [f'Actual {label}' for label in labels]
    table = pd.DataFrame(confusion_matrix(y_true, y_pred),
                         columns=columns,
                         index=index)
    return sns.heatmap(table, annot=True, fmt='d', cmap=cmap)


ONES = pd.DataFrame(np.ones(10))

ZEROS = pd.DataFrame(np.zeros(50))
