import pandas as pd
import matplotlib.pyplot as plt

file_name = "2_ratechange.csv"
data = pd.read_csv(file_name)

data_rate=data["Data Rate"]
aggre_throughput = data["Aggregate Throughput"]

plt.figure(figsize=(10, 6))
plt.plot(data_rate, aggre_throughput, marker='o', color='b', label="Aggregate Throughput")
plt.title("Aggregate Throughput vs Data Rate", fontsize=16)
plt.xlabel("Data Rate", fontsize=14)
plt.ylabel("Aggregate Throughput", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 保存并显示图表
plt.savefig("2aggregate_throughput_vs_data_rate.png", dpi=300)
plt.show()