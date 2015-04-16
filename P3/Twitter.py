__author__ = 'Miguel Castillo y Diego Farinas'
import twitter
import io
import json

#Funcion para la conexion.
def oauth_login():
    CONSUMER_KEY = '9knChod065lvNpDUvIK36vbsJ'
    CONSUMER_SECRET = 'Q9ZMgtbImUghdIi8kPh9V0tT3vO50zobMQiqYBopv2ixOUmy5v'
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Funcion para grabar la informacion en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Funcion para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()
