# Giant Ball of String - Kiosk

Kiosk Web Interface for the Giant Ball of String Attraction.  The purpose of this application
is for visitors to enter there phone number so that information about the attraction can
be sent to them via SMS.

[Cisco Tropo](http://tropo.com) is used for the SMS backend.

The backend application for this demo can be found at:

[https://github.com/imapex/gbos_tropo](https://github.com/imapex/gbos_tropo)

# Installation

This application can be installed locally on your server, or by using Docker (preferred).
In either mode the following environment variables must be present

* SECRET_KEY - Flask application secret
* TROPO_TOKEN - token for the SMS backend application

## Docker installation

The latest version of this application is available on Docker hub. Start it by using
the following command:
```
 docker run -it \
-e SECRET_KEY=dontshare \
-e TROPO_TOKEN=<your TROPO app token> \
-p 5000:5000 imapex/gbos_kiosk`
```
## Local Installation

* Clone this repo
```
git clone https://github.com/imapex/gbos_kiosk
```
* Create Virtual Environment and install dependencies
```
cd gbos_kiosk
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

```

* Start the service

```
python main.py
```

## Marathon Deployment

Alternatively, installation scripts are provided for deploying to a Marathon infrastructure

```
bash marathon_install.sh

```

