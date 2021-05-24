from urllib.request import Request, urlopen
import json
import os

api_url = 'https://api.github.com/repos/prajnasb/observations/contents/experiements/data/without_mask?ref=master'

#브라우저 정보
hds = {'User-Agent': 'Mozilla/5.0'}

request = Request(api_url, headers=hds)
#요청 보내기
response = urlopen(request)
directory_bytes = response.read()
#웹사이트 정보가 들어옴/불러들여짐

#문자열로 변환
directory_str = directory_bytes.decode('utf-8')
#배열로 변환
contents = json.loads(directory_str)

#download_url을 불러옴
for i in range(len(contents)):
    content = contents[i]
    #print(content['download_url'])
    request = Request(content['download_url'], headers=hds)
    response = urlopen(request)
    #9 11과 같다, 이미지 데이터를 가져옴
    image_data = response.read()

    #데이터 폴더가 있는지 확인힌다,없으면 만든다
    if not os.path.exists('../data'):
        os.mkdir('../data')#폴더가 만들어진다
    if not os.path.exists('../data/without_mask'):
        os.mkdir('../data/without_mask')

    #이미지 파일로 쓰여진다
    image_file = open('data/without_mask/'+ content['name'],'wb')
    image_file.write(image_data)
    print('다운로드 완료('+str(i+1) + '/' + str(len(contents)) + '): ' + content['name'])
    #다운로드 완료(10/500): 10.jpg

     #지우면 전체 파일이 다운받아진다(break)


#깃허브에서 제공하는 api를 통해 url을 뽑아냄





#제이슨으로 변환시켜 데이터를 뽑아낸다

