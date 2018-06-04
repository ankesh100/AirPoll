import os,sys
from stat import *
import pandas as pd
import numpy as np
import pandas
import numpy
from sklearn.model_selection import train_test_split
df=pd.read_csv('/home/ankesh/Desktop/AQI-Air-quality-index/data/Air_Quality_RSPM_2008.csv')
feature_col_name=['Numbers of  monitoring days (n)','Respirable Suspended Particulate Matter(RSPM)- Annual average (µg/m3)','Percentage- exceedence(24 hourly)']
predicted_classname=['Air Quality']
#lol={'Low':0,'Moderate':0,'High':1,'Critical':1}
lol={'Low':0,'Moderate':1,'High':2,'Critical':3}
df['Air Quality']=df['Air Quality'].fillna('Moderate')
df['Air Quality']=df['Air Quality'].map(lol)
x=df[feature_col_name].values
y=df[predicted_classname].values
def main(StringData):
    inputData = StringData.split(' ')
    inputData = [float(elem) for elem in inputData]
    inputData = [inputData]

    from sklearn.tree import DecisionTreeClassifier
    dt_model=DecisionTreeClassifier(random_state=0)
    dt_model.fit(x,y.ravel())
    #rf_test_predict=rf_model.predict_proba(inputData)
    dt_test_predict=dt_model.predict(inputData)
    #print("%-30s%-4.2f%-1s"%('Likelihood of Heart Disease is ',100*rf_test_predict[0][1],'%'))
    #print(dt_test_predict)
    if dt_test_predict==[0]:
    	print('Risk Impact of Air Pollution: Low')
    elif dt_test_predict==[1]:
    	print('Risk Impact of Air Pollution: Moderate')
    elif dt_test_predict==[2]:
    	print('Risk Impact of Air Pollution: High')
    elif dt_test_predict==[3]:
    	print('Risk Impact of Air Pollution: Critical')
if __name__ == "__main__":
    inputs = ' '.join(sys.argv[1:])
    
    main(inputs)

