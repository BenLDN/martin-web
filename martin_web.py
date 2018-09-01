#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, response
import coinflips

app = Flask(__name__)

@app.route('/')
def mainpage():
	response.cache_control.max_age = 1
	return render_template("martin.html")

@app.route('/play', methods = ['POST'])
def play():

	if request.method == "POST":

		startingChips=int(request.form['startingChips'])
		rounds=int(request.form['rounds'])
		games=int(request.form['games'])

		coinflips.martingale_play(startingChips, rounds, games)


	return redirect('/')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)
