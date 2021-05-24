#데이터 파트의 최종 코드
from urllib.request import Request, urlopen
import json
import os

import face_recognition
from PIL import Image, ImageDraw
import numpy as np


#다운로드 기능(without maks, with mask, 마스크 이미지)
def download_image(kind):
    if kind == 'without_mask':
        api_url = 'https://api.github.com/repos/prajnasb/observations/contents/experiements/data/without_mask?ref=master'
        hds = {'User-Agent': 'Mozilla/5.0'}

        request = Request(api_url, headers=hds)
        response = urlopen(request)
        directory_bytes = response.read()
        directory_str = directory_bytes.decode('utf-8') #문자열 형태로 변환

        contents = json.loads(directory_str) #파이썬의 자료구조(블록단위)로 가공된 상태

        for i in range(len(contents)): #i는 인덱스
            content = contents[i] #다운로드 유알엘을 뽑아야 한다

            request = Request(content['download_url'])
            response = urlopen(request)
            image_data = response.read()

            if not os.path.exists('data'):
                os.mkdir('data')
            if not os.path.exists('data/without_mask'):
                os.mkdir('data/without_mask')

            image_file = open('data/without_mask/' + content['name'], 'wb')
            image_file.write(image_data)
            image_file.close()
            print('without_mask 이미지 다운로드 중 (' + str(i+1) + '/'+str(len(contents)) + '): '+content['name'])
        print('without_mask 이미지 다운로드 완료')



    elif kind == 'with_mask':
        api_url = 'https://api.github.com/repos/prajnasb/observations/contents/experiements/data/with_mask?ref=master'
        hds = {'User-Agent': 'Mozilla/5.0'}

        request = Request(api_url, headers=hds)
        response = urlopen(request)
        directory_bytes = response.read()
        directory_str = directory_bytes.decode('utf-8')  # 문자열 형태로 변환

        contents = json.loads(directory_str)  # 파이썬의 자료구조(블록단위)로 가공된 상태

        for i in range(len(contents)):  # i는 인덱스
            content = contents[i]  # 다운로드 유알엘을 뽑아야 한다

            request = Request(content['download_url'])
            response = urlopen(request)
            image_data = response.read()

            if not os.path.exists('data'):
                os.mkdir('data')
            if not os.path.exists('data/with_mask'):
                os.mkdir('data/with_mask')

            image_file = open('data/with_mask/' + content['name'], 'wb')
            image_file.write(image_data)
            image_file.close()
            print('with_mask 이미지 다운로드 중 (' + str(i + 1) + '/' + str(len(contents)) + '): ' + content['name'])
        print('with_mask 이미지 다운로드 완료')
    elif kind == 'mask':
        mask_image_download_url = 'https://github.com/prajnasb/observations/raw/master/mask_classifier/Data_Generator/images/blue-mask.png'

        request = Request(mask_image_download_url)
        response = urlopen(request)
        image_data = response.read()

        if not os.path.exists('data'):
            os.mkdir('data')

        image_file = open('data/mask.png')
        image_file.write(image_data)
        image_file.close()
        print('mask 이미지 다운로드 완료')

#점과 점 사이의 거리 함수
def distance_point_to_point(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#마스크 합성 기능
def mask_processing(face_image_file_name):
    #이미지 경로 생성
    face_image_path = 'data/without_mask' + face_image_file_name
    mask_image_path = 'data/mask.png'

    #얼굴 영역 추출,얼굴 랜드마크 추출
    face_image_np = face_recognition.load_image_file(face_image_path)
    face_locations = face_recognition.face_locations(face_image_np)
    face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

    #결과 이미지
    face_image = Image.fromarray(face_image_np) #원본 그대로 준비
    mask_image = Image.open(mask_image_path)

    face_count = 0


    #마스크 합성
    for face_landmark in face_landmarks:
        if ('nose_bridge' not in face_landmark) or ('chin' not in face_landmark):
            continue

        #마스크 너비 보정값(1.2배)
        mask_width_ratio = 1.2

        #마스크 높이 계산 ( 노즈 브릿지 2번쨰 점 , 친 9번째 점 사이의 길이)
        maks_height = int(distance_point_to_point(face_landmark['nose_bridge'][1], face_landmark['chin'][8]))

        #마스크 좌/우 분할
        mask_left_image = mask_image.crop((0, 0, mask_image.width // 2, mask_image.height)) #복사본으로 원본에는 손상이 없다
        mask_right_image = mask_image.crop((mask_image.width // 2, 0, mask_image.width, mask_image.height))
        #왼쪽 얼굴 너비 계산

        #왼쪽 마스크 크기 조절

        #오른쪽 얼굴 너비 계산

        #오른쪽 마스크 크기 조절

        #좌/우 마스크 크기 연결

        #얼굴 회전 각도 계산

        #마스크 회전




    #결과 이미지 반환
    return face_image, face_count








#데이터 생성 함수   (총 3가지 함수 생성)


#외부에서 불러올 때는 실행되지 않는다
if __name__ == '__main__':
    download_image('without_mask')

