import tweepy

'''
Función utilizada para utilizar la Api de Twitter
'''
def get_auth():
    consumer_key = 'tbQLjeaiBvj2H6JVPB7y8k9qe'
    consumer_secret = 'wHU0l1l0LGIuXO0pjHEQ0a42Yamqcs8PZdZfQwV9UgpOSFvtv4'
    access_token = '1248394473039695872-GHpOEaARr4oqhUv4ucmPFqfiJEsVFA'
    access_token_secret = 'ZMTKukgwR3jogbIfIN3Co6jlbli19eO0WqcUieSWlkyXN'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth