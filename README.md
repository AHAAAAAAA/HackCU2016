# HackCU2016
Semantic analysis + Tweets + Jazz + balance + information

# Quick setup:
  $ pip install -U django
  Use the following commands but change jazz (at end of first command and other places) to the name of your project:
  $ django-admin.py startproject --template=https://github.com/arocks/edge/archive/master.zip --extension=py,md,html,env jazz
  $ cd jazz
  $ pip install -r requirements.txt 
  $ cd src
  $ cp jazz/settings/local.sample.env jazz/settings/local.env
  $ python manage.py migrate
  $ python manage.py createsuperuser
  $ pip install -r requirements.txt

