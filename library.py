__author__ = 'Nick'
import os
import sys


def isPingable(site):
    import subprocess
    import shlex

    command_line = "ping -c 1 " + site
    args = shlex.split(command_line)
    try:
      subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
      return 1
    except subprocess.CalledProcessError:
      return 0

def singleton(parentFile):
    scriptPath = os.path.dirname(parentFile)


    fileName = os.path.basename(parentFile)
    fileNameBase = os.path.splitext(fileName)[0]
    pidFile=scriptPath+"/"+fileNameBase+'.pid'
    print pidFile
    if os.path.isfile(pidFile):
        f=open(pidFile,'r')
        pid=int(f.readline())
        f.close()
        if check_pid(pid):
            print 'process is already running; exiting'
            exit()
        else:
            print 'pid '+str(pid)+ ' is NOT running'
            write_pid(pidFile,str(os.getpid()))
    else:
        write_pid(pidFile,str(os.getpid()))


def write_pid(pidFile,pid):
    f=open(pidFile,'w')
    print "Writing pid to .pid file "+pidFile+' '+str(pid)
    f.write(str(pid))
    f.close()

def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True
