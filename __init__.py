from flask import Flask
from flask import render_template

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'SeCrEtKeY'
toolbar = DebugToolbarExtension(app)
app.config["DEBUG"] = True

def debug_state(debug):
    try:
        if debug == True:
            DEBUG = True
        else:
            DEBUG = False
    except Exception as e:
        DEBUG = False

app.config.from_object(debug_state(True))
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
