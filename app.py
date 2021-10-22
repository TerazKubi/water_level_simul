from flask import Flask, render_template, request, url_for
from chart import simulate
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
        height = request.form['height']
        kp = request.form['kp']
        ti = request.form['ti']
        td = request.form['td']
        a = request.form['a']
        qdmax = request.form['qdmax']
        umax = request.form['umax']
    else:
        time = request.args.get('time')
        height = request.args.get('height')
        kp = request.args.get['kp']
        ti = request.args.get['ti']
        td = request.args.get['td']
        a = request.args.get['a']
        qdmax = request.args.get['qdmax']
        umax = request.args.get['umax']

    if time == None:
        return render_template('index.html')

    t = int(time)
    if t <= 0:
        return render_template('index.html')

    # height = to wysokosc rzadana podana przez urzytkownik
    simulate(t, height, kp, ti, td, a, qdmax, umax)
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'test.png')
    return render_template("wykres.html", img_url=file_name)





if __name__ == "__main__":
    app.run(debug=True)

