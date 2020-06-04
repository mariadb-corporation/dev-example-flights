import flask
from airlines import airlines
from airports import airports
from flights import flights

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(airlines)
app.register_blueprint(airports)
app.register_blueprint(flights)

@app.route("/api/version")
def version():
    return "1.0"

app.run(port=8080)