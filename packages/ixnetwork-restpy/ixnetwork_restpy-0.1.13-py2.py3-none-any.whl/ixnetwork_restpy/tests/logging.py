
import sys
import os
sys.path[0] = os.path.abspath(sys.path[0] + '\\..\\..\\')

from ixnetwork_restpy.testplatform.testplatform import TestPlatform

# send trace messages to a log file
# the default is 'none' which is no tracing of request and response messages
test_platform=TestPlatform('127.0.0.1', rest_port=11009, log_file_name='test.log')
session=test_platform.add_Sessions()

# trace requests
# the next add vport should show a debug message for the request
test_platform.Trace='request'
session.Ixnetwork.add_Vport()

# trace requests and responses
# the next add vport should show debug messages for the request and response
test_platform.Trace='request_response'
session.Ixnetwork.add_Vport()

# turn off tracing
# the next add vport should not show debug messages for the request and response
test_platform.Trace='none'
session.Ixnetwork.add_Vport()
