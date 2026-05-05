import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("student_scores")
X=df[['Hours']]
y=df[Scores']
X+train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
st.title("exam score predictor")
st.write("enter hours studied to predict exam score")
hours=st.number_input("Hours:",min_value=0.0,step=0.1)
if st.button("predict score"):
  predicted score = model.predict([[hourse]])[0]
  st.success(f"predicted score:{predicted_score:.2f}")
  st.write("###sample training data")
  st.dataframe(df)
