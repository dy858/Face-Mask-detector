import face_recognition
from PIL import Image, ImageDraw


face_image_path = 'data/without_mask/1.jpg'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

face_landmark_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmark_image)

for face_landmark in face_landmarks:
    for feature_name, points in face_landmark.items():
        print(feature_name, points)
        #for point in points:
        if feature_name == 'chin':
            draw.point(points[2])
            draw.point(points[len(points)-2])
            draw.point(points[8])
        if feature_name == 'nose_bridge':
            draw.point(points[2])

#마스크의 세로길이는 콧대2번-턱8번(y좌표)
#마스크의 가로길이는 턱15번-턱2번(x좌표)
#2,8,14,29 points


#chin에서 3번째의 좌표를 찍으려면
#draw.point(points[2])


face_landmark_image.show()

#회전하지 않은 경우
#chin에서 y좌표가 가장 큰 부분을 찾고
#nose bridge에서 2번째로 작은 좌표를 찾고
#chin에서 3번째로 큰  x좌표, 3번째로 작은 x좌표를 가져온다