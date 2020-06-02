# api.sso.ameyrupji.com

A SSO website backend for my platform deployed as a serverless REST API.


## Prerequisites

- Python >= 3.6

## Run Application

### Create Virtual Environment for Application

Run the following command to create a new Python Virtual Environment for running this application:

```shell script
python3 -m venv venv
```

***Note:* Creation of Virtual Environment needs to be only done once when this repository is downloaded.


### Activate Virtual Environment

Run the following command to activate the created Virtual Environment:

```shell script
source venv/bin/activate
```

**Note:** This needs to run each time the application needs to be run in a terminal

### Install pip dependencies

Run the following command to run to install dependencies of this application into the Virtual Environment:

```shell script
pip3 install -r requirements.txt
```

### Add additional pip dependencies

Run the following commands to add a new pip dependencies to this application. The command below show the example of installing `flask` package.

```shell script
pip3 install flask
echo 'flask' >> requirements.txt
pip3 install -r requirements.txt
pip3 freeze > requirements.txt
```

### Running Application

Run the application by running the following commands:
```shell script
export FLASK_APP=src/api/run.py
flask run
```

## Cleanup


Stop the application by running `Command (⌘) + c` 
 
Run the following commands to exit from the activated Virtual Environment:

```shell script
deactivate
```

## Install Application

To install application with the configured environments run the following command:

```shell script
zappa deploy beta
```

This will deploy the application exposing a api gateway.

## Delete Application

To uninstall the application run the following command:

```shell script
zappa undeploy beta
```

## Useful Links

**Dependant repositories:**

- Branching Strategy: https://github.com/ameyrupji-com/ameyrupji.com-branching-strategy
- Infrastructure as Code: https://github.com/ameyrupji-com/ameyrupji.com-iac
- Frontend: https://github.com/ameyrupji-com/sso.ameyrupji.com
- Developer Portal: https://github.com/ameyrupji-com/developer.sso.ameyrupji.com

**References:**

- https://hackernoon.com/deploy-a-serverless-flask-application-on-aws-lambda-d8ca58af42a4