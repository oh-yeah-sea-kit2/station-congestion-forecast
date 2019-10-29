FROM centos:7

RUN yum update -y
RUN yum install -y wget git which vim

RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
RUN yum install -y gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel git libffi-devel && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc

RUN source ~/.bashrc
RUN pyenv install anaconda3-5.3.1
RUN pyenv global anaconda3-5.3.1

COPY ./endpoint.sh /root/
# CMD ["/root/endpoint.sh"]
