from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hellp():
    return 'Welcome to GCP 101 by Pudit Tempattarachoke, AI & Robotics Engineer'

@app.route('/OZT')
def gcp():
	# https://console.cloud.google.com/
    return redirect("https://www.oztrobotics.com/", code=302)

if __name__ == '__main__':
    
     app.run(host='0.0.0.0',port ='5000')

