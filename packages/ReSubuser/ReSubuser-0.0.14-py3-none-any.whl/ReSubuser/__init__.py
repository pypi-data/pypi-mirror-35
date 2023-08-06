import os
from os import environ

name="ReSubuser"

TPL="""                                                                                                                                                          
{"rights":{                                                                                                                                                      
        "daemon":false,                                                                                                                                          
        "display":false,                                                                                                                                         
        "docker":false,                                                                                                                                          
        "home":false,                                                                                                                                            
        "pwd":false,                                                                                                                                             
        "root":false,                                                                                                                                            
        "sound":false,                                                                                                                                           
        "ssh":false                                                                                                                                              
          },                                                                                                                                                     
"cmd":"/bin/sh"}                                                                                                                                                 
"""


## Environ                                                                                                                                                       
base="/home/"+environ['USER']+"/.ReSubuser/"                                                                                                                     
user=environ['USER']                                                                                                                                             
display=environ['DISPLAY']                                                                                                                                       
ssh_auth=environ['SSH_AUTH_SOCK']                                                                                                                                
pwd=environ['PWD']                                                                                                                                               
uid=os.getuid()                                                                                                                                                  
gid=os.getgid()                                                                                                                                                  
verbose=False                                                                                                                                                    
cmd=""                                                                                                                                                           
term=""

