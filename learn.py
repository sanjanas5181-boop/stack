import pandas as pd
import os
csv_path=os.path.join(os.path.dirname(__file__),'student_marks.csv')
df=pd.read_csv(csv_path)
#print(df)
#print(df.head())
#print(df.tail(3))
#print(df.shape)
#print(df.info())
#print(df.describe())
#print(df.columns)
# names_series= df ['name']
# print(names_series)
# print(type(names_series))
# print(type(df))
# print(df.iloc[0])
# print(df.loc[0,'name'])
# print(df.iloc[0:3,1:3])
# df_filtered=df[df["Name"]=="Eve davis"]
# print("students who scored>50:",df_filtered)
# df_filtered=df[df["Score"]<50]
# print("students who scored<50:",df_filtered) 
# top_science=df[(df['Subject']=='Science') & (df['Class']=='10A')]
# print(top_science)
# top_Math=df[(df['Subject']=='Math') & (df['Class']=='10A')]
# print(top_Math) 
# subject_avg=df.groupby('Subject')['Score'].mean()
# print(subject_avg) 
# Class_subject_avg=df.groupby(['Class','Subject'])['Score'].mean()
# print(Class_subject_avg)
#Aggregations
# pivot_table
# pivot_table=df.pivot_table(index='Subject',columns='Class',values='Score',aggfunc='mean')
# print(pivot_table)
# january_sales=pd.DataFrame({"Item":["Apple","Banana"],"Sales":[100,150]})
# february_sales=pd.DataFrame({"Item":["Cherry","Dates"],"Sales":[200,50]})
# print(january_sales)
employees=pd.DataFrame({
    "Emp_ID":[1,2,3],
    "name":["john","sarah","mike"]
})
salaries = pd.DataFrame({
    "Emp_ID":[1,2,3],
    "salary":[60000,80000,75000]
})
full_employee_data=pd.merge(employees,salaries,on="Emp_ID")
print("merged employee table:\n",full_employee_data)




