import fileinput
from textblob import TextBlob as blob

import speech_recognition as sr
from flask import Flask, render_template, request, flash,redirect
from flask_wtf import FlaskForm
from wtforms import FileField

app = Flask(__name__)
app.secret_key = "Rakshit_app1192"


class MyForm(FlaskForm):
    image = FileField('image')

'''@app.route("/", methods=['POST', 'GET'])
def index():
	transcript = ""
	form = MyForm()
	return render_template("index.html",transcript=transcript)'''


@app.route("/", methods=['POST', 'GET'])
@app.route("/analyze",methods=['POST', 'GET'])
def analyzer():
	transcript=""
	form = MyForm()


	if request.method == 'POST':
		print("data received")

		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files["file"]
		if file.filename == "":
			return redireect(request.url)
		if file:
			r = sr.Recognizer()
			file_audio = sr.AudioFile(file)

			with file_audio as source:
				audio = r.record(source)
			try:
				text = r.recognize_google(audio)
				ck = text

				tb = blob(text)

				test = tb.sentiment
				if (test[0] > 0):
					transcript = 'postive' + str(abs(test[0]))

				else:
					transcript = 'negative' + str(abs(test[0]))

			except:
				print('sorry.. try again')

			return render_template("index.html", transcript=transcript)

	return render_template("audio_file.html", form=form)




if __name__ == '__main__':
	app.run()