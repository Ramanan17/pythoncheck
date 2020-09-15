import pandas as pd
import numpy as np
mean =0;
std =1
data =np.random.normal(mean, std, size=(10, 4))
index = [i for i in range(1, len(data)+1)]
columns =[i for i in range(1, 5)]
df = pd.DataFrame(data, index=index,columns=columns)
print(df)
print("Now printing the first row values")
print(df.iloc[0])
change = df.iloc[0]
print("Now printing the first row values where values are greater than zero")
print(change[df.iloc[0]>0])
