#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
import coinflips
import urllib, base64
#import time

app = Flask(__name__)

@app.route('/')
def mainpage():


	
	return render_template("martin.html", plot_url=plot_data)

@app.route('/play', methods = ['POST'])
def play():

	if request.method == "POST":

		global plot_data

		startingChips=int(request.form['startingChips'])
		rounds=int(request.form['rounds'])
		games=int(request.form['games'])

		img=coinflips.martingale_play(startingChips, rounds, games)
		img.seek(0)
		plot_data = urllib.quote(base64.b64encode(img.read()).decode())

		print(plot_data)

		#time.sleep(5)

		return redirect('/')

if __name__ == '__main__':
	plot_data=""
	app.run(host='0.0.0.0', debug = True)
