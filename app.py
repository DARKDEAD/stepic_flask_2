from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'xv3gavkxc04n3mzx7oksd6q'


@app.route('/')
def render_index():
    return render_template('index.html', title='Главная страница Stepik Travel')


@app.route('/departures/<departure>/')
def render_departures(departure):
    return render_template('departure.html')


@app.route('/tours/<id_tour>')
def render_tours(id_tour):
    return render_template('tour.html')


@app.errorhandler(404)
def render_not_found(error):
    return render_template('404.html')


toolbar = DebugToolbarExtension(app)
app.run('127.0.0.1', 8000)
