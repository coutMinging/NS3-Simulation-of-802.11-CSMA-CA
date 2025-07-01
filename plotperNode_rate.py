import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
file_name = "2_ratechange.csv"
data = pd.read_csv(file_name)

# 提取数据
data_rate = data["Data Rate"]
node_throughputs = data.iloc[:, 1:11]  # 提取 Node 0 到 Node 9 的 Throughput

# 绘制 Node 0 到 Node 9 的 Throughput 图
plt.figure(figsize=(12, 8))
for i, column in enumerate(node_throughputs.columns):
    plt.plot(data_rate, node_throughputs[column], marker='o', label=f"{column}")

# 设置标题和标签
plt.title("Node 0-9 Throughput vs Data Rate", fontsize=16)
plt.xlabel("Data Rate", fontsize=14)
plt.ylabel("Throughput (Per Node)", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10, title="Nodes", loc="upper right")

# 保存并显示图表
plt.savefig("2node_0_9_throughput_vs_data_rate.png", dpi=300)
plt.show()