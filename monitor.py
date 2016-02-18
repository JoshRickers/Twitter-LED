from twython import Twython, TwythonError
import serial, time, re

ser = serial.Serial('COM3', 9600, timeout=2)

regex = re.compile('(#[a-f0-9]{6}|#[a-f0-9]{3})', re.IGNORECASE)

api_key = ""
api_secret = ""
access_token = ""
access_secret = ""
tweetID = 0

twitter = Twython(api_key, api_secret, access_token, access_secret)

while True:
    try:
        search_results = twitter.search(q = 'to:joshuarickers', count = 1, since_id = tweetID)
    except TwythonError as e:
        print(e)

    print('Tweet: ', search_results['statuses'][0]['text']) 

    if re.search(regex, search_results['statuses'][0]['text']):
        colour = re.search(regex, search_results['statuses'][0]['text']).group()
        print('Colour :', colour)
        print(ser.readline())
        ser.write(bytes(colour, 'ascii'))

    time.sleep(60)
