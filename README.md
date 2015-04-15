# DCIIM
Data center Infrastructures Information Management (DCIIM) is a simple handy application to handle and manage datadcenter's information.
my default deployment for this app is to manage openstack user and infra. information for the openstack deployment so it may exist a lot of openstack phrases and names there.


Deployment Requirements
-----------
* django 1.6
* mysql-server

DevOps Tools
------------
* django 1.6
* git
* south

Deployment instruction on Debian Jessie
------------
* apt-get install pip
* pip install django=1.6
* git clone https://github.com/mrafieee/DCIIM.git
* cd DCIIM
* python manage.py syncdb
* python manage.py runserver 8000

Enjoy it in your Firefox http://localhost:8000
