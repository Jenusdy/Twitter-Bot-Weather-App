import tweepy
from secret import *
import json
import urllib.request
import signal
import asyncio
from time import strftime


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

async def tweet():
    while 1:
        try:
            with urllib.request.urlopen(url_weather) as url:
                response = url.read()
            charset = url.info().get_content_charset('utf-8')
            data=json.loads(response.decode(charset))
            kalimat = "[BOT]"+strftime('[%H:%M:%S]')+" Current weather Jakarta " + str(data['weather'][0]['main']) + " with temperature:" + str(data['main']['temp']) + ", humidity:" + str(data['main']['humidity']) + "%" + ", pressure:" + str(data['main']['pressure']) + "hPa #weather #jakarta"
            print(kalimat)
            api.update_status(kalimat)

            await asyncio.sleep(1 * 60)
        except asyncio.CancelledError:
            break


def shutdown():
    print(strftime('[%H:%M:%S]'), "shutdown")
    for task in asyncio.Task.all_tasks():
        task.cancel()

def main():
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGTERM, shutdown)
    tasks = asyncio.ensure_future(tweet())
    loop.run_until_complete(asyncio.gather(tasks))

if __name__ == "__main__":
    main()
