__author__ = 'Miguel Castillo y Diego Fariñas'
import twitter
import io
import json

#Función para la conexión.
def oauth_login():
    CONSUMER_KEY = 'V1k5HWU0z62uFCZnagy9RQ'
    CONSUMER_SECRET = 'gVw8steIbXtnq65sHVCL1kRvlARaC1a6dne2KrMY'
    OAUTH_TOKEN = '218857687-vWSbnv9WE3Wy1cyPeFJSXhZZVcwIpeNIRSWyasss'
    OAUTH_TOKEN_SECRET = 'I8QGeSElKpwr3J0aydFVA3CxBn6MknFjTt2J5VCiGY'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Función para grabar la información en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(str(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()