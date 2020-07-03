from flask import Flask, render_template

# from flask_debugtoolbar import DebugToolbarExtension
from data import tours as data_tours
from data import departures as data_departures
from data import title as data_title
from data import subtitle as data_subtitle
from data import description as data_description

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "xv3gavkxc04n3mzx7oksd6q"


@app.route("/")
def render_index():
    log_data_tours = {}
    amount = 1

    for d_tours_key, d_tour_value in data_tours.items():
        if amount <= 6:
            log_data_tours[d_tours_key] = d_tour_value
            amount += 1
        else:
            break

    return render_template(
        "index.html",
        title=data_title,
        subtitle=data_subtitle,
        description=data_description,
        departures=data_departures,
        tours=log_data_tours,
    )


@app.route("/departures/<id_departure>/")
def render_departures(id_departure):
    new_departure = {}
    cost_tours = []
    amount_nights = []

    for d_tour_key, d_tour_value in data_tours.items():
        if d_tour_value.get("departure") == id_departure:
            new_departure[d_tour_key] = d_tour_value
            cost_tours.append(d_tour_value.get("price"))
            amount_nights.append(d_tour_value.get("nights"))

    return render_template(
        "departure.html",
        title=data_title,
        data_tours=new_departure,
        departures=data_departures,
        cost_tours=cost_tours,
        amount_nights=amount_nights,
    )


@app.route("/tours/<int:id_tour>")
def render_tours(id_tour):
    return render_template(
        "tour.html",
        data_tours=data_tours.get(id_tour),
        title=data_title,
        departures=data_departures,
    )


@app.errorhandler(404)
def render_not_found(error):
    return render_template("404.html", err=error)


# toolbar = DebugToolbarExtension(app)
app.run("127.0.0.1", 8000)
