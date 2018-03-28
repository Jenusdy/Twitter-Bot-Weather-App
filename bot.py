import tweepy
from secret import *
import MySQLdb
import signal
import asyncio
from time import strftime


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

db = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                     passwd="",
                     db="statistik_kita")

async def tweet():
    while 1:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM informasi_statistik")
            for row in cursor.fetchall():
                api.update_status("[BOT]" + strftime('[%H:%M:%S]')+ " " + row[1] + " | #statistikkita")
                print("This is works")
                try:
                    await asyncio.sleep(1 * 60)
                except asyncio.CancelledError:
                    break
            break
        finally:
            cursor.close()


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
