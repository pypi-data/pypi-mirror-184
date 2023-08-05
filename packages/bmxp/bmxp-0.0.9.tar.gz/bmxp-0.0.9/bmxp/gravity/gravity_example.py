"""
A quick example on how to use Gravity
"""
import pandas as pd

try:
    from bmxp.gravity import cluster
except:
    from __init__ import cluster

# load a dataset
df = pd.read_csv("bladder_cancer_full.csv", header=0, index_col="Compound_ID")
import time

times = []

t0 = time.time()
sample_df = cluster(
    df, 0.015, 0.95, batch_size=1000, method="spearman", nan_policy="fill"
)
print(time.time() - t0)
# print(df)

# add to our own dataframe
df["Cluster_Num"] = sample_df["Cluster_Num"]
df["Cluster_Size"] = sample_df["Cluster_Size"]

# record results
df.to_csv("results.csv")
