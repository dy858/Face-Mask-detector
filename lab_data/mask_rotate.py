from PIL import Image, ImageDraw
import face_recognition
import numpy as np

mask_image_path = '../data/mask.png'
face_image_path = '../data/without_mask/1.jpg'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

face_landmark_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmark_image)
mask_image = Image.open(mask_image_path)

for face_landmark in face_landmarks:
    nb = face_landmark['nose_bridge']
    #콧대를 기준으로 돌아간 각도를 구한다
    nb_top = nb[0]
    nb_bottom = nb[3]

    dx = nb_bottom[0] - nb_top[0]   #x변화량
    dy = nb_bottom[1] - nb_top[1]  #y변화량

    # 반시계방향으로 각도법으로 돌아감
    face_radian = np.arctan2(dy, dx)
    face_degree = np.rad2deg(face_radian)
    mask_degree = 90 - face_degree

    mask_image = mask_image.resize((80, 50))
    mask_image = mask_image.rotate(mask_degree, expand = True)

    face_landmark_image.paste(mask_image, (0, 0), mask_image)

face_landmark_image.show()
