from wtforms import Form
from wtforms.fields.html5 import TelField


class Register(Form):
    phonenumber = TelField()
