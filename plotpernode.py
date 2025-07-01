import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file
filename = "63-127pernode.csv"
df=pd.read_csv(filename)
df_numeric = df.iloc[:,1:].astype(float)
plt.figure(figsize=(12,6))
for column in df_numeric.columns:
    plt.plot(df_numeric.index,df_numeric[column],label=column)

plt.xlabel("Number of Nodes")
plt.ylabel("Throughput (Mbps)")

plt.title("Throughput VS Number of Nodes")
plt.legend()
plt.show()