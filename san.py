import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data={
    "hours_studied":[2,3,5,7,9],
    "test_score":[55,60,75,85,95],
    "hours_playing_games":[5,4,2,1,0]
}
df=pd.DataFrame(data)
print(df)
corr_matrix=df.corr()
print(corr_matrix)
 

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix,annot=True,cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()