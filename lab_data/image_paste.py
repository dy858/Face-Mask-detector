import face_recognition
from PIL import Image, ImageDraw

image_path = '../data/without_mask/0.jpg'
face_image_path = '../data/without_mask/0.jpg'
mask_image_path = '../data/mask.png'

face_image_np = face_recognition.load_image_file(image_path)
face_image_np = face_recognition.load_image_file(face_image_path)
face_image = Image.fromarray(face_image_np)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)
#draw = ImageDraw.Draw(face_image)

face_landmark_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmark_image)

for face_location in face_locations:
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
    #draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=2)
    #draw.rectangle(((left, 1.3*top), (right, bottom)), outline=(255, 255, 0), width=4)

x = abs(right - left )*1.2
y = abs(top - bottom)*0.8

mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((int(x), int(y)))
face_image.paste(mask_image, (int(0.8*left), int(top*1.4)), mask_image)

face_image.show()