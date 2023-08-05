from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RsvpP2mpIngressLsps(Base):
	"""RSVP-TE P2MP Head (Ingress) LSPs
	"""

	_SDM_NAME = 'rsvpP2mpIngressLsps'

	def __init__(self, parent):
		super(RsvpP2mpIngressLsps, self).__init__(parent)

	def RsvpDetourSubObjectsList(self, AvoidNodeId=None, Count=None, DescriptiveName=None, Name=None, PlrId=None):
		"""Gets child instances of RsvpDetourSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of RsvpDetourSubObjectsList will be returned.

		Args:
			AvoidNodeId (obj(ixnetwork_restpy.multivalue.Multivalue)): Avoid Node ID
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PlrId (obj(ixnetwork_restpy.multivalue.Multivalue)): PLR ID

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpdetoursubobjectslist.RsvpDetourSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpdetoursubobjectslist import RsvpDetourSubObjectsList
		return self._select(RsvpDetourSubObjectsList(self), locals())

	def RsvpIngressRroSubObjectsList(self, BandwidthProtection=None, CType=None, Count=None, DescriptiveName=None, GlobalLabel=None, Ip=None, Label=None, Name=None, NodeProtection=None, ProtectionAvailable=None, ProtectionInUse=None, Type=None):
		"""Gets child instances of RsvpIngressRroSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of RsvpIngressRroSubObjectsList will be returned.

		Args:
			BandwidthProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): Bandwidth Protection
			CType (obj(ixnetwork_restpy.multivalue.Multivalue)): C-Type
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			GlobalLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Global Label
			Ip (obj(ixnetwork_restpy.multivalue.Multivalue)): IP
			Label (obj(ixnetwork_restpy.multivalue.Multivalue)): Label
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NodeProtection (obj(ixnetwork_restpy.multivalue.Multivalue)): Node Protection
			ProtectionAvailable (obj(ixnetwork_restpy.multivalue.Multivalue)): Protection Available
			ProtectionInUse (obj(ixnetwork_restpy.multivalue.Multivalue)): Protection In Use
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Type: IP or Label

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist.RsvpIngressRroSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist import RsvpIngressRroSubObjectsList
		return self._select(RsvpIngressRroSubObjectsList(self), locals())

	@property
	def RsvpP2mpIngressSubLsps(self):
		"""Returns the one and only one RsvpP2mpIngressSubLsps object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresssublsps.RsvpP2mpIngressSubLsps)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpp2mpingresssublsps import RsvpP2mpIngressSubLsps
		return self._read(RsvpP2mpIngressSubLsps(self), None)

	def Tag(self, __id__=None, Count=None, Enabled=None, Name=None):
		"""Gets child instances of Tag from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Tag will be returned.

		Args:
			__id__ (obj(ixnetwork_restpy.multivalue.Multivalue)): the tag ids that this entity will use/publish
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return self._select(Tag(self), locals())

	def add_Tag(self, Enabled="False", Name=None):
		"""Adds a child instance of Tag on the server.

		Args:
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return self._create(Tag(self), locals())

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AutoGenerateSessionName(self):
		"""Auto Generate Session Name

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('autoGenerateSessionName')

	@property
	def BackupLspId(self):
		"""Backup LSP Id Pool Start

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspId')

	@property
	def BandwidthProtectionDesired(self):
		"""Bandwidth Protection Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthProtectionDesired')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DelayLspSwitchOver(self):
		"""Delay LSP switch over

		Returns:
			bool
		"""
		return self._get_attribute('delayLspSwitchOver')
	@DelayLspSwitchOver.setter
	def DelayLspSwitchOver(self, value):
		self._set_attribute('delayLspSwitchOver', value)

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableFastReroute(self):
		"""Enable Fast Reroute

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableFastReroute')

	@property
	def EnablePathReOptimization(self):
		"""Enable Path Re-Optimization

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enablePathReOptimization')

	@property
	def EnablePeriodicReEvaluationRequest(self):
		"""Enable Periodic Re-Evaluation Request

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enablePeriodicReEvaluationRequest')

	@property
	def ExcludeAny(self):
		"""Exclude Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('excludeAny')

	@property
	def FacilityBackupDesired(self):
		"""Facility Backup Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('facilityBackupDesired')

	@property
	def FastRerouteBandwidth(self):
		"""Bandwidth (bps)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteBandwidth')

	@property
	def FastRerouteExcludeAny(self):
		"""Exclude Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteExcludeAny')

	@property
	def FastRerouteHoldingPriority(self):
		"""Holding Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteHoldingPriority')

	@property
	def FastRerouteIncludeAll(self):
		"""Include All

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteIncludeAll')

	@property
	def FastRerouteIncludeAny(self):
		"""Include Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteIncludeAny')

	@property
	def FastRerouteSetupPriority(self):
		"""Setup Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fastRerouteSetupPriority')

	@property
	def HoldingPriority(self):
		"""Holding Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdingPriority')

	@property
	def HopLimit(self):
		"""Hop Limit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hopLimit')

	@property
	def IncludeAll(self):
		"""Include All

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAll')

	@property
	def IncludeAny(self):
		"""Include Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeAny')

	@property
	def IncludeConnectedIpOnTop(self):
		"""Include connected IP on top

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeConnectedIpOnTop')

	@property
	def IncludeHeadIpAtBottom(self):
		"""Include Head IP at bottom

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeHeadIpAtBottom')

	@property
	def IngressP2mpSubLspRanges(self):
		"""Number of P2MP Ingress Sub LSPs configured per RSVP-TE P2MP Ingress LSP

		Returns:
			number
		"""
		return self._get_attribute('ingressP2mpSubLspRanges')
	@IngressP2mpSubLspRanges.setter
	def IngressP2mpSubLspRanges(self, value):
		self._set_attribute('ingressP2mpSubLspRanges', value)

	@property
	def InsertIPv6ExplicitNull(self):
		"""Insert IPv6 explicit NULL

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('insertIPv6ExplicitNull')

	@property
	def LabelRecordingDesired(self):
		"""Label Recording Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('labelRecordingDesired')

	@property
	def LocalIp(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('localIp')

	@property
	def LocalProtectionDesired(self):
		"""Local Protection Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localProtectionDesired')

	@property
	def LspId(self):
		"""LSP Id

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lspId')

	@property
	def LspSwitchOverDelayTime(self):
		"""LSP Switch Over Delay timer (sec)

		Returns:
			number
		"""
		return self._get_attribute('lspSwitchOverDelayTime')
	@LspSwitchOverDelayTime.setter
	def LspSwitchOverDelayTime(self, value):
		self._set_attribute('lspSwitchOverDelayTime', value)

	@property
	def MaximumPacketSize(self):
		"""Maximum Packet Size

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maximumPacketSize')

	@property
	def MinimumPolicedUnit(self):
		"""Minimum Policed Unit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('minimumPolicedUnit')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def NodeProtectionDesired(self):
		"""Node Protection Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('nodeProtectionDesired')

	@property
	def NumberOfDetourSubObjects(self):
		"""Number Of Detour Sub-Objects

		Returns:
			number
		"""
		return self._get_attribute('numberOfDetourSubObjects')
	@NumberOfDetourSubObjects.setter
	def NumberOfDetourSubObjects(self, value):
		self._set_attribute('numberOfDetourSubObjects', value)

	@property
	def NumberOfRroSubObjects(self):
		"""Number Of RRO Sub-Objects

		Returns:
			number
		"""
		return self._get_attribute('numberOfRroSubObjects')
	@NumberOfRroSubObjects.setter
	def NumberOfRroSubObjects(self, value):
		self._set_attribute('numberOfRroSubObjects', value)

	@property
	def OneToOneBackupDesired(self):
		"""One To One Backup Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('oneToOneBackupDesired')

	@property
	def P2mpIdAsNumber(self):
		"""P2MP ID displayed in Integer format

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('p2mpIdAsNumber')

	@property
	def P2mpIdIp(self):
		"""P2MP ID displayed in IP Address format

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('p2mpIdIp')

	@property
	def PeakDataRate(self):
		"""Peak Data Rate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('peakDataRate')

	@property
	def ReEvaluationRequestInterval(self):
		"""Re-Evaluation Request Interval

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reEvaluationRequestInterval')

	@property
	def RefreshInterval(self):
		"""Refresh Interval (ms)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('refreshInterval')

	@property
	def ResourceAffinities(self):
		"""Resource Affinities

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('resourceAffinities')

	@property
	def SeStyleDesired(self):
		"""SE Style Desired

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('seStyleDesired')

	@property
	def SendDetour(self):
		"""Send Detour

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendDetour')

	@property
	def SendRro(self):
		"""Send RRO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sendRro')

	@property
	def SessionName(self):
		"""Session Name

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sessionName')

	@property
	def SetupPriority(self):
		"""Setup Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setupPriority')

	@property
	def SourceIpv4(self):
		"""Source IPv4

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIpv4')

	@property
	def SourceIpv6(self):
		"""Source IPv6

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIpv6')

	@property
	def State(self):
		"""State

		Returns:
			list(str[down|none|notStarted|up])
		"""
		return self._get_attribute('state')

	@property
	def TimeoutMultiplier(self):
		"""Timeout Multiplier

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('timeoutMultiplier')

	@property
	def TokenBucketRate(self):
		"""Token Bucket Rate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tokenBucketRate')

	@property
	def TokenBucketSize(self):
		"""Token Bucket Size

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tokenBucketSize')

	@property
	def TunnelId(self):
		"""Tunnel ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tunnelId')

	@property
	def TypeP2mpId(self):
		"""P2MP ID Type

		Returns:
			str(iP|p2MPId)
		"""
		return self._get_attribute('typeP2mpId')
	@TypeP2mpId.setter
	def TypeP2mpId(self, value):
		self._set_attribute('typeP2mpId', value)

	@property
	def UsingHeadendIp(self):
		"""Using Headend IP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('usingHeadendIp')

	def FetchAndUpdateConfigFromCloud(self, Mode):
		"""Executes the fetchAndUpdateConfigFromCloud operation on the server.

		Args:
			Mode (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('fetchAndUpdateConfigFromCloud', payload=locals(), response_object=None)

	def InitiateP2mpPathReoptimization(self, Arg1):
		"""Executes the initiateP2mpPathReoptimization operation on the server.

		Send P2MP Path with re-evaluation request bit of SESSION-ATTRIBUTE object set, for selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('initiateP2mpPathReoptimization', payload=locals(), response_object=None)

	def InitiateP2mpPathReoptimization(self, Arg1, SessionIndices):
		"""Executes the initiateP2mpPathReoptimization operation on the server.

		Send P2MP Path with re-evaluation request bit of SESSION-ATTRIBUTE object set, for selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('initiateP2mpPathReoptimization', payload=locals(), response_object=None)

	def InitiateP2mpPathReoptimization(self, Arg1, SessionIndices):
		"""Executes the initiateP2mpPathReoptimization operation on the server.

		Send P2MP Path with re-evaluation request bit of SESSION-ATTRIBUTE object set, for selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('initiateP2mpPathReoptimization', payload=locals(), response_object=None)

	def InitiatePathReoptimization(self, Arg2):
		"""Executes the initiatePathReoptimization operation on the server.

		Initiate Path Reoptimization

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('initiatePathReoptimization', payload=locals(), response_object=None)

	def MakeBeforeBreak(self, Arg2):
		"""Executes the makeBeforeBreak operation on the server.

		Make Before Break

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('makeBeforeBreak', payload=locals(), response_object=None)

	def P2mpMakeBeforeBreak(self, Arg1):
		"""Executes the p2mpMakeBeforeBreak operation on the server.

		Initiate P2MP Make Before Break for selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('p2mpMakeBeforeBreak', payload=locals(), response_object=None)

	def P2mpMakeBeforeBreak(self, Arg1, SessionIndices):
		"""Executes the p2mpMakeBeforeBreak operation on the server.

		Initiate P2MP Make Before Break for selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('p2mpMakeBeforeBreak', payload=locals(), response_object=None)

	def P2mpMakeBeforeBreak(self, Arg1, SessionIndices):
		"""Executes the p2mpMakeBeforeBreak operation on the server.

		Initiate P2MP Make Before Break for selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('p2mpMakeBeforeBreak', payload=locals(), response_object=None)

	def Start(self, Arg1):
		"""Executes the start operation on the server.

		Activate/Enable P2MP Tunnel selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Activate/Enable P2MP Tunnel selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg1, SessionIndices):
		"""Executes the start operation on the server.

		Activate/Enable P2MP Tunnel selected Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Start(self, Arg2):
		"""Executes the start operation on the server.

		Start

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Arg1):
		"""Executes the stop operation on the server.

		Deactivate/Disable P2MP selected Tunnel Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Deactivate/Disable P2MP selected Tunnel Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg1, SessionIndices):
		"""Executes the stop operation on the server.

		Deactivate/Disable P2MP selected Tunnel Head Ranges

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./rsvpP2mpIngressLsps object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)

	def Stop(self, Arg2):
		"""Executes the stop operation on the server.

		Stop

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('stop', payload=locals(), response_object=None)
