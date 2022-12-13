# importando modulos da api climatica
from requests import get
import json
from pprint import pprint
# importando modulos da camera
from picamera import PiCamera
from time import sleep

# api climatica:
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'
stations_json = get(weather).text
stations_dict = json.loads(stations_json)['items'][0]

pprint(stations_dict)
print(type(stations_dict))

# camera
camera = PiCamera()
camera.resolution = (1024, 768)

camera.start_preview()
sleep(2)
camera.capture('sel0337.jpg')
camera.stop_preview()

camera.start_preview()
camera.annotate_text = "10748434 e 10788697"
sleep(5)
camera.capture('/home/sel/SEL0337/flavio_pimenta/pimenta_crush.jpg')
camera.stop_preview()

camera.start_preview()
camera.annotate_text = "Vai BRASIL"
camera.start_recording('/home/sel/SEL0337/flavio_pimenta/hexa.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
