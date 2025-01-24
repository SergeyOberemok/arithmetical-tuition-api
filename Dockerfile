FROM node:22 AS ui

WORKDIR /usr/src/app

COPY ./arithmetical-tuition-ui/package*.json ./
COPY ./arithmetical-tuition-ui ./

RUN npm install
RUN npm install rimraf -S

ENV PATH=/usr/src/app/node_modules/.bin:$PATH

RUN npm run build



FROM ubuntu:22.04

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y python3 python3-pip

COPY ./arithmetical-tuition-api/requirements.txt .
RUN pip install -r requirements.txt

COPY ./arithmetical-tuition-api ./
COPY --from=ui /usr/src/app/dist ./dist

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["assessment_flask_app.py"]