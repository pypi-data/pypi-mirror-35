# ReSub

From an original idea from  [subuser](http://subuser.org/) to
run an application into a docker container like a local application.

## Quick Start
* Copy sample from (https://framagit.org/who0/ReSubuser/tree/master/sample) to  ~/.ReSubuser
* Build container: ```./ReSub.py -b vim ```
* Run container: ```./ReSub.py vim```

## Build your own
* ./ReSub.py -b name
* Edit container + adapt option files.
* Build until success
* Run ./ReSub.py -v name

### --options
* -h      :help
* -v      :verbose
* -t      :force terminal
* -l      :List images
* -b name :Build subContainer
* -e name :Edit Files
* -c cmd  :Command override
* name    :Name of the container


### Rights
/!\ **security warning**

Docker can run applications as root inside container (but, external files (ie outside container) will be as root. Don't use root if you don't know what your are doing. (see example)

### name/options
- [ ] "daemon" instead of terminal
- [ ] "display" share /tmp/.X11 to display graphical interface
- [ ] "docker" for host docker api
- [ ] "home" private home for this application
- [ ] "pwd" access to the current pwd << don't be root
- [ ] "root" launch docker as root (instead of current user)
- [ ] "sound" access to pulse audio
- [ ] "ssh" share ssh-agent

### name/Dockerfile
* you need to understand [dockerfile syntax](https://docs.docker.com/engine/reference/builder/)


## ByPass Root with Docker power
```docker run -v /etc:/hack -it debian cat /hack/shadow```

## Well Known
> sound only works with pulse
