#!/bin/bash

running_line="/usr/bin/python2.7 manage.py"
if [[ ! -f data/db.sqlite3 ]]; then
    $running_line migrate
    $running_line runserver 0.0.0.0:8080
else
    $running_line runserver 0.0.0.0:8080
fi

