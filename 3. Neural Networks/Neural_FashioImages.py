# TensorFlow and tf.keras
print(" \\ -- \\ -- \\ -- \\ -- \\ -- ")
print(" ")

import tensorflow as tf
from tensorflow import keras
# Helper libraries
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

print(tf.__version__)

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

test_images.shape


model = keras.Sequential([ 
    keras.layers.Flatten(input_shape=(28,28)), 
    keras.layers.Dense(128, activation = "relu"),
    keras.layers.Dense(10, activation ="softmax")
])

model.compile(optimizer='adam',
              loss= keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs = 10)

#test_loss, test_acc = model.evaluate(test_images, test_labels)

#print("testes acc", test_acc)

# model is trained~

prediction = model.predict(test_images)
#prediction = model.predict(test_images[7])
class_names[test_labels[9]]


for i in range(8, 10):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("prediction " + class_names[np.argmax(prediction[i])])
    plt.show()
