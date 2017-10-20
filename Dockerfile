FROM ubuntu

MAINTAINER Anton <jnt2007@ya.ru>

USER root

RUN apt-get update -y && apt-get install -y \
    vim \
    python2.7 \
    python-dev \
    python-pip \
    sqlite3

RUN /usr/bin/pip install django

ENV site_dir /etc/version_site
RUN mkdir -p $site_dir
ADD src/dashboard/ $site_dir/dashboard
ADD src/static/ $site_dir/static
ADD src/templates/ $site_dir/templates
ADD src/version_site/ $site_dir/version_site
ADD src/main.sh $site_dir
ADD src/manage.py $site_dir

WORKDIR /etc/version_site
ENTRYPOINT ["/bin/bash", "main.sh"]