from flask import Flask, render_template, request, url_for
from chart import h2
import os
from time import sleep

IMG_FOLDER = os.path.join('static', 'img_folder')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wykres', methods = ['POST', 'GET'])
def wykres():
    if request.method == 'POST':
        time = request.form['time']
    else:
        time = request.args.get('time')

    if time == None:
        return render_template('index.html')
    t = int(time)
    h2(t)
    print('zapisano do pliku')
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'test.png')
    return render_template("wykres.html", img_url=file_name)





if __name__ == "__main__":
    app.run(debug=True)

