import pandas as pd
import numpy as np

df = pd.read_csv('Prueba.csv')
df['event_time']=pd.to_datetime(df['event_time']).dt.date
df.groupby(['event_time', 'event_type']).size()
print(df.groupby(['event_time', 'event_type']).size())
