Twitter bot Weather App
=========================
### Deskripsi
Twitter bot Weather App ini adalah sebuah program abal-abalan yang dibuat dengan tidak ada tujuan tertentu.

### Tools
1. Python 3 (Usahakan 3.5 keatas)

### Dependency
```{bash}
$ pip install tweepy
$ pip install Pillow
```

### Instalasi
1. Buat akun [twitter](https://www.twitter.com) jika belum punya
2. Buat daftarkan aplikasi yang ingin dibuat di [apps.twitter.com](https://apps.twitter.com/)
3. Generate secret_key, consumer_key, access_token, access_secret dari aplikasi yang didaftarkan. Nggak tahu caranya? Tanya mbah google.
4. Buat akun dan api key untuk mengambil data dari [openweathermap.org](http://openweathermap.org/) menggunakan API
5. Isikan secret_key, consumer_key, consumer_secret, access_token, access_secret ke file secret.py
6. Jalankan programnya

```{python}
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_token'
access_secret = 'your_access_secret'
api_key_weather = 'your_api_key_weather'

url_weather = 'http://api.openweathermap.org/data/2.5/weather?q=Jakarta&appid=' + api_key_weather
```
```{bash}
$ python bot.py
```


### Credit
* Fawcet Jenusdy Makay
* Mbah google
