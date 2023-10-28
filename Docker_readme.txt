# To build a new docker image

$ docker build -t yourname/colorbot:latest .

# To run in a container

Make a local dir to store your .env and database files

$ mkdir /opt/colorbot
$ cp .env /opt/colorbot/

Run the container:

$ docker run -d --restart unless-stopped --name colorbot -v /opt/colorbot:/root/colorbot -e DATA_DIR=/root/colorbot yourname/colorbot:latest
