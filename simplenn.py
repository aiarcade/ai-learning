import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation


model=Sequential()
model.add(Dense(1, input_dim=2,activation='relu'))
#model.add(Dense(1, input_dim=2,activation='relu'))
model.compile(loss='mean_squared_error', optimizer='adam')

X=np.array([[1,2],[3,2],[4,5],[6,5],[1,5]])
y=np.array([1,10,1,10,1])

model.fit(X,y,epochs=10000)
print model.predict(X)
