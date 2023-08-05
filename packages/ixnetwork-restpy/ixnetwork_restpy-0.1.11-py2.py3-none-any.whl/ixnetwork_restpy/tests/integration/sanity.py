
import sys
import os
sys.path[0] = os.path.abspath(sys.path[0] + '\\..\\..\\..\\')

from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.errors import IxNetworkError
from ixnetwork_restpy.files import Files

session = None

try:
	#test_platform = TestPlatform('10.36.79.20')
	test_platform = TestPlatform('127.0.0.1', rest_port=11009)
	test_platform.Trace = 'request'
	test_platform.Authenticate('admin', 'admin')
	print(test_platform)

	# get a list of sessions
	for session in test_platform.Sessions():
		print(session)
	# add a session and remove the session
	session = test_platform.add_Sessions()
	print(session)
	session.remove()
	try:
		# get an invalid session
		session = test_platform.Sessions(Id=6)
	except IxNetworkError as e:
		print(e)
	# get a valid session
	session = test_platform.Sessions(Id=1)
	print(session)

	ixnetwork = session.Ixnetwork
	print(ixnetwork)

	views = ixnetwork.Statistics.View()
	print(views)

	try:
		ixnetwork.LoadConfig('c:/temp/ipv4_traffic.ixncfg')
		assert ('Type checking failed')
	except TypeError as e:
		print(e)
	ixnetwork.LoadConfig(Files('c:/users/anbalogh/downloads/ipv4_traffic.ixncfg', local_file=True))

	print(ixnetwork.Globals)
	print(ixnetwork.AvailableHardware)
	print(ixnetwork.Traffic)
	print(ixnetwork.Statistics)
	print(ixnetwork.ResourceManager)

	ixnetwork.NewConfig()
	
	assert(len(ixnetwork.Vport()) == 0)
	assert(len(ixnetwork.Topology()) == 0)
	assert(len(ixnetwork.AvailableHardware.Chassis()) == 0)
	assert(len(ixnetwork.Statistics.View()) == 0)
	assert(len(ixnetwork.Traffic.TrafficItem()) == 0)

	vport_name = 'Abstract Port 1'
	vport = ixnetwork.add_Vport(Name=vport_name, Type='pos')
	assert (vport.Type == 'pos')
	assert (vport.Name == vport_name)
	vport.Type = 'ethernet'
	assert (vport.Type == 'ethernet')
	vport.refresh()
	print(vport)
	ixnetwork.add_Vport(Name='Abstract Port 2')
	ixnetwork.add_Vport(Name='Abstract Port 3')
	print(ixnetwork.Vport())

	topology = ixnetwork.add_Topology(Name='Device Group 1', Ports=ixnetwork.Vport())
	print(topology)

	device_group = topology.add_DeviceGroup(Name='Device 1', Multiplier='7')
	print(device_group)
	device_group.Enabled.Alternate('False')
	assert (device_group.Enabled == 'Alt: False')
	
	# create and print ethernet information
	ethernet = device_group.add_Ethernet()
	print(ethernet)

	# get multivalue information
	# # outputs format, count, possible patterns etc
	print(ethernet.Mac.Info)

	# multivalue steps
	steps = ethernet.Mac.Steps()
	for step in steps:
		print(step)
		step.Enabled = False
		step.refresh()
		assert (step.Enabled is False)
		
	# update multivalue on server immediately
	ethernet.Mac.Decrement(start_value='00:00:de:ad:be:ef', step_value='00:00:fa:ce:fa:ce')
	assert (ethernet.Mac == 'Dec: 00:00:de:ad:be:ef, 00:00:fa:ce:fa:ce')
	ethernet.Mac.Increment(start_value='00:00:fa:ce:fa:ce', step_value='00:00:de:ad:be:ef')
	assert (ethernet.Mac == 'Inc: 00:00:fa:ce:fa:ce, 00:00:de:ad:be:ef')
	ethernet.Mac.Random()
	assert (ethernet.Mac == 'Rand')
	ethernet.Mac.RandomRange()
	assert (ethernet.Mac.Pattern.startswith('Randr:'))
	ethernet.Mac.RandomMask()
	assert (ethernet.Mac.Pattern.startswith('Randb:'))
	ethernet.Mac.Distributed(algorithm='autoEven', mode='perPort', values=[('00:00:fa:ce:fa:ce', 60), ('0:00:de:ad:be:ef', 40)])
	assert (ethernet.Mac.Pattern.startswith('Dist:'))
	ethernet.Mac.ValueList(values=['00:00:fa:ce:fa:ce', '00:00:de:ad:be:ef'])
	assert (ethernet.Mac.Pattern.startswith('List:'))
	ethernet.Mac.Custom(start_value='00:00:fa:ce:fa:ce', step_value='00:00:de:ad:be:ef', increments=[('00:00:ab:ab:ab:ab', 6, [('00:00:01:01:01:01', 2, None)])])
	assert (ethernet.Mac.Pattern.startswith('Custom:'))
	print(ethernet.Mac.Values)
	
	ipv4 = ethernet.add_Ipv4(Name='Ipv4 1')
	print(ipv4)
	ipv4.Address.Increment(start_value='1.1.1.1', step_value='0.1.1.1')
	assert(ipv4.Address == 'Inc: 1.1.1.1, 0.1.1.1')
	
	bgp4 = ipv4.add_BgpIpv4Peer(Name='Bgp 1')
	bgp4.Md5Key.String('my-md5-key-{Dec: 1,1}')
	print(bgp4)

	vports = ixnetwork.Vport(Name=vport_name)
	assert (len(vports) == 1)
	assert (vports[0].Name == vport_name)
	ixnetwork.ReleasePort(ixnetwork.Vport())

	bgp6 = topology.add_DeviceGroup(Name='Device 2').add_Ethernet().add_Ipv6().add_BgpIpv6Peer()
	print(bgp6)

	# add one quick flow group per vport
	ixnetwork.AddQuickFlowGroups(ixnetwork.Vport(), 1)

	# config = ixnetwork.ResourceManager.ExportConfig(['/descendant-or-self::*'], False, 'json')
	# ixnetwork.ResourceManager.ImportConfig(config, True)

	# errors = ixnetwork.Globals.AppErrors()[0].Error(Name='JSON Import Errors')
	# for instance in errors[0].Instance():
	# 	print(instance)

	# chassis = ixnetwork.AvailableHardware.add_Chassis(Hostname='10.36.24.55')
except IxNetworkError as e:
	print(e)

if session is not None:
	session.remove()


