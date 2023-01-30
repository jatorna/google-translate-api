FROM nikolaik/python-nodejs:python3.10-nodejs18
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app
WORKDIR /usr/src/app/scripts/javascript
RUN npm i google-translate-extended-api
WORKDIR /usr/src/app
