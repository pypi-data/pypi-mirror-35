from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RequestedLsps(Base):
	"""Requested LSPs
	"""

	_SDM_NAME = 'requestedLsps'

	def __init__(self, parent):
		super(RequestedLsps, self).__init__(parent)

	def PccRequestedMetricSubObjectsList(self, Active=None, Count=None, DescriptiveName=None, EnableBflag=None, EnableCflag=None, MetricType=None, MetricValue=None, Name=None, PFlagMetric=None):
		"""Gets child instances of PccRequestedMetricSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PccRequestedMetricSubObjectsList will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Active
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableBflag (obj(ixnetwork_restpy.multivalue.Multivalue)): B Flag
			EnableCflag (obj(ixnetwork_restpy.multivalue.Multivalue)): C Flag
			MetricType (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric Type
			MetricValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric Value
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PFlagMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Metric P Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pccrequestedmetricsubobjectslist.PccRequestedMetricSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pccrequestedmetricsubobjectslist import PccRequestedMetricSubObjectsList
		return self._select(PccRequestedMetricSubObjectsList(self), locals())

	def PcepIroSubObjectsList(self, Active=None, AsNumber=None, Count=None, DescriptiveName=None, InterfaceId=None, Ipv4Address=None, Ipv6Address=None, Name=None, PrefixLength=None, RouterId=None, SubObjectType=None):
		"""Gets child instances of PcepIroSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PcepIroSubObjectsList will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Active
			AsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): AS Number
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			InterfaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface ID
			Ipv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Address
			Ipv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Address
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Router ID
			SubObjectType (obj(ixnetwork_restpy.multivalue.Multivalue)): Sub Object Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepirosubobjectslist.PcepIroSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepirosubobjectslist import PcepIroSubObjectsList
		return self._select(PcepIroSubObjectsList(self), locals())

	def PcepXroSubObjectsList(self, Active=None, AsNumber=None, Attribute=None, Count=None, DescriptiveName=None, Exclude_bit=None, InterfaceId=None, Ipv4Address=None, Ipv6Address=None, Name=None, PFlagXro=None, PceId128=None, PceId32=None, PrefixLength=None, RouterId=None, SrlgId=None, SubObjectType=None):
		"""Gets child instances of PcepXroSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of PcepXroSubObjectsList will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Controls whether the XRO sub-object will be sent in the PCRequest message.
			AsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): AS Number
			Attribute (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates how the exclusion subobject is to be indicated
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Exclude_bit (obj(ixnetwork_restpy.multivalue.Multivalue)): Indicates whether the exclusion is mandatory or desired.
			InterfaceId (obj(ixnetwork_restpy.multivalue.Multivalue)): Interface ID
			Ipv4Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv4 Address
			Ipv6Address (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Address
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			PFlagXro (obj(ixnetwork_restpy.multivalue.Multivalue)): XRO P Flag
			PceId128 (obj(ixnetwork_restpy.multivalue.Multivalue)): 128 bit PKS ID
			PceId32 (obj(ixnetwork_restpy.multivalue.Multivalue)): 32 bit PKS ID
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Router ID
			SrlgId (obj(ixnetwork_restpy.multivalue.Multivalue)): SRLG ID
			SubObjectType (obj(ixnetwork_restpy.multivalue.Multivalue)): Using the Sub Object Type control user can configure which sub object needs to be included from the following options: IPv4 Prefix IPv6 Prefix Unnumbered Interface ID AS Number. SRLG

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepxrosubobjectslist.PcepXroSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pcepxrosubobjectslist import PcepXroSubObjectsList
		return self._select(PcepXroSubObjectsList(self), locals())

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
	def ActiveDataTrafficEndPoints(self):
		"""Specifies whether that specific Data Traffic Endpoint will generate data traffic

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('activeDataTrafficEndPoints')

	@property
	def Bandwidth(self):
		"""Bandwidth (bits/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidth')

	@property
	def BiDirectional(self):
		"""Bi-directional

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('biDirectional')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def DestinationIpv4Address(self):
		"""Destination IPv4 Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destinationIpv4Address')

	@property
	def DestinationIpv6Address(self):
		"""Destination IPv6 Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('destinationIpv6Address')

	@property
	def ExcludeAny(self):
		"""Exclude Any

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('excludeAny')

	@property
	def FailBit(self):
		"""Fail Bit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('failBit')

	@property
	def HoldingPriority(self):
		"""Holding Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('holdingPriority')

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
	def IncludeBandwidth(self):
		"""Include Bandwidth

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeBandwidth')

	@property
	def IncludeEndPoints(self):
		"""Include End Points

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeEndPoints')

	@property
	def IncludeIro(self):
		"""Include IRO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeIro')

	@property
	def IncludeLsp(self):
		"""Include LSP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeLsp')

	@property
	def IncludeLspa(self):
		"""Include LSPA

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeLspa')

	@property
	def IncludeMetric(self):
		"""Include Metric

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeMetric')

	@property
	def IncludeRp(self):
		"""Include RP

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeRp')

	@property
	def IncludeSymbolicPathNameTlv(self):
		"""Include Symbolic Path Name TLV

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeSymbolicPathNameTlv')

	@property
	def IncludeXro(self):
		"""Include XRO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeXro')

	@property
	def InitialDelegation(self):
		"""Initial Delegation

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('initialDelegation')

	@property
	def InsertIpv6ExplicitNull(self):
		"""Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6

		Returns:
			bool
		"""
		return self._get_attribute('insertIpv6ExplicitNull')
	@InsertIpv6ExplicitNull.setter
	def InsertIpv6ExplicitNull(self, value):
		self._set_attribute('insertIpv6ExplicitNull', value)

	@property
	def IpVersion(self):
		"""IP Version

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipVersion')

	@property
	def LocalProtection(self):
		"""Local Protection

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localProtection')

	@property
	def Loose(self):
		"""Loose

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('loose')

	@property
	def LspDelegationState(self):
		"""LSP Delegation State

		Returns:
			list(str[delegated|delegationConfirmed|delegationRejected|delegationReturned|delegationRevoked|nonDelegated|none])
		"""
		return self._get_attribute('lspDelegationState')

	@property
	def MaxExpectedSegmentCount(self):
		"""This control is used to set the maximum Segment count/ MPLS labels that would be present in the generted traffic.

		Returns:
			number
		"""
		return self._get_attribute('maxExpectedSegmentCount')
	@MaxExpectedSegmentCount.setter
	def MaxExpectedSegmentCount(self, value):
		self._set_attribute('maxExpectedSegmentCount', value)

	@property
	def MaxNoOfIroSubObjects(self):
		"""Max Number of IRO Sub Objects

		Returns:
			number
		"""
		return self._get_attribute('maxNoOfIroSubObjects')
	@MaxNoOfIroSubObjects.setter
	def MaxNoOfIroSubObjects(self, value):
		self._set_attribute('maxNoOfIroSubObjects', value)

	@property
	def MaxNoOfXroSubObjects(self):
		"""Max Number of XRO Sub Objects

		Returns:
			number
		"""
		return self._get_attribute('maxNoOfXroSubObjects')
	@MaxNoOfXroSubObjects.setter
	def MaxNoOfXroSubObjects(self, value):
		self._set_attribute('maxNoOfXroSubObjects', value)

	@property
	def MaxNumberOfMetrics(self):
		"""Max Number of Metrics

		Returns:
			number
		"""
		return self._get_attribute('maxNumberOfMetrics')
	@MaxNumberOfMetrics.setter
	def MaxNumberOfMetrics(self, value):
		self._set_attribute('maxNumberOfMetrics', value)

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
	def OverridePlspId(self):
		"""Override PLSP-ID

		Returns:
			bool
		"""
		return self._get_attribute('overridePlspId')
	@OverridePlspId.setter
	def OverridePlspId(self, value):
		self._set_attribute('overridePlspId', value)

	@property
	def OverrideRequestId(self):
		"""Override Request ID

		Returns:
			bool
		"""
		return self._get_attribute('overrideRequestId')
	@OverrideRequestId.setter
	def OverrideRequestId(self, value):
		self._set_attribute('overrideRequestId', value)

	@property
	def OverrideSourceAddress(self):
		"""Override Source Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('overrideSourceAddress')

	@property
	def PFlagBandwidth(self):
		"""Bandwidth P Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pFlagBandwidth')

	@property
	def PFlagIro(self):
		"""IRO P Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pFlagIro')

	@property
	def PFlagLsp(self):
		"""LSP P Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pFlagLsp')

	@property
	def PFlagLspa(self):
		"""LSPA P Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pFlagLspa')

	@property
	def PFlagRp(self):
		"""RP P Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pFlagRp')

	@property
	def PFlagXro(self):
		"""XRO P Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pFlagXro')

	@property
	def PflagEndpoints(self):
		"""End Points P Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pflagEndpoints')

	@property
	def PlspId(self):
		"""An identifier for the LSP. A PCC creates a unique PLSP-ID for each LSP that is constant for the lifetime of a PCEP session. The PCC will advertise the same PLSP-ID on all PCEP sessions it maintains at a given time.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('plspId')

	@property
	def Priority(self):
		"""Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('priority')

	@property
	def ReDelegationTimerStatus(self):
		"""Re-Delegation Timer Status

		Returns:
			list(str[expired|none|notStarted|running|stopped])
		"""
		return self._get_attribute('reDelegationTimerStatus')

	@property
	def ReOptimization(self):
		"""Re-optimization

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reOptimization')

	@property
	def RedelegationTimeoutInterval(self):
		"""The period of time a PCC waits for, when a PCEP session is terminated, before revoking LSP delegation to a PCE and attempting to redelegate LSPs associated with the terminated PCEP session to PCE.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('redelegationTimeoutInterval')

	@property
	def RequestId(self):
		"""Request ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('requestId')

	@property
	def SetupPriority(self):
		"""Setup Priority

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setupPriority')

	@property
	def SourceEndPointIPv4(self):
		"""Source IPv4 Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceEndPointIPv4')

	@property
	def SourceEndPointIPv6(self):
		"""Source IPv6 Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceEndPointIPv6')

	@property
	def SourceIpv4Address(self):
		"""Source IPv4 Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIpv4Address')

	@property
	def SourceIpv6Address(self):
		"""Source IPv6 Address

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIpv6Address')

	@property
	def SymbolicPathName(self):
		"""Symbolic Path Name

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('symbolicPathName')

	def Delegate(self, Arg2):
		"""Executes the delegate operation on the server.

		Delegate

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('delegate', payload=locals(), response_object=None)

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

	def RevokeDelegation(self, Arg2):
		"""Executes the revokeDelegation operation on the server.

		Revoke Delegation

		Args:
			Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('revokeDelegation', payload=locals(), response_object=None)
