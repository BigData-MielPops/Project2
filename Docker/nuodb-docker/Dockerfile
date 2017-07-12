FROM java:openjdk-8-jre

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y wget
RUN apt-get -y install default-jre-headless supervisor

RUN wget -r -O /tmp/nuodb-ce_2.6.1.5_amd64.deb http://www.gaetanobonofiglio.com/public/nuodb-ce_2.6.1.5_amd64.deb
RUN ls /tmp

RUN chmod 755 /tmp/nuodb-ce_2.6.1.5_amd64.deb
RUN /usr/bin/dpkg -i /tmp/nuodb-ce_2.6.1.5_amd64.deb

RUN /bin/sed -ie 's/#domainPassword =/domainPassword = foo/' /opt/nuodb/etc/default.properties
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN chmod 755 /etc/supervisor/conf.d/supervisord.conf
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
