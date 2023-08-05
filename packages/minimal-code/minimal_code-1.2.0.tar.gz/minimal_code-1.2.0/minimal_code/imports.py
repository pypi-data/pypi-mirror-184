#import modules
import pandas as pd

#load RR.csv dataset
def load_rr():
    return pd.read_csv("Data/RR.csv",header=None)