FROM ubuntu
RUN apt-get update && apt-get -y install build-essential debhelper automake libtool git devscripts

VOLUME /package

COPY bin/package-deb.sh /bin/package-deb
RUN chmod 755 /bin/package-deb

CMD ["package-deb", "--version=0.2.4", "--dest=/package", "--src=/eventlog", "--release=UNRELEASED", "https://github.com/balabit/eventlog"]
