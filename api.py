# # Api endpoint is like a location of api and it is in the form of
# # api[webistename].com
# # Api request ... you cant just got get the information witout a proper request
# # import the requtes package
import requests
from datetime import *
from smtplib import *
import time
# # 404 response code not working
# # 100 and something hold on
# # 200 code successful
# # 300 forbidden no permission
# # 400 You screwed up lol
# # 500 server down
# # we use the raise_for_status() handles the error
my_gmail = 'racooltest88@gmail.com'
my_gmail_password = 'nljezkzcqivldaaf'
receiving_address = 'ridwan.rede02@gmail.com'
# api has parameter not all though
parameters = {
    'apiKey': '73a6d5500fc84c14aaf01df5b0150c52',
    'lat': 47.5615,
    'long': -52.7126
}


while True:
    time.sleep(60)
    report = requests.get('http://api.open-notify.org/iss-now.json')
    report.raise_for_status()
    data = report.json()
    iss_longitude = float(data.get('iss_position')['longitude'])
    iss_latitude = float(data.get('iss_position')['latitude'])
    request_for_sun = requests.get('https://api.ipgeolocation.io/astronomy?', params=parameters)
    request_for_sun.raise_for_status()
    sun_data = request_for_sun.json()
    sunset = sun_data['sunset']
    sunrise = sun_data['sunrise']
    current_time = datetime.now()
    sunset_hour = int(sunset.split(':')[0])
    sunrise_hour = int(sunrise.split(':')[0])
    current_time_hour = current_time.hour
    print(f'long:{iss_longitude},lat:{iss_latitude}')
    if ((current_time_hour >= sunset_hour) or (current_time_hour <= sunrise_hour)) and (
            ((parameters['long'] - 5) <= iss_longitude <= (parameters['long'] + 5))) and (
            ((parameters['lat'] - 5) <= iss_latitude <= (parameters['lat'] + 5))):
        with SMTP('smtp.gmail.com') as send:
            send.starttls()
            send.login(user=my_gmail, password=my_gmail_password)
            send.sendmail(from_addr=my_gmail, to_addrs=receiving_address,
                          msg="Subject : Look Up Do'nt miss the space_station !!!\n\nISS Remainder!!!")

