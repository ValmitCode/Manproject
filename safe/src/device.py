import random
import os
import time
from Adafruit_CCS811 import Adafruit_CCS811
import platform
import geocoder
import math
import sqlite3

conn = sqlite3.connect("device_report.db") 
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS devices(
   deviceid INT PRIMARY KEY,
   devicepass TEXT,
   voc INT,
   co2 INT,
   temp INT,
   geo INT);
""")
conn.commit()

rad = 6372795

g = geocoder.ip('me')
print (g.address)
print (g.latlng)

llat1 = g.latlng[0]
llong1 = g.latlng[1]
llat2 =  -33.8678500
llong2 = 151.2073200

def dist(lt1,ln1,lt2,ln2):
    lat1 = llat1*math.pi/180.
    lat2 = llat2*math.pi/180.
    long1 = llong1*math.pi/180.
    long2 = llong2*math.pi/180.

    #косинусы и синусы широт и разницы долгот
    cl1 = math.cos(lat1)
    cl2 = math.cos(lat2)
    sl1 = math.sin(lat1)
    sl2 = math.sin(lat2)
    delta = long2 - long1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)

    #вычисления длины большого круга
    y = math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2))
    x = sl1*sl2+cl1*cl2*cdelta
    ad = math.atan2(y,x)
    dist = ad*rad/1000
    print ('Distance >> %.0f' % dist, ' [meters]')
    print(dist)
dist (llat1,llong1,llat2,llong2)

VOC = 0
eCO2 = 0
temp = 0
data_file = r"/home/pi/Desktop/MAPB_data.txt"
send_every = 60

# print hostname
print(platform.node())


def main():
    global eCO2,VOC,temp, geo
    ccs = Adafruit_CCS811(address=0x5b)

    time_begin = time.time()

    while True:
        try:
            # opros datchika
            if ccs.available():
                temp = ccs.calculateTemperature()
                if not ccs.readData():
                    eCO2 = ccs.geteCO2()
                    VOC = ccs.getTVOC()
                # s="rad:"+str(random.random())
                s = str(eCO2)+"|"+str(VOC)+"|"+str("%.2f" % temp)+str(llat1)+str(llong2)
                print(s)
                f = open(data_file, 'a')
                f.write(s+"\n")
                f.close()
            time_now = time.time()
            if time_now-time_begin >= send_every:
                if os.system("scp -P 2211 "+data_file+" valmit@178.151.227.197:data/") == 0:
                    # os.system("scp -P 2211 /home/pi/Desktop/comand valmit@178.151.227.197:data/")
                    with open(data_file, 'w'):
                        pass
                    time_begin = time.time()
        except Exception as e:
            print('ERROR ON SEND DATA: '+str(e))
        time.sleep(10)



if __name__ == "__main__":
    main()
