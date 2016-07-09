import time
import os

from PIL import Image
from celery import Celery

app = Celery(__name__,
            broker = 'redis://127.0.0.1:6379/0',
            backend = 'redis://127.0.0.1:6379/0')


@app.task
def add(a,b):
    time.sleep(3)
    return a+b


@app.task
def sum2(values):
    print('-'*40)
    print(values)
    time.sleep(3)   #3초 동안 잠듦(그정도로 복잡한일을 수행한다고 가정)
    return sum(values)

@app.task
def make_thumbnail(path,width,height):
    if not os.path.isfile(path):     #디렉토리도 포함될수 있기때문에 exists는 사용안함
        return

    filepath, ext = os.splittext(path)
    output = '{}_thumb{}'.format(filepath,ext)

    im = Image.open(path)
    im.tumbnail([width, height, ], Image.ANTIALIAS)
    im.save(output)
    im.close()

    return output
