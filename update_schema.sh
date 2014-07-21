#!/bin/bash -x
./manage.py schemamigration userdb --auto
./manage.py migrate userdb

