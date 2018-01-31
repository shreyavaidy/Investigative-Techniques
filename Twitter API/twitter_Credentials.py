consumer_key = '47ziJwnyZOtGB7lOzWZDCJtFr'
consumer_secret = 'Paq9R7U5OHKN4Ysgp8EH9aRnQQO9UZG3CJe7e4izyms4YueaIt'

key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')

#Encode to ASCII because you cant send bytes through the API call