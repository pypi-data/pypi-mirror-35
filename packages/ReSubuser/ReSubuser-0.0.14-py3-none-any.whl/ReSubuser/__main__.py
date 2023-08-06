from ReSubuser import dockerwrap
from ReSubuser import config
from ReSubuser import cmdline
import os

def cli():
    config.check()
    a=cmdline.parsearg()
    cmd=cmdline.cmdline()
    os.system(cmd)


if __name__=="__main__":
    print("[ ReSubuser ]")
    cli()
