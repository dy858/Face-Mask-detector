import face_recognition
from PIL import Image, ImageDraw
import math
import numpy as np
face_image_path = '../data/without_mask/3.jpg'
mask_image_path = '../data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)
face_image = Image.fromarray(face_image_np)

face_landmark_image = Image.fromarray(face_image_np)
mask_image = Image.open(mask_image_path)
draw = ImageDraw.Draw(face_landmark_image)


for face_landmark in face_landmarks:
    chin1 = face_landmark['chin'][1]
    chin15 = face_landmark['chin'][15]

    mask_ratio_width = 1.1
    #마스크 너비 구하기
    mask_width = int(math.sqrt((chin1[0] - chin15[0]) ** 2 + (chin1[1] - chin15[1]) ** 2) * mask_ratio_width)

    a = float(chin1[0] - chin15[0])
    degree = (math.acos(a / mask_width))
    print(degree)
    mask_image = mask_image.rotate(np.pi / 2 - degree, expand=True)

    chin8 = face_landmark['chin'][8]
    nose28 = face_landmark['nose_bridge'][1]

    mask_center_x = (chin15[0] + chin1[0]) // 2
    mask_center_y = (chin8[1] + nose28[1]) // 2
    mask_ratio_height = 1
    #마스크 높이 구하기
    mask_height = int(math.sqrt((chin8[0] - nose28[0]) ** 2 + (chin8[1] - nose28[0]) ** 2) * mask_ratio_height)

    mask_image = mask_image.resize((mask_width, mask_height))

    mask_position_x = mask_center_x - mask_image.width // 2
    mask_position_y = mask_center_y - mask_image.height // 2

    #얼굴 각도(기울기)
    #slope = (chin15[1] - chin1[1]) / (chin15[0] - chin1[0])
    #angle = np.pi/2 - np.arctan(slope)
    #print(angle * np.pi / 180)

    #mask_image = mask_image.rotate(angle, expand = True)


    face_landmark_image.paste(mask_image, (mask_position_x, mask_position_y) , mask_image)


face_landmark_image.show()