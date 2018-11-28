import Adafruit_DHT as dht
import time as t

while True:
    umid,temp = dht.read_retry(dht.DHT11, 4)
    print ('Temp {0:0.1f}     Umid: {1:0.1f}'.format(temp,umid))
    t.sleep(1)