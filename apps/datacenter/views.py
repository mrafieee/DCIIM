__author__ = 'mohammad'
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import *
from datetime import datetime
import os, tarfile, sys, shutil,subprocess
from dciim.settings import BASE_DIR
from django.db import connections


def list_backup_files(request):
    path = BASE_DIR+"/media/uploads/"
    files = os.listdir(path)
    return render_to_response('list-files.html', {'files': files}, context_instance=RequestContext(request))

def extract(request, file):
    print file
    tar_address = BASE_DIR+"/media/uploads/"+file
    print tar_address
    extract_path = BASE_DIR+"/media/uploads/tmp/"
    tar = tarfile.open(tar_address, 'r:bz2')

    for item in tar:
        tar.extract(item, extract_path)
        if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1 or item.name.find(".tar.bz2") != -1:
            if item.name == "tmp":
                extract(item.name, "./" + item.name[:item.name.rfind('/')])
    try:
        extract(sys.argv[1] + '.tgz')
        print 'Done.'
    except:
        name = os.path.basename(sys.argv[0])
        print name[:name.rfind('.')], '<filename>'

    message = file +" has successfully extracted"
    return render_to_response('extract.html', {'message': message}, context_instance=RequestContext(request))

def import_databases(request):
    path = BASE_DIR+"/media/uploads/tmp/tmp/"
    sql_files = os.listdir(path)

    for item in sql_files:
        print item
        dbname = item.split("_",1)[0]
        item = path + item
        print dbname
        if dbname == "mysql":
            continue
        proc = subprocess.Popen(["mysql",
                                 "--user=%s" % 'root',
                                 "--password=%s" % 'root',
                                 dbname],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        out, err = proc.communicate(file(item).read())

    message = "Databases has successfully imported and temp directory removed"
    shutil.rmtree(BASE_DIR+"/media/uploads/tmp/")
    return render_to_response('import.html', {'files':sql_files, 'message': message}, context_instance=RequestContext(request))

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def list_projects(request):
    message = "projects list"
    query = "SELECT * FROM project;"

    projects = {}
    with connections['keystone'].cursor() as c:
        c.execute(query)
        projects = dictfetchall(c)

    return render_to_response('projects.html', {'projects':projects, 'message': message}, context_instance=RequestContext(request))