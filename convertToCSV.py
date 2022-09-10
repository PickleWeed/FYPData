import pandas as pd

filePath = "HostData.json"
csvPath = "HostData.csv"

df = pd.read_json(filePath)

# add header
headerList = ['id', 'Advisor', 'HARoleplay', 'DateTime', 'GameResults']

df.to_csv(csvPath, header=headerList, index=None)

df = pd.read_csv(csvPath)
# print(df)
split_df = pd.DataFrame(df['GameResults'].tolist())

# split and concatenate
print(split_df)
df.to_csv(csvPath, index=None)
