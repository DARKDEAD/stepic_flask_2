from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from data import tours as data_tours
from data import departures as data_departures
from data import tours as data_title
from data import tours as data_subtitle
from data import tours as data_description


app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "xv3gavkxc04n3mzx7oksd6q"


@app.route("/")
def render_index():
    return render_template("index.html", title=data_title, subtitle=data_subtitle, description=data_description)


@app.route("/departures/<departure>/")
def render_departures(departure):
    return render_template("departure.html", title=data_title, data_tours=data_tours,
                           departure=data_departures[departure])


@app.route("/tours/<int:id_tour>")
def render_tours(id_tour):
    return render_template(
        "tour.html", data_tours=data_tours.get(id_tour), title=data_title, departures=data_departures)


@app.errorhandler(404)
def render_not_found(error):
    return render_template("404.html", err=error)


toolbar = DebugToolbarExtension(app)
app.run("127.0.0.1", 8000)
