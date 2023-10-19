# IMAGEM = sysdistr/back:1.0

FROM node

WORKDIR /usr/src/back

# Úteis em intranet iterconteineres
#EXPOSE 5432  postgres
#EXPOSE 27017 mongodb
#EXPOSE 8080  http

COPY . .

RUN cat package.json
RUN npm install
CMD node ./src/build/index.js
