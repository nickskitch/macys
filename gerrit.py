__author__ = 'Nick'
import subprocess
departData=[]

def gerrit():
    cmd2 = "curl --digest http://wdsgerrit:8080/a/path/to/api/"
    print cmd2
    departData.append(subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip())

    print "\n".join(departData)