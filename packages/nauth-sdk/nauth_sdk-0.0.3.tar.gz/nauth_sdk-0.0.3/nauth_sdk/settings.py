import os
cwd = os.getcwd()
import sys
sys.path.insert(0, cwd)
eval('import nauth_settings as n')
nid = eval('n.nid')
nauth_host_location = eval('n.nauth_host_location')
nkey = eval('n.nkey')
sitename = eval('n.sitename')