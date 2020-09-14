import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, ELU
from keras.layers.convolutional import Convolution2D, MaxPooling2D, Cropping2D
from keras.layers import Lambda
shape = [160,320,3]

model = Sequential()
model.add(Lambda(lambda x:x/255-0.5, input_shape=shape))
model.add(Cropping2D(cropping=((70,25), (0,0)), input_shape=shape))
model.add(Convolution2D(24, 5, 5, subsample=(2,2) ,activation='relu'))
model.add(Convolution2D(36, 5, 5, subsample=(2,2) ,activation='relu'))
model.add(Dropout(0.5))
model.add(Convolution2D(48, 5, 5, subsample=(2,2) ,activation='relu'))
model.add(Dropout(0.5))
model.add(Convolution2D(64, 3, 3, activation='relu'))
model.add(Convolution2D(64, 3, 3, activation='relu'))
#model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="tf"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))
model.compile(loss='mse', optimizer="adam")


# Train model
X_train = np.load('X_train_easy.npy')
y_train = np.load('y_train_easy.npy')
model.fit(X_train, y_train, epochs=3, validation_split=0.1, shuffle=True)

# Save model
model.save('model_easy.h5')
