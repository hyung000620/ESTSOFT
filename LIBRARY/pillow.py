from PIL import Image, ImageFilter
import os
import random
from datetime import datetime

now = datetime.now()
f_time = now.strftime("%Y%m%d")

rd_num = random.randint(1000, 9999)

current_dir = os.path.dirname(os.path.abspath(__file__))

img = Image.open(current_dir +'/foo.jpg', mode = 'r')
img.show()
print(img.size)

croped_img = img.crop((10, 10, 200, 200))
croped_img.save(current_dir + f'croped_test.jpg')

blur_test = img.filter(ImageFilter.BLUR) # 이미지를 흐리게 필터링 BLUR
blur_test.save(current_dir + f'blur_test.jpg')

contour_test = img.filter(ImageFilter.CONTOUR) #이미지윤곽
contour_test.save(current_dir + f'contour_test.jpg')

detail_test = img.filter(ImageFilter.DETAIL)
detail_test.save(current_dir + f'detail_test.jpg')

emboss_test = img.filter(ImageFilter.EMBOSS)
emboss_test.save(current_dir + f'emboss_test.jpg')

smooth_test = img.filter(ImageFilter.SMOOTH)
smooth_test.save(current_dir + f'smooth_test.jpg')

smooth_more_test = img.filter(ImageFilter.SMOOTH_MORE)
smooth_more_test.save(current_dir + f'smooth_more_test.jpg')

find_edges_test = img.filter(ImageFilter.FIND_EDGES)
find_edges_test.save(current_dir + f'find_edges_test.jpg')

