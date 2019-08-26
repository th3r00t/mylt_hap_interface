from flask import Flask
from flask import render_template
from flask_mqtt import Mqtt
import random
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# app.debug = True
app.config['SECRET_KEY'] = 'SeCrEtKeY'
# toolbar = DebugToolbarExtension(app)
# app.config["DEBUG"] = True
app.config["MQTT_CLIENT_ID"] = "mylt?controler?%s"%(random.randint(0000, 9999))
app.config["MQTT_BROKER_URL"] = '10.0.0.2'
app.config["MQTT_BROKER_PORT"] = 1883
app.config["MQTT_TLS_ENABLED"] = False
app.config["MQTT_KEEPALIVE"] = 5
# app.config["MQTT_TLS_ENABLED"] = False
mqtt = Mqtt(app)
# mqtt.init_app(app)
@mqtt.on_log()
def logging(client, userdata, level, buf):
    if level == MQTT_LOG_ERR:
        print('Error: {}'.format(buf))
    elif level == MQTT_LOG_NOTICE:
        print('Notice: {}'.format(buf))
    elif level == MQTT_LOG_WARNING:
        print('Warning: {}'.format(buf))
    elif level == MQTT_LOG_INFO:
        print('Info: {}'.format(buf))
    elif level == MQTT_LOG_DEBUG:
        print('Debug: {}'.format(buf))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/controller", methods=['GET', 'POST'])
def controller():
    if (not mqtt.connected):
        mqtt._connect()
    mqtt.publish('lighting/benchlight', '0')
    return ('', 505)

if __name__ == "__main__":
    app.run(debug=False)
