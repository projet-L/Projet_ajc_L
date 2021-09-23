
FROM debian:10
MAINTAINER Your Name "zuuuuper-meh@crash-test.fr"

RUN apt-get update -y
RUN apt-get install python -y
RUN apt-get install -y python3-pip
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

ENV container docker
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive

RUN echo 'deb http://deb.debian.org/debian stretch-backports main' >> /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y --no-install-recommends systemd python3 sudo bash net-tools openssh-server openssh-client vim git\
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config

RUN rm -f /lib/systemd/system/multi-user.target.wants/* \
    /etc/systemd/system/*.wants/* \
    /lib/systemd/system/local-fs.target.wants/* \
    /lib/systemd/system/sockets.target.wants/*udev* \
    /lib/systemd/system/sockets.target.wants/*initctl* \
    /lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup* \
    /lib/systemd/system/systemd-update-utmp*


RUN ln -s /lib/systemd/system /sbin/init
RUN systemctl set-default multi-user.target
#set password to "password"
#RUN sed -i 's#root:\*#root:sa3tHJ3/KuYvI#' /etc/shadow
RUN sed -i 's#root:\*#root:sa3tHJ3/KuYvI#' /etc/shadow
RUN useradd -m -p sa3tHJ3/KuYvI jenkins
USER jenkins
WORKDIR /home/jenkins

RUN mkdir ${HOME}/.ssh && chmod 700 ${HOME}/.ssh && chown $USER:$USER $HOME/.ssh
RUN touch ${HOME}/.ssh/authorized_keys && chmod 600 ${HOME}/.ssh/authorized_keys && chown $USER:$USER ${HOME}/.ssh/authorized_keys
#ADD [--chown=jenkins:jenkins] id_rsa.pub /home/jenkins/.ssh/authorized_keys
#RUN chown $USER:$USER /home/jenkins/.ssh/authorized_keys

USER root
RUN echo 'jenkins   ALL=(ALL) NOPASSWD: ALL'>>/etc/sudoers
ADD [--chown=jenkins:jenkins] id_rsa.pub /home/jenkins/
RUN cat /home/jenkins/id_rsa.pub >> /home/jenkins/.ssh/authorized_keys
RUN passwd -d jenkins
RUN service ssh start


ENV init /lib/systemd/systemd
VOLUME [ "/sys/fs/cgroup" ]

ENTRYPOINT ["/lib/systemd/systemd"]


COPY . .
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["./app.py"]
