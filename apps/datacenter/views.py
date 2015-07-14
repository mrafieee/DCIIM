__author__ = 'mohammad'
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import *
from datetime import datetime
import os, tarfile, sys, shutil,subprocess
import MySQLdb as mdb
from dciim.settings import BASE_DIR
from django.db import connections


def reports(request):
    return render_to_response('reports.html', context_instance=RequestContext(request))

def list_backup_files(request):
    path = BASE_DIR+"/media/uploads/"
    files = os.listdir(path)
    files.sort()
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
    query = "ALTER TABLE keystonedb.`project` CHANGE `id` `id` VARCHAR(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;"
    try:
        con = mdb.connect('localhost', 'root', 'root', '')
        cur = con.cursor()
        cur.execute(query)
    finally:
        con.close()

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
    title = "Projects List"
    message = "projects successfully listed"
    query = "SELECT * FROM project;"
    projects = {}

    c = connections['keystone'].cursor()
    try:
        c.execute(query)
        projects = dictfetchall(c)

    finally:
        c.close()
    return render_to_response('projects.html', {'projects':projects, 'message': message, 'title': title}, context_instance=RequestContext(request))


def list_routers(request):
    title = "Routers details List"
    message = "Routers successfully listed"
    query = "SELECT keystonedb.project.name as project_name,keystonedb.project.id as project_id,neutrondb.`networks`.`name` as network_name,`routers`.name as router_name,neutrondb.`ports`.`mac_address` as port_mac_address,neutrondb.`ipallocations`.`ip_address` FROM keystonedb.project inner join neutrondb.`networks` on neutrondb.`networks`.`tenant_id`=keystonedb.project.id inner join neutrondb.`routers` on neutrondb.`routers`.`tenant_id`=keystonedb.project.id inner join neutrondb.`ports` on neutrondb.`routers`.`id`=neutrondb.`ports`.`device_id` inner join neutrondb.`ipallocations` on neutrondb.`ports`.`id`=neutrondb.`ipallocations`.`port_id` "
    routers = {}
    try:
        con = mdb.connect('localhost', 'root', 'root', '')
        cur = con.cursor()
        cur.execute(query)
        routers = dictfetchall(cur)
    finally:
        con.close()
    return render_to_response('routers.html', {'routers':routers, 'message': message, 'title': title}, context_instance=RequestContext(request))


def list_subnets(request):
    title = "Subnets details List"
    message = "subnets successfully listed"
    query = "SELECT keystonedb.project.name as project_name,keystonedb.project.id as project_id,neutrondb.`networks`.`name` as network_name,"\
        "`routers`.name as router_name,"\
        "neutrondb.`subnets`.`name` as subnet_name,neutrondb.`subnets`.`Cidr`,"\
        "neutrondb.`subnets`.`gateway_ip`,"\
        "neutrondb.`ipallocationpools`.first_ip as pool_address_start,"\
        "neutrondb.`ipallocationpools`.last_ip as pool_address_end,"\
        "neutrondb.`ipavailabilityranges`.first_ip as first_available_ip,"\
        "neutrondb.`ipavailabilityranges`.last_ip as last_available_ip " \
        "FROM keystonedb.project "\
        "inner join neutrondb.`networks` on neutrondb.`networks`.`tenant_id`=keystonedb.project.id "\
        "inner join neutrondb.`routers` on neutrondb.`routers`.`tenant_id`=keystonedb.project.id "\
        "inner join neutrondb.`subnets` on neutrondb.`subnets`.`network_id`=neutrondb.`networks`.`id` "\
        "inner join neutrondb.`ipallocationpools` on neutrondb.`ipallocationpools`.`subnet_id`=`neutrondb`.`subnets`.id "\
        "inner join neutrondb.`ipavailabilityranges` on neutrondb.`ipavailabilityranges`.`allocation_pool_id`=`neutrondb`.`ipallocationpools`.id ORDER BY neutrondb.`subnets`.`Cidr`"\

    subnets = {}
    try:
        con = mdb.connect('localhost', 'root', 'root', '')
        cur = con.cursor()
        cur.execute(query)
        subnets = dictfetchall(cur)

    finally:
        con.close()
    return render_to_response('subnets.html', {'subnets':subnets, 'message': message, 'title': title}, context_instance=RequestContext(request))

def list_floating_ip(request):
    title = "Floating IPs details List"
    message = "Floating IPs successfully listed"
    query = "SELECT keystonedb.project.name as project_name,keystonedb.project.id as project_id,neutrondb.`floatingips`.`floating_ip_address`,"\
            "neutrondb.`floatingips`.`fixed_ip_address`, neutrondb.`floatingips`.`status` FROM keystonedb.project "\
            "inner join neutrondb.`floatingips` on neutrondb.`floatingips`.`tenant_id`=keystonedb.project.id "\
            "order by neutrondb.`floatingips`.`floating_ip_address`"
    f_ip = {}
    try:
        con = mdb.connect('localhost', 'root', 'root', '')
        cur = con.cursor()
        cur.execute(query)
        f_ip = dictfetchall(cur)

    finally:
        con.close()
    return render_to_response('floating.html', {'list':f_ip, 'message': message, 'title': title}, context_instance=RequestContext(request))
