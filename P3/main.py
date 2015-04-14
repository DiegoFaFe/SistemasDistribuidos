from flask import Flask, render_template
from flask import request
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

import Twitter
import json

app = Flask(__name__)
GoogleMaps(app)

@app.route("/buscar", methods=['POST'])
def mapview():

	twitter = Twitter.oauth_login()

	formtext = request.form['text']

	tweets = twitter.search.tweets(q=formtext, count=1000, geocode='40.2085,-3.713,497mi');

	Twitter.save_json('tweets', tweets);

	fileload = Twitter.load_json('tweets');

	search = json.loads(fileload);

	results = []

	for i in search['statuses']:
		if i['geo']:
			xy=	(i['geo']['coordinates'][0], i['geo']['coordinates'][1])
			results.append(xy)

	print(results)

	mymap = Map(identifier="view-side", lat=40.45, lng=3.75, markers=results, style="height:700px;width:700px;margin:0 auto;", zoom=4)

	return render_template('mapa.html', mymap=mymap)

@app.route("/")
def indexview():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
