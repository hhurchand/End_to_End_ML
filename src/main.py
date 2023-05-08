import numpy as np
import pandas as pd
import argparse
def read_data():
    df = pd.read_csv("../data/processed/train.csv")
    return df
