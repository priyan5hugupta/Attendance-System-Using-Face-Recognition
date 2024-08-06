from tensorflow.keras.layers import Input, Lambda, Dense, Flatten,Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
import numpy as np
import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt
import shutil
train_path="D:/Minor 2/Preprocessing/splitdataset/train"
test_path="D:/Minor 2/Preprocessing/splitdataset/test"
val_path="D:/Minor 2/Preprocessing/splitdataset/valid"
x_train=[]

for folder in os.listdir(train_path):

    sub_path=train_path+"/"+folder

    for img in os.listdir(sub_path):

        image_path=sub_path+"/"+img
    
        img_arr=cv2.imread(image_path)

        if img_arr is not None:
        # Resize the image
            img_arr = cv2.resize(img_arr, (224, 224))
        else:
            print(f"Failed to load image: {image_path}")
        x_train.append(img_arr)

x_test=[]

for folder in os.listdir(test_path):

    sub_path=test_path+"/"+folder

    for img in os.listdir(sub_path):

        image_path=sub_path+"/"+img
        img_arr=cv2.imread(image_path)

         # Load the image
        img_arr = cv2.imread(image_path)

    # Check if the image is loaded successfully
        if img_arr is not None:
        # Resize the image
            img_arr = cv2.resize(img_arr, (224, 224))
        else:
            print(f"Failed to load image: {image_path}")

        x_test.append(img_arr)

    

   
x_val=[]

for folder in os.listdir(val_path):

    sub_path=val_path+"/"+folder

    for img in os.listdir(sub_path):

        image_path=sub_path+"/"+img
    
        img_arr=cv2.imread(image_path)

        img_arr=cv2.resize(img_arr,(224,224))
        if img_arr is not None:
        # Resize the image
            img_arr = cv2.resize(img_arr, (224, 224))
        else:
            print(f"Failed to load image: {image_path}")
        x_val.append(img_arr)
train_x=np.array(x_train)
test_x=np.array(x_test)
val_x=np.array(x_val)
train_x=train_x/255.0
test_x=test_x/255.0
val_x=val_x/255.0
train_datagen = ImageDataGenerator(rescale = 1./255)
test_datagen = ImageDataGenerator(rescale = 1./255)
val_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory(train_path,
                                                 
                                                 batch_size = 32,
                                                 class_mode = 'sparse')
test_set = test_datagen.flow_from_directory(test_path,
                                          
                                            batch_size = 32,
                                            class_mode = 'sparse')
val_set = val_datagen.flow_from_directory(val_path,
                                            
                                            batch_size = 32,
                                            class_mode = 'sparse')
train_y=training_set.classes
test_y=test_set.classes
val_y=val_set.classes
training_set.class_indices
train_y.shape,test_y.shape,val_y.shape
IMAGE_SIZE = [224, 224]
vgg = VGG19(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)
#do not train the pre-trained layers of VGG-19
for layer in vgg.layers:
    layer.trainable = False
# Print unique label values in training labels
unique_labels = np.unique(train_y)
s = len(unique_labels) + 1
print(len(unique_labels))

x = Flatten()(vgg.output)
#adding output layer.Softmax classifier is used as it is multi-class classification
prediction = Dense(s, activation='softmax')(x)

model = Model(inputs=vgg.input, outputs=prediction)
# view the structure of the model
model.summary()
model.compile(
  loss='sparse_categorical_crossentropy',
  optimizer="adam",
  metrics=['accuracy']
)
from tensorflow.keras.callbacks import EarlyStopping
early_stop=EarlyStopping(monitor='val_loss',mode='min',verbose=1,patience=5)
#Early stopping to avoid overfitting of model
# fit the model
history = model.fit(
  train_x,
  train_y,
  validation_data=(val_x,val_y),
  epochs=10,
  callbacks=[early_stop],
  batch_size=32,shuffle=True)
# accuracies

plt.plot(history.history['accuracy'], label='train acc')

plt.plot(history.history['val_accuracy'], label='val acc')

plt.legend()

plt.savefig('vgg-acc-rps-1.png')

plt.show()
# loss
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.savefig('vgg-loss-rps-1.png')
plt.show()
model.evaluate(test_x,test_y,batch_size=32)
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import numpy as np
#predict
y_pred=model.predict(test_x)
y_pred=np.argmax(y_pred,axis=1)
#get classification report
print(classification_report(y_pred,test_y))
#get confusion matrix
print(confusion_matrix(y_pred,test_y))
model.save('D:/Minor 2/model.h5')

shutil.rmtree('D:/Minor 2/Preprocessing/cropped face')
print(f"Directory removed")
