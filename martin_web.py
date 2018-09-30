#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect #Blueprint
import coinflips
import urllib, base64
#import time

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = "/martin-web"

plot_data=""
prefix="/martin-web"


@app.route(prefix+'/')
def mainpage():

	global plot_data

	
	return render_template("martin.html", plot_url=plot_data)

@app.route(prefix+'/play', methods = ['POST'])
def play():

	if request.method == "POST":

		global plot_data

		startingChips=int(request.form['startingChips'])
		rounds=int(request.form['rounds'])
		games=int(request.form['games'])

		img=coinflips.martingale_play(startingChips, rounds, games)
		img.seek(0)
		plot_data = urllib.quote(base64.b64encode(img.read()).decode())

		return redirect(prefix+'/')



if __name__ == '__main__':
	
	app.run(host='0.0.0.0', debug = True)
