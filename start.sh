#!/bin/bash
app="lostark.engraving"
sudo docker rm -f ${app}
sudo docker rmi -f ${app}
docker build -t plc402/${app} .
docker run -d -p 80:80 \
  --name=${app} \
  -v $PWD:/app \
  -v $PWD/app/static:/var/www/app/static plc402/${app}
