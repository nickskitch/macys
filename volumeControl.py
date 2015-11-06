import subprocess
import time
volume=0

cmd ='osascript -e "Set volume '+str(volume)+'"'
subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
