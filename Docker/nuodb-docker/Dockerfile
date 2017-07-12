FROM java:openjdk-8-jre

ENV nuodb_package nuodb-ce_2.6.1.5_amd64.deb
RUN /usr/bin/apt-get update
RUN /usr/bin/apt-get -y install default-jre-headless supervisor wget

RUN wget --output-document=/tmp/$nuodb_package https://studuniroma3-my.sharepoint.com/personal/gae_bonofiglio_stud_uniroma3_it/_layouts/15/guestaccess.aspx?docid=06716ef81e5cd464bbd53abc76251d5ad&authkey=AdqDLfjtheRH33nNCKuMrpY

RUN chmod 755 /tmp/$nuodb_package
RUN /usr/bin/dpkg -i /tmp/$nuodb_package

RUN /bin/sed -ie 's/#domainPassword =/domainPassword = foo/' /opt/nuodb/etc/default.properties
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN chmod 755 /etc/supervisor/conf.d/supervisord.conf
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
