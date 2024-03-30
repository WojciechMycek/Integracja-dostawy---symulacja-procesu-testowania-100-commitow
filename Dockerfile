FROM jenkins/jenkins

USER root

RUN apt-get update && \
    apt-get -y install apt-transport-https \
                       ca-certificates \
                       curl \
                       gnupg-agent \
                       software-properties-common

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

RUN apt-get update && \
    apt-get -y install docker-ce docker-ce-cli containerd.io

USER jenkins
