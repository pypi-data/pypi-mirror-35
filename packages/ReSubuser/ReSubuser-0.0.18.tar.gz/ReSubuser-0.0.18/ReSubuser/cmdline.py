import sys
import os
import json
import getopt

import ReSubuser
from ReSubuser import dockerwrap,config

class cmdline():
    """
    class with all requierement to launch docker with parameters
    """


    def __init__(self):
        self.env=ReSubuser.env
        self.conf=config.config(self.env)
        self.conf.check()
        self.parsearg()


    def usage(self):
        """Help message with all switches"""
        print("""
##############################################
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
        internal_docker=dockerwrap.dockerwrap(self.env)
        internal_docker.listimg()
        return 0

    def parsearg(self):
        """Parse arguments """
        try:
            optlist,args = getopt.getopt(sys.argv[1:],'hlb:n:ve:c:t',{'check','clean'})
        except :
            usage()
            exit(0)

        internal_docker=dockerwrap.dockerwrap(self.env)

        for o,a in optlist:
            if o == "-b":
                internal_docker.build(a)
                exit(0)
            if o == "-v":
                self.env.verbose=True
            if o == "-e":
                self.conf.edit(a)
                exit(0)
            if o=="-h":
                self.usage()
                exit(0)
            if o=="-c":
                self.env.cmd=a
            if o=="-t":
                self.env.term="-it"
            if o=="-l":
                internal_docker.listimg()
                exit(0)
            if o=="--check":
                internal_docker.container()
                exit(0)
            if o=="--clean":
                internal_docker.clean()
                exit(0)

        try:
            app=args[0]
            self.env.app=app
            self.env.internal=False
        except:
            print("Need an argument")
            return 1


    def command(self):
        """Generate final command"""
        if (not os.path.isdir(self.env.base+self.env.app)):
            os.mkdir(self.env.base+self.env.app)
        try:
            data=json.load(open(self.env.base+"/"+self.env.app+'/option'))
        except:
            print("Error no option %s/%s "%(self.env.base,self.env.app))
            exit()

        cmdline=""
        cmd=""

        try:
            if ('display' in data['rights']):
                if (data['rights']['display']):
                    cmdline="-e DISPLAY={} ".format(self.env.display)
                    cmdline=cmdline+"-v /tmp/.X11-unix:/tmp/.X11-unix "

            if ('home' in data['rights']):
                if (data['rights']['home']):
                    path="{}/homes/{}".format(self.env.base,self.env.app)
                    cmdline=cmdline+"-e HOME=/home/{} ".format(self.env.user)
                    cmdline=cmdline+"-e USER={} ".format(self.env.user)
                    cmdline=cmdline+"-e LOGNAME={} ".format(self.env.user)
                    cmdline=cmdline+"-v {}/homes/{}:/home/{} ".format(self.env.base,self.env.app,self.env.user)
                    if (not os.path.isdir(path)):
                        os.mkdir(path)

            if ('ssh' in data['rights']):
                if (data['rights']['ssh']):
                    cmdline=cmdline+"-e SSH_AUTH_SOCK=/ssh-agent "
                    cmdline=cmdline+"-v {}:/ssh-agent ".format(self.env.ssh_auth)

            if ('pwd' in data['rights']):
                if (data['rights']['pwd']):
                    cmdline=cmdline+"-v {}:/local ".format(self.env.pwd)
                    cmdline=cmdline+"-w /local "

            if ('sound' in data['rights']):
                if (data['rights']['sound']):
                    cmdline=cmdline+"-v /run/user/{}/pulse:/run/pulse ".format(self.env.uid)
                    cmdline=cmdline+"-v /dev/shm:/dev/shm "
                    cmdline=cmdline+"-v /etc/machine-id:/etc/machine-id "
                    cmdline=cmdline+"-e PULSE_SERVER=unix:/run/pulse/native "

            if ('daemon' in data['rights'] and self.env.term==""):
                if (data['rights']['daemon']):
                    self.env.term="-d"
                else:
                    self.env.term="-it"
            else:
                self.env.term="-it"

            if ('docker' in data['rights']):
                if (data['rights']['docker']):
                    cmdline=cmdline+"-v /var/run/docker.sock:/var/run/docker.sock "

            if ('root' in data['rights']):
                if (data['rights']['root']):
                    self.env.uid=0

        except e:
            print("Need Param %s"%(sys.argv[0]))


        line={}
        line.update({'uid':self.env.uid})

        if (self.env.cmd==""):
            line.update({'cmd':data['cmd']})
        else:
            line.update({'cmd':self.env.cmd})

        line.update({'cmdline':cmdline})
        line.update({'app':self.env.app})
        line.update({'term':self.env.term})
        ## don't know how to run  session
        cmdline="docker run {term} --rm -u {uid}:{uid} {cmdline} sub_{app} {cmd}".format(**line)
        if (self.env.verbose):
            print(cmdline)

        return cmdline
