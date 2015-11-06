    #!/bin/sh

## Initialize the cookie-jar
curl --cookie-jar cjar --output /dev/null https://www.okcupid.com/login

export USERNAME='onestrangegravy@gmail.com'
export PASSWORD='nNpxvj9M'

## Login and save the resulting HTML file as loginResult.html (for debugging purposes)
curl --cookie cjar --cookie-jar cjar \
  --data 'dest=/?' \
  --data 'username=$USERNAME' \
  --data 'password=$PASSWORD' \
  --location \
  --output loginResult.html \
    https://www.okcupid.com/login

## Download the inbox and save it as inbox.html
curl --cookie cjar \
  --output inbox.html \
  http://www.okcupid.com/messages