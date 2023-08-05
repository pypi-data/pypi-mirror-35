import sys
import os
sys.path[0] = os.path.abspath(sys.path[0] + '\\..\\..\\')
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.errors import IxNetworkError


# setup the connection information for a windows gui test platform that has a default session of 1
test_platform=TestPlatform('127.0.0.1', rest_port=11009, platform='windows')

# get a list of sessions
for session in test_platform.Sessions():
	print(session)

# add a session and remove the session
session = test_platform.add_Sessions()
print(session)
session.remove()

# get an invalid session
try:
	session = test_platform.Sessions(Id=6)
except IxNetworkError as e:
	print(e)

# get a valid session
session = test_platform.Sessions(Id=1)
print(session)