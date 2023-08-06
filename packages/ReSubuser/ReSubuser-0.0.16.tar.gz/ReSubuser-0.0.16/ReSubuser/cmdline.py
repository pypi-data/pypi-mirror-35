import sys
import os
import ReSubuser
import json
import getopt

base=ReSubuser.base

from ReSubuser import dockerwrap
from ReSubuser import config


term=""
cmd=""



def usage():
    """Help message"""
    print("""
ReSub.py [option] [name]
-h      :help
-v      :verbose
-t      :force terminal
-l      :List images
--check :Check containers
--clean :Clean unneeded containers
-b name :Build subContainer
-e name :Edit Files
-c cmd  :Command override
name    :Name of the container
""")

    print("### Available containers") 
    dockerwrap.listimg()
    exit(0)



def parsearg():
    try:
        optlist,args = getopt.getopt(sys.argv[1:],'hlb:n:ve:c:t',{'check','clean'})
    except :
        usage()
        exit(0)

    for o,a in optlist:
        if o == "-b":
            dockerwrap.build(a)
            exit(0)
        if o == "-v":
            ReSubuser.verbose=True
        if o == "-e":
            config.edit(a)
            exit(0)
        if o=="-h":
            usage()
            exit(0)
        if o=="-c":
            ReSubuser.cmd=a
        if o=="-t":
            ReSubuser.term="-it"
        if o=="-l":
            dockerwrap.listimg()
            exit(0)
        if o=="--check":
            dockerwrap.container()
            exit(0)
        if o=="--clean":
            dockerwrap.clean()
            exit(0)

    try:
        app=args[0]
        ReSubuser.app=app
    except:
        print("Need an argument")
        exit()


def cmdline():
    term=ReSubuser.term
    cmd=ReSubuser.cmd
    uid=ReSubuser.uid
    gid=ReSubuser.gid
    user=ReSubuser.user
    base=ReSubuser.base
    verbose=ReSubuser.verbose
    display=ReSubuser.display
    ssh_auth=ReSubuser.ssh_auth
    pwd=ReSubuser.pwd
    app=ReSubuser.app

    if (not os.path.isdir(base+app)):
        os.mkdir(base+app)
    try:
        data=json.load(open(base+"/"+app+'/option'))
    except:
        print("Error no option %s/%s "%(base,app))
        exit()

    cmdline=""
    
    try:
        if ('display' in data['rights']):
            if (data['rights']['display']):
                cmdline="-e DISPLAY={} ".format(display)
                cmdline=cmdline+"-v /tmp/.X11-unix:/tmp/.X11-unix "
    
        if ('home' in data['rights']):
            if (data['rights']['home']):
                path="{}/homes/{}".format(base,app)
                cmdline=cmdline+"-e HOME=/home/{} ".format(user)
                cmdline=cmdline+"-e USER={} ".format(user)
                cmdline=cmdline+"-e LOGNAME={} ".format(user)
                cmdline=cmdline+"-v {}/homes/{}:/home/{} ".format(base,app,user)
                if (not os.path.isdir(path)):
                    os.mkdir(path)
    
        if ('ssh' in data['rights']):
            if (data['rights']['ssh']):
                cmdline=cmdline+"-e SSH_AUTH_SOCK=/ssh-agent "
                cmdline=cmdline+"-v {}:/ssh-agent ".format(ssh_auth)
    
        if ('pwd' in data['rights']):
            if (data['rights']['pwd']):
                cmdline=cmdline+"-v {}:/local ".format(pwd)
                cmdline=cmdline+"-w /local "
    
        if ('sound' in data['rights']):
            if (data['rights']['sound']):
                cmdline=cmdline+"-v /run/user/{}/pulse:/run/pulse ".format(uid)
                cmdline=cmdline+"-v /dev/shm:/dev/shm "
                cmdline=cmdline+"-v /etc/machine-id:/etc/machine-id "
                cmdline=cmdline+"-e PULSE_SERVER=unix:/run/pulse/native "
    
        if ('daemon' in data['rights'] and term==""):
            if (data['rights']['daemon']):
                term="-d"
            else:
                term="-it"
        else:
            term="-it"
    
        if ('docker' in data['rights']):
            if (data['rights']['docker']):
                cmdline=cmdline+"-v /var/run/docker.sock:/var/run/docker.sock "
    
    ### the Dangerous ONE ###
        if ('root' in data['rights']):
            if (data['rights']['root']):
                uid=0
    
    except e:
        print("Need Options %s"%(sys.argv[0]))
        exit()
    

    line={}
    line.update({'uid':uid})
    if (cmd==""):
        line.update({'cmd':data['cmd']})
    else:
        line.update({'cmd':cmd})
    
    line.update({'cmdline':cmdline})
    line.update({'app':app})
    line.update({'term':term})
    ## don't know how to run  session
    cmdline="docker run {term} --rm -u {uid}:{uid} {cmdline} sub_{app} {cmd}".format(**line)
    if (verbose):
        print(cmdline)

    return cmdline

#    a=os.system(cmdline)
#    if (a!=0):
#        print("try to %s -b %s "%(sys.argv[0],app))
#        if (os.path.isfile(base+app+"/Dockerfile")):
#        build(app)
