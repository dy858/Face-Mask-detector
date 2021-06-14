import tensorflow as tf
import matplotlib.pyplot as plt
import os

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    validation_split=0.2,
    subset='training',
    seed=777,
    image_size=(224, 224),
    batch_size=16
)

valid_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    validation_split=0.2,
    subset='validation',
    seed=777,
    image_size=(224, 224),
    batch_size=16
)

resize_and_crop = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomCrop(height=224, width=224),
tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
])

#재료로 쓰일 데이터
rc_train_dataset = train_dataset.map(lambda x, y: (resize_and_crop(x), y))
rc_valid_dataset = valid_dataset.map(lambda x, y: (resize_and_crop(x), y))

model = tf.keras.applications.MobileNet(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

model.trainable = False

model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalAveragePooling2D(), #연산량이 줄어들게 된다.
    tf.keras.layers.Dense(1)
])

learning_rate = 0.001
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), #분류문제에 적합한 학습이다
    optimizer=tf.keras.optimizers.RMSprop(lr=learning_rate),
    metrics=['accuracy']

)

print(model.summary())

history = model.fit(rc_train_dataset, epochs=4, validation_data=rc_valid_dataset)
print(history)


if not os.path.exists('../models'):
    os.mkdir('../models')

model.save('../models/mymodel')