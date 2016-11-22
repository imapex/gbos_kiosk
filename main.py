import logging
import os
from flask import Flask, render_template, request, flash, redirect
from forms import Register
import requests
import os

# Flask initialization
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Logging configuration
logger = logging.getLogger('KIOSK')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def prepare_data(number):
    token = os.getenv("TROPO_TOKEN")
    url = "https://api.tropo.com/1.0/sessions?action=create&token={}&numberToDial={}".format(token, number)
    resp = requests.get(url)
    print "Tropo Response: {}".format(resp.status_code)
    return resp.text


@app.route('/', methods=['GET', 'POST'])
def kiosk():
    if request.method == 'GET':
        form = Register()
        title = "Giant Ball of String"
        return render_template('base.html',
                               title=title,
                               form=form)

    if request.method == 'POST':
        # We are receiving data from the user (phone number)
        form = Register(request.form)
        phonenumber = form.phonenumber.data
        if form.validate():
            logger.info('Received registration for number {}'.format(phonenumber))
            prepare_data(phonenumber)
            return redirect('/')
        else:
            logger.error("Did not receive valid form")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=os.getenv("DEBUG", False))
