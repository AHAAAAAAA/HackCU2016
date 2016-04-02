# HackCU2016
Semantic analysis + Tweets + Jazz + balance + information

# Quick setup:
Install Django:

  $ pip install -U django
  
Use the following commands:
  
  `django-admin.py startproject --template=https://github.com/arocks/edge/archive/master.zip --extension=py,md,html,env jazz`
  
  `cd jazz`
  
  `pip install -r requirements.txt `
  
  `cd src`
  
  `cp jazz/settings/local.sample.env jazz/settings/local.env`
  
  `python manage.py migrate`
  
  `python manage.py createsuperuser`
  
  `pip install -r requirements.txt`

# Usage

`python manage.py runserver`
