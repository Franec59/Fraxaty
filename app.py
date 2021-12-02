from flask import Flask
from flask.templating import render_template




app = Flask(__name__)


@app.route("/infirmiers")
def infirmiers():
    return render_template("infirmiers.html")

app.run()