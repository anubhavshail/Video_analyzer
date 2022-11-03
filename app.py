from flask import Flask, render_template, Response, request
import math
import random
import os
import time
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/FallDetection', methods=['GET', 'POST'])
def falldetection():
    return render_template('FallDetection.html')

@app.route('/ObjectDetection', methods=['GET', 'POST'])
def objectdetection():
    return render_template('ObjectDetection.html')

@app.route('/CarCrashDetection', methods=['GET', 'POST'])
def carcrashdetection():
    return render_template('CarCrashDetection.html')

@app.route('/SocialDistancingDetection', methods=['GET', 'POST'])
def socialdistancingdetection():
    return render_template('SocialDistancingDetection.html')

@app.route('/video', methods=['GET','POST'])
def video():
    global video_link
    video_link = request.form.get('videolink')
    return render_template('video.html',val=video_link)

if __name__=="__main__":
    app.run(debug=True)



