__author__ = 'Nick'


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
