import face_recognition
from PIL import Image, ImageDraw


face_image_path = 'data/without_mask/1.jpg'
mask_image_path = 'data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)
face_image = Image.fromarray(face_image_np)

face_landmark_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmark_image)

for face_landmark in face_landmarks:
    face_landmark['chin']
    for feature_name, points in face_landmark.items():
        #print(feature_name, points)
        #for point in points:
        if feature_name == 'chin':
            draw.point(points[2])
            draw.point(points[len(points)-2])
            draw.point(points[8])
            x = points[15][0] - points[2][0]
            x_1 = points[2][0]
            a = points[8][1]
        if feature_name == 'nose_bridge':
            draw.point(points[2])
            b = points[2][1]


#마스크의 세로길이는 콧대2번-턱8번(y좌표)
#마스크의 가로길이는 턱15번-턱2번(x좌표)
#2,8,14,29 points
#x = int(face_landmarks[0][0][15][0] - face_landmarks[0][0][2][0])
#y = int(face_landmarks[0][3][2][1] - face_landmarks[0][0][8][1])

print(abs(x), abs(b - a))
y = abs(b - a)
mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((int(1.2 * abs(x)), int(1.2 * abs(y))))
face_image.paste(mask_image, (int(x_1 - 0.2*x), int(b)), mask_image)

#chin에서 3번째의 좌표를 찍으려면
#draw.point(points[2])


#face_landmark_image.show()
face_image.show()

#회전하지 않은 경우
#chin에서 y좌표가 가장 큰 부분을 찾고
#nose bridge에서 2번째로 작은 좌표를 찾고
#chin에서 3번째로 큰  x좌표, 3번째로 작은 x좌표를 가져온다