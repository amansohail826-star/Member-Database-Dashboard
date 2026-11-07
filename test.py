import pandas as pd

df = pd.DataFrame({
    "a":[1,2,3,4],
    "c":[1,2,3,4],
    "d":[1,2,3,4],
    "e":[1,2,3,4]
})
df1 = pd.DataFrame({
    "a":[5],
    "c":[5],
    "d":[5],
    "e":[5]
})

df = pd.concat([df,df1])
# print(df.head())
# p = list(df["a"])

# dict = {}
# for i in range(0,len(p)-1):
#     if 4 == p[i]:
#         # print(i)
#         print(df["a"][i])
#         # print(df[][i])

df = df.drop(axis=0,index=3)
print(df.head())





