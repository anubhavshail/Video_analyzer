from flask import Flask, render_template, response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('intex.html')

@app.route('/FallDetection', methods=['GET', 'POST'])
def falldetection():
    return render_template('FallDetection.html')

@app.route('/ObjectDetection', methods=['GET', 'POST'])
def objectdection():
    return render_template('ObjectDetection.html')

@app.route('/CarCrashDetection', methods=['GET', 'POST'])
def carcrashdetection():
    return render_template('CarCrashDetection.html')

@app.route('/SocialDistancingDetection', methods=['GET', 'POST'])
def carcrashdetection():
    return render_template('SocialDistancingDetection.html')

if __name__=="__main__":
    app.run(debug=True)



