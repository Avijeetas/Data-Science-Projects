# -*- coding: utf-8 -*-
"""Car Prediction with ANN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10CUejnVE4-HNex3nfJxULDO0-rtO7tY9
"""

import pandas as pd
import numpy as np

from google.colab import files



#retrieve uploaded file
uploaded = files.upload()

#print results
for fn in uploaded.keys():

  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df=pd.read_csv('Car_Purchasing_Data.csv',encoding='ISO-8859-1')

df

sns.pairplot(df)

df.columns

X=df.drop(['Customer Name', 'Customer e-mail', 'Country','Car Purchase Amount'],axis=1)

X.shape

sns.scatterplot(x='Net Worth',y='Age',hue='Gender',data=df)

y=df['Car Purchase Amount']

y_scaled= y.values.reshape(-1,1)

from sklearn.preprocessing import MinMaxScaler
scaler= MinMaxScaler()
X_scaled=scaler.fit_transform(X)
scaler_y= MinMaxScaler()

y_scaled=scaler_y.fit_transform(y_scaled)
scaler.data_max_

from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test= train_test_split(X_scaled, y_scaled,test_size =.25 )

import tensorflow.keras
from keras.models import Sequential
from keras.layers import Dense

model= Sequential()

model.add(Dense(5,input_dim=5, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='linear'))

model.summary()

model.compile(optimizer='adam', loss='mean_squared_error')

hist= model.fit(X_train,y_train, epochs=100, batch_size=50, verbose=1, validation_split=.2)

hist_dict= hist.history
hist_dict.keys()

import matplotlib.pyplot as plt




plt.plot(hist_dict['loss'])

plt.plot(hist_dict['val_loss'])

import matplotlib.pyplot as plt

loss=hist_dict['loss']
val_loss=hist_dict['val_loss']


epochs=range(1,len(loss)+1)


plt.plot(epochs,loss,'bo',label='Training loss')

plt.plot(epochs,val_loss,'b',label='Validation loss')


plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

# Gender, Age, Annual Salary, Credit Card Debt, Net Worth 

# ***(Note that input data must be normalized)***

X_test_sample = np.array([[0, 0.4370344,  0.53515116, 0.57836085, 0.22342985]])

y_predict_sample = model.predict(X_test_sample)

print('Expected Purchase Amount=', y_predict_sample)
y_predict_sample_orig = scaler_y.inverse_transform(y_predict_sample)
print('Expected Purchase Amount=', y_predict_sample_orig)

