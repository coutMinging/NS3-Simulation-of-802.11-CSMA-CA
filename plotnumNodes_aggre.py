import pandas as pd
import matplotlib.pyplot as plt

file_name = "63-127aggre.csv"
data = pd.read_csv(file_name)

nodes = data["Number of Nodes"]
throughput = data["Aggregate throughput"]

plt.figure(figsize=(10,6))
plt.plot(nodes,throughput,marker="o",linestyle="-",color="b", label="Aggregate throughput")
plt.xlabel("Number of Nodes", fontsize=12)
plt.ylabel("Aggregate Throughput", fontsize=12)
plt.title("Aggregate Throughput vs Number of Nodes (CWmin=63, CWmax=127)",fontsize=14)
plt.grid(True,linestyle="--",alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig("63-127numNode_aggre.png")
plt.show()


