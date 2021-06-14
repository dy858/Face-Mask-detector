import matplotlib.pyplot as plt
import tensorflow as tf
import numpy

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

rc_train_dataset = train_dataset.map(lambda x, y: (resize_and_crop(x), y))
rc_valid_dataset = valid_dataset.map(lambda x, y: (resize_and_crop(x), y))

model = tf.keras.models.load_model('../models/mymodel')


plt.figure(0)
plt.title('valid dataset predict')

for images, labels in valid_dataset.take(1):
    rc_images = resize_and_crop(images)
    predict = model.predict(rc_images)
    print(predict)
    for i in range(16):
        plt.subplot(4, 4, i+1)
        plt.imshow(images[i].numpy().astype('uint8'))
        plt.axis('off')
        if predict[i][0] > 0.5:
            predict_index = 1
        else:
            predict_index = 0

        if predict_index == labels[i]:
            result = 'ok'

        else:
            result = 'wrong'

        plt.title(valid_dataset.class_names[predict_index] + '\n' + result)
        plt.axis('off')

plt.show()