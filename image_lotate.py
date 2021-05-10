#이미지 회전

from PIL import Image

mask_image_path = 'data/mask.png'
mask_image = Image.open(mask_image_path)

angle = 30
mask_image_rotate = mask_image.rotate(angle, expand = True)  #라디안이 아닌 도 사용, expand를 사용해 이미지가 잘리지 않고 출력
mask_image_rotate.show()