import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
#dataset:does spending more money on ads increase sales?
data={
    "Ad_budget":[1000,2000,3000,4000,5000,6000,7000,8000],
    "sales":[150,300,450,600,750,900,1050,1200]
}
df=pd.DataFrame(data)
x=df[["Ad_budget"]]
y=df["sales"]
#we hold back 25% of the data for testing .random_state ensures we get the same split every time we run the file.
x_train, x_test ,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
print("training data length(80%):",len(x_train))
print("testing data length(20%):",len(x_test))
model=LinearRegression()
model.fit(x_train,y_train)
print("model successfully trained")
predictions=model.predict(x_test)
print("the model guessed:",predictions)
print("the actual truth :",y_test.values)
error=mean_absolute_error(y_test,predictions)
print(f"mean absolute error (MEA):{error}")
print("if MAE is 0.0,the model is literally predicting the future perfectly!")
new_budget=pd.DataFrame({"Ad_budget":[5500]})
new_predictions=model.predict(new_budget)
print("the model guessed for sales in 5500 budget:",new_predictions)