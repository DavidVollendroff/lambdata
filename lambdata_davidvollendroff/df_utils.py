"""
Utility functions for working with DataFrames
"""

import pandas
import numpy as np

TEST_DF = pandas.DataFrame([1,2,3])

def explore_df(dataframe):
    print(dataframe.describe())
    print('Null Values\n', dataframe.isnull().value_counts())
    print('Head\n', dataframe.head())
    print('Tail\n', dataframe.tail())

class O:
    """
    A square shaped block for my PyTetris game.
    """
    def __init__(self):
        self.type = "O"
        self.color = (255, 255, 0)
        mold = np.zeros([24, 10]) # framework for falling piece
        mold[1, 4:6] = 1 # placing 1s where the piece begins
        mold[2, 4:6] = 1
        self.position = mold

        self.position = [self.position, self.position, self.position, self.position] # square blocks look the same under rotation
           
