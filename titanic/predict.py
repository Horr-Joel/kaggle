import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('train.csv')


Sex = {'female':0,'male':1}
df['Sex'] = df['Sex'].map(Sex)


