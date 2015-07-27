__author__ = 'mohammad'

from django.shortcuts import render_to_response
from django.template import RequestContext
import json
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
    return render_to_response('generate-list-files.html', {'files': files}, context_instance=RequestContext(request))

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
    return render_to_response('generate-extract.html', {'message': message}, context_instance=RequestContext(request))

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
    return render_to_response('generate-import.html', {'files':sql_files, 'message': message}, context_instance=RequestContext(request))

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def list_projects(request):
    title = "Projects"
    message = "projects successfully listed"
    query = "SELECT * FROM project;"
    projects = {}

    c = connections['keystone'].cursor()
    try:
        c.execute(query)
        projects = dictfetchall(c)

    finally:
        c.close()
    return render_to_response('reports-projects.html', {'projects':projects, 'message': message, 'title': title}, context_instance=RequestContext(request))


def list_routers(request):
    title = "Routers"
    message = "Routers successfully listed"
    query = "SELECT keystonedb.project.name as project_name,keystonedb.project.id as project_id,neutrondb.`networks`.`name` as network_name,`routers`.name as router_name,neutrondb.`ports`.`mac_address` as port_mac_address,neutrondb.`ipallocations`.`ip_address` "\
            "FROM keystonedb.project inner join neutrondb.`networks` on neutrondb.`networks`.`tenant_id`=keystonedb.project.id " \
            "inner join neutrondb.`routers` on neutrondb.`routers`.`tenant_id`=keystonedb.project.id "\
            "inner join neutrondb.`ports` on neutrondb.`routers`.`id`=neutrondb.`ports`.`device_id` "\
            "inner join neutrondb.`ipallocations` on neutrondb.`ports`.`id`=neutrondb.`ipallocations`.`port_id` and neutrondb.`networks`.`id`= neutrondb.`ipallocations`.`network_id` "\
            "order by keystonedb.project.name "
    query2 = "SELECT keystonedb.project.name as project_name,keystonedb.project.id as project_id,neutrondb.`networks`.`name` as network_name,`routers`.name as router_name,neutrondb.`ports`.`mac_address` as port_mac_address,neutrondb.`ipallocations`.`ip_address` FROM keystonedb.project inner join neutrondb.`networks` on neutrondb.`networks`.`tenant_id`=keystonedb.project.id inner join neutrondb.`routers` on neutrondb.`routers`.`tenant_id`=keystonedb.project.id inner join neutrondb.`ports` on neutrondb.`routers`.`id`=neutrondb.`ports`.`device_id` inner join neutrondb.`ipallocations` on neutrondb.`ports`.`id`=neutrondb.`ipallocations`.`port_id` "
    routers = {}
    try:
        con = mdb.connect('localhost', 'root', 'root', '')
        cur = con.cursor()
        cur.execute(query)
        routers = dictfetchall(cur)
    finally:
        con.close()
    return render_to_response('reports-routers.html', {'routers':routers, 'message': message, 'title': title}, context_instance=RequestContext(request))


def list_subnets(request):
    title = "Subnets"
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
    return render_to_response('reports-subnets.html', {'subnets':subnets, 'message': message, 'title': title}, context_instance=RequestContext(request))

def list_floating_ip(request):
    title = "Floating IPs for instances and routers"
    message = "Floating IPs successfully listed"
    query = "SELECT keystonedb.project.name as project_name,keystonedb.project.id as project_id,neutrondb.`floatingips`.`floating_ip_address`,"\
            "neutrondb.`floatingips`.`fixed_ip_address`, neutrondb.`floatingips`.`status` FROM keystonedb.project "\
            "inner join neutrondb.`floatingips` on neutrondb.`floatingips`.`tenant_id`=keystonedb.project.id "\
            "ORDER BY project_name"
    f_ip = {}
    try:
        con = mdb.connect('localhost', 'root', 'root', '')
        cur = con.cursor()
        cur.execute(query)
        f_ip = dictfetchall(cur)

    finally:
        con.close()
    return render_to_response('reports-floating.html', {'list':f_ip, 'message': message, 'title': title}, context_instance=RequestContext(request))

def list_demo_vpc(request):
    title = "Demo VPCs"
    message = "Demo VPCs successfully listed"

    query = "drop view if exists toke_extra_view;" \
            "create view toke_extra_view as SELECT `extra` FROM `token` WHERE `extra` like '%VPC_XAAS_demo%';" \
            "drop view if exists vpc_main_fields_view;" \
            "create view vpc_main_fields_view as SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(extra, ',', 2), ',', -1),'issued_at\":',-1) as create_date,SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(extra, ',', 54), ',', -1),'\"email\": \"',-1) as email_address,SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(extra, ',', 60), ',', -1),'\"name\": \"',-1) as tenant_name,SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(extra, ',', 53), ',', -1),'\"tenantId\": ',-1) as tenant_id FROM `toke_extra_view`;" \
            "drop view if exists final_vpc_main_files_view;" \
            "create view final_vpc_main_files_view as select trim(replace(replace(`tenant_id`,'\"',''),'}','')) as tenantId,trim(replace(replace(`tenant_name`,'\"',''),'}','')) as tenantName, trim(replace(replace(SUBSTRING_INDEX(`create_date`, '.', 1),'\"',''),'T',' ')) as CreateDate, trim(replace(replace(`email_address`,'\"',''),'}','')) as emailAddress from `vpc_main_fields_view`;" \
            "delete from final_vpc_main_files_view where `tenantId` like '%id%';"

    query2 = "select grouped_results.*,TIMEDIFF(grouped_results.terminate_date,grouped_results.create_date) as tenant_lifetime from " \
            "(SELECT `tenantId`, `tenantName`,`emailAddress`, min(`CreateDate`) as create_date, max(`CreateDate`) as terminate_date FROM `final_vpc_main_files_view` "\
            "group by `tenantId`) as grouped_results " \
            "order by create_date;"
    list = {}
    try:
        con = mdb.connect('localhost', 'root', 'root', 'keystonedb')
        cur = con.cursor()
        con.query(query)
    finally:
        con.close()

    try:
        con2 = mdb.connect('localhost', 'root', 'root', 'keystonedb')
        cur = con2.cursor()
        cur.execute(query2)
        list = dictfetchall(cur)

    finally:
        con2.close()
    return render_to_response('reports-vpc.html', {'list':list, 'message': message, 'title': title}, context_instance=RequestContext(request))

def list_instances(request):
    title = "Instances"
    message = "Instances successfully listed"
    query1 = "ALTER TABLE novadb.`instances` CHANGE `image_ref` `image_ref` VARCHAR(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;"
    query2 = "ALTER TABLE novadb.`instances` CHANGE `project_id` `project_id` VARCHAR(64) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL;"
    query = "SELECT `novadb`.`instances`.`id`,`novadb`.`instances`.`hostname`,`novadb`.`instances`.`created_at`,`keystonedb`.`project`.`name` as project_name,`glancedb`.`images`.`name` as image_name,`novadb`.`instances`.`root_gb` as disk_gb," \
            "`novadb`.`instances`.`memory_mb`,`novadb`.`instances`.`vcpus`,`novadb`.`instances`.`host`,`novadb`.`instances`.`vm_state`,`novadb`.`instances`.`availability_zone`,`novadb`.instance_info_caches.`network_info` " \
            "FROM `novadb`.`instances` " \
            "inner join `glancedb`.`images` on `glancedb`.`images`.`id`=`novadb`.`instances`.`image_ref` " \
            "inner join `keystonedb`.`project` on `keystonedb`.`project`.`id`=`novadb`.`instances`.`project_id` " \
            "inner join `novadb`.instance_info_caches on `novadb`.instance_info_caches.`instance_uuid`= `novadb`.`instances`.`uuid`" \
            "and `novadb`.`instances`.deleted_at is null"
    list = {}

    try:
        con = mdb.connect('localhost', 'root', 'root', '')
        con.query(query1)
        con.query(query2)
        cur = con.cursor()
        cur.execute(query)
        list = dictfetchall(cur)
    finally:
        con.close()

    for item in list:
        str = item.get("network_info")
        j = json.loads(str)
        item['network_info'] = "IP:<b>" + j[0]['network']['subnets'][0]['ips'][0]['address'] + "</b><br />"
        if j[0]['network']['subnets'][0]['ips'][0]['floating_ips']:
            item['network_info'] = item['network_info'] + "Floating:<b>" + j[0]['network']['subnets'][0]['ips'][0]['floating_ips'][0]["address"] + "</b><br />"
        item['network_info'] = item['network_info'] + "Mac:<b>" + j[0]['address'] + "</b>"
    return render_to_response('reports-instances.html', {'list':list, 'message': message, 'title': title}, context_instance=RequestContext(request))