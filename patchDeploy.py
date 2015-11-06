__author__ = 'Nick'
import subprocess
import time
import os.path

server=''
MacysNavAppWebVersion=''
MacysShopNServeVersion=''

def log():
    f = open('/tmp/patchlog.txt','a')
    f.write('run at: ' + time.strftime("%I:%M:%S")+'\n')
    f.close()

def copyFile(src, dest):
    if os.path.isfile(src):
        cmd = "cp "+src+" "+dest
        print cmd
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()

def setServer():
    cmd = "hostname"
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
    if "nvapp" in output:
        return 'navapp'
        print server+" detected"
    if "esu2v240" in output:
        return 'legacy'
        print server+" detected"

def getNavAppNodeRoots():
    if server == 'navapp':
        global MacysNavAppRoot
        navAppBase = "/usr/WebSphere70/AppServer/profiles/storemacys_mngd/installedApps/storemacys/macys-navapp_cluster1.ear/"
        cmd = 'ls ' +navAppBase + '| egrep -o "([0-9]{1,}\.)+[0-9]{1,}"'
        MacysNavAppWebVersion = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
        MacysNavAppRoot=navAppBase+"MacysNavAppWeb-"+MacysNavAppWebVersion+".war/"

        print "the root of macysNavappweb is " + MacysNavAppRoot

        global ShopNServeRoot
        SNSbase = "/usr/WebSphere70/AppServer/profiles/storemacys_mngd/installedApps/storemacys/macys-shopapp_cluster1.ear/"
        cmd = 'ls '+SNSbase+' | egrep -o "([0-9]{1,}\.)+[0-9]{1,}"'
        MacysShopNServeVersion = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
        ShopNServeRoot = SNSbase + "MacysShopNServe.war-"+MacysShopNServeVersion+".war/"
        print "the root of ShopNServe is " + ShopNServeRoot

server=setServer()
log()

# | egrep -o "([0-9]{1,}\.)+[0-9]{1,}"

if server == 'legacy':
    print 'copying legacy files'
    legacyRoot="/usr/WebSphere70/AppServer/profiles/storemacys_mngd/installedApps/storemacys/"
    copyFile("/tmp/header.jsp", legacyRoot+"macys-store_cluster1.ear/macys.war/web20/global/header/header.jsp")
    copyFile("/tmp/responsive_header.jsp", legacyRoot+"macys-cache_cluster1.ear/macys.war/web20/global/header/responsive_header.jsp")
    copyFile("/tmp/responsive_header.jsp", legacyRoot+"macys-store_cluster1.ear/macys.war/web20/global/header/responsive_header.jsp")
    copyFile("/tmp/responsive_footer.jsp", legacyRoot+"macys-cache_cluster1.ear/macys.war/web20/global/footer/responsive_footer.jsp")
    copyFile("/tmp/responsive_footer.jsp", legacyRoot+"macys-store_cluster1.ear/macys.war/web20/global/footer/responsive_footer.jsp")

if server == 'navapp':
    print 'copying navapp files'
    getNavAppNodeRoots()
    copyFile("/tmp/faceted_navbar.jsp", MacysNavAppRoot+"web20/catalog/browse/faceted_navbar.jsp")
    copyFile("/tmp/header.jsp", MacysNavAppRoot+"web20/global/header/header.jsp")
    copyFile("/tmp/responsive_header.jsp", ShopNServeRoot+"/web20/global/header/responsive_header.jsp")
    copyFile("/tmp/responsive_header.jsp", MacysNavAppRoot+"web20/global/header/responsive_header.jsp")
    copyFile("/tmp/responsive_footer.jsp", ShopNServeRoot+"web20/global/footer/responsive_footer.jsp")
    copyFile("/tmp/responsive_footer.jsp", MacysNavAppRoot+"web20/global/footer/responsive_footer.jsp")
    copyFile("/tmp/responsive_base_script.jsp", ShopNServeRoot+"web20/global/tiles/responsive_base_script.jsp")
    copyFile("/tmp/responsive_base_script.jsp", MacysNavAppRoot+"web20/global/tiles/responsive_base_script.jsp")
