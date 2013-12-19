FROM ubuntu:12.10
MAINTAINER Silviu Tantos "me@razius.com"
# Changing the line bellow will invalidate the image cache and trigger a refresh.
ENV UPDATED 2013-12-19

RUN apt-get update
RUN apt-get install -y software-properties-common python-pip
RUN pip install pelican Markdown

# CMD /etc/init.d/php5-fpm start && /usr/sbin/nginx -c /etc/nginx/nginx.conf -g "daemon off;"

# EXPOSE 8080:80
