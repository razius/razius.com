FROM ubuntu:12.10
MAINTAINER Silviu Tantos "me@razius.com"
# Changing the line bellow will invalidate the image cache and trigger a refresh.
ENV UPDATED 2013-12-19
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /mnt/

RUN apt-get update
RUN apt-get install -y software-properties-common python-dev python-pip asciidoc
RUN pip install pelican Markdown fabric typogrify
RUN make regenerate &

CMD make serve

EXPOSE 8000:8000
