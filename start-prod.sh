#!/bin/bash
app="lostark.engraving"
docker build -t ${app} -f Dockerfile-prod .
docker run -d -p 6663:80 \
  --restart unless-stopped \
  --name=${app} \
  -v $PWD:/app \
  -v $PWD/app/static:/var/www/app/static plc402/${app}
