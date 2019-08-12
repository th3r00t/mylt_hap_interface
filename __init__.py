from flask import Flask
app = Flask(__name__)
flask_config = app.config.from_object('config')
flask_config["DEBUG"] = True
@app.route("/")
def hello():
    return "Hello, Flask"
if __name__ == "__main__":
    app.run()
