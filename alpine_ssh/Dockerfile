FROM alpine:latest
MAINTAINER lei fireflykind@gmail.com

USER root

RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.3/main/" > /etc/apk/repositories && \
    mkdir /root/.ssh && \
    apk --update add bash openssh && \
    rm -rf /var/cache/apk/* /tmp/* /root/src/ && \
    ssh-keygen -A 

COPY authorized_keys /root/.ssh/authorized_keys
COPY sshd_config /etc/ssh/sshd_config

RUN chmod 600 /root/.ssh/authorized_keys
    

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]