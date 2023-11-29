import pandas as pd
import numpy as np
import tensorflow as tf

df = pd.read_csv('cardio_train.csv')

X = df.iloc[:, :12].values
Y = df.iloc[:, 12].values