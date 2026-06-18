import pandas as pd

df = pd.read_csv("data/conversations.csv")

lengths = []

for _, row in df.iterrows():

    conversation = str(row.iloc[0])

    count = len(
        conversation.split("\n")
    )

    lengths.append(count)

print("Rows:", len(lengths))
print("Average:", sum(lengths)/len(lengths))
print("Max:", max(lengths))
print("Min:", min(lengths))