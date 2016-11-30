# Giant Ball of String: Kiosk

Giant Ball of String (GBoS) is a sample demonstration applicaiton that illustrates how several technologies from Cisco can be brought together to address a business problem.  

## Demo Application Background

All across the United States, there are roadside attractions like *The Worlds Largest Fork*, *The Biggest Donut*, and *The Giant Ball of String*.  The organization that manages these attractions is facing pressure to provide better metrics and details about the visitors to the attractions, and to provide a better experience for those visitors.  If they can't meet this demand, they may see their funding reduced.  

To address this problem, the technical staff has built their next generation attraction support platform.  This platform provides the following capabilities:

* Monitor activity at each site using motion detectors.  
* Turn on lights, signage, and resources at each site only when vistors are present
* Provide centralized logging of visits at all attractions
* Informational Kiosks at each attraction 
* Direct interaction with visitors by providing facts and Q/A through their mobile devices

## Full Demo Details

This repository and README provide details on setting up just the gbos_iox code and deployment.  More details available at: 

* [gbos_demo](https://github.com/imapex/gbos_demo) - Full Demo Application Setup and Details
* [gbos_iox](https://github.com/imapex/gbos_iox) - Details on the Cisco IOx Client Application 
* [gbos_arduino](https://github.com/imapex/gbos_arduino) - Details on the Arduino Microcontroller Code 
* [gbos_kiosk](https://github.com/imapex/gbos_kiosk) - Details on the Welcome Web Portal Page
* [gbos_tropo](https://github.com/imapex/gbos_tropo) - Details on the Tropo Service for SMS based communication with visitors

---


# gbos_kiosk

Kiosk Web Interface for the Giant Ball of String Attraction.  The purpose of this application
is for visitors to enter there phone number so that information about the attraction can
be sent to them via SMS.

[Cisco Tropo](http://tropo.com) is used for the SMS backend.



# Prerequisites

To use this application effectively, you will need the following
* An SMS backend The backend application for this demo can be found at:
    [https://github.com/imapex/gbos_tropo](https://github.com/imapex/gbos_tropo)

    Specifically, you will need the tropo token for this backend application which is provided by the
    installation script from this repo

* A Mantl or marathon stack



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

