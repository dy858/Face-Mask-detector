from urllib.request import Request, urlopen
import json

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
    print(content['download_url'])


#깃허브에서 제공하는 api를 통해 url을 뽑아냄





#제이슨으로 변환시켜 데이터를 뽑아낸다

