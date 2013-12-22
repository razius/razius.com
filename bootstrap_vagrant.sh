#!/bin/bash
sudo apt-get update
sudo apt-get install -y software-properties-common python-dev python-pip ghp-import python-docutils asciidoc
sudo pip install pelican pelican_youtube Markdown fabric typogrify

if [ ! -f "/etc/init/pelican.conf" ];
then
sudo tee /etc/init/pelican.conf << EOF
description "Pelican"
start on filesystem or runlevel [2345]
stop on runlevel [!2345]
respawn
respawn limit 5 60
pre-start script
    chdir /vagrant
    exec make regenerate & >> /vagrant/pelican.log 2>&1
end script
script
    chdir /vagrant
    exec make serve >> /vagrant/pelican.log 2>&1
end script
EOF

sudo service pelican restart
fi

