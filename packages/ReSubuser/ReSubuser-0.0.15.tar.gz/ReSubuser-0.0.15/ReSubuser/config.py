import os
import json

import ReSubuser
base=ReSubuser.base

def check():
    """Check folders Verification """
    if (not os.path.isdir(base)):
        os.mkdir(base)
    if (not os.path.isdir(base+"/homes")):
        os.mkdir(base+"/homes") 
    return 0

def default_option(app):
    """Write default option from TPL """
    print("create "+app+" option")                                                                                                                               
    default_json=json.loads(ReSubuser.TPL)
    json.dump(default_json, open(base+"/"+app+"/option","w"),indent=4)                                                                                           
    return 0

def edit(app):
    """Open Editor to write option/dockerfile"""

    if (not os.path.isdir(base+app)):
        os.mkdir(base+app)

    os.chdir(base+app)                                                                                                                                           

    if (not os.path.isfile("option")):
        default_option(app)

    os.system("$EDITOR option Dockerfile")                                                                                                                       
    return 
