from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BgpEthernetSegmentV4(Base):
	"""BGP V4 Ethernet Segment Configuration
	"""

	_SDM_NAME = 'bgpEthernetSegmentV4'

	def __init__(self, parent):
		super(BgpEthernetSegmentV4, self).__init__(parent)

	def BgpAsPathSegmentList(self, Count=None, DescriptiveName=None, EnableASPathSegment=None, Name=None, NumberOfAsNumberInSegment=None, SegmentType=None):
		"""Gets child instances of BgpAsPathSegmentList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpAsPathSegmentList will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableASPathSegment (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Path Segment
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfAsNumberInSegment (number): Number of AS Number In Segment
			SegmentType (obj(ixnetwork_restpy.multivalue.Multivalue)): SegmentType

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist.BgpAsPathSegmentList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpaspathsegmentlist import BgpAsPathSegmentList
		return self._select(BgpAsPathSegmentList(self), locals())

	def BgpClusterIdList(self, ClusterId=None, Count=None, DescriptiveName=None, Name=None):
		"""Gets child instances of BgpClusterIdList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpClusterIdList will be returned.

		Args:
			ClusterId (obj(ixnetwork_restpy.multivalue.Multivalue)): Cluster ID
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist.BgpClusterIdList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpclusteridlist import BgpClusterIdList
		return self._select(BgpClusterIdList(self), locals())

	def BgpCommunitiesList(self, AsNumber=None, Count=None, DescriptiveName=None, LastTwoOctets=None, Name=None, Type=None):
		"""Gets child instances of BgpCommunitiesList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpCommunitiesList will be returned.

		Args:
			AsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): AS #
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LastTwoOctets (obj(ixnetwork_restpy.multivalue.Multivalue)): Last Two Octets
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist.BgpCommunitiesList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpcommunitieslist import BgpCommunitiesList
		return self._select(BgpCommunitiesList(self), locals())

	def BgpExtendedCommunitiesList(self, AsNumber2Bytes=None, AsNumber4Bytes=None, AssignedNumber2Bytes=None, AssignedNumber4Bytes=None, ColorCOBits=None, ColorReservedBits=None, ColorValue=None, Count=None, DescriptiveName=None, Ip=None, LinkBandwidth=None, Name=None, OpaqueData=None, SubType=None, Type=None):
		"""Gets child instances of BgpExtendedCommunitiesList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpExtendedCommunitiesList will be returned.

		Args:
			AsNumber2Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): AS 2-Bytes
			AsNumber4Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): AS 4-Bytes
			AssignedNumber2Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): Assigned Number(2 Octets)
			AssignedNumber4Bytes (obj(ixnetwork_restpy.multivalue.Multivalue)): Assigned Number(4 Octets)
			ColorCOBits (obj(ixnetwork_restpy.multivalue.Multivalue)): Color CO Bits
			ColorReservedBits (obj(ixnetwork_restpy.multivalue.Multivalue)): Color Reserved Bits
			ColorValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Color Value
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Ip (obj(ixnetwork_restpy.multivalue.Multivalue)): IP
			LinkBandwidth (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Bandwidth
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			OpaqueData (obj(ixnetwork_restpy.multivalue.Multivalue)): Opaque Data
			SubType (obj(ixnetwork_restpy.multivalue.Multivalue)): SubType
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Type

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist.BgpExtendedCommunitiesList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpextendedcommunitieslist import BgpExtendedCommunitiesList
		return self._select(BgpExtendedCommunitiesList(self), locals())

	@property
	def Bgpv4BMacMappedIpList(self):
		"""Returns the one and only one Bgpv4BMacMappedIpList object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv4bmacmappediplist.Bgpv4BMacMappedIpList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpv4bmacmappediplist import Bgpv4BMacMappedIpList
		return self._read(Bgpv4BMacMappedIpList(self), None)

	@property
	def AdvertiseAliasingBeforeAdPerEsRoute(self):
		"""Advertise Aliasing Before A-D/ES Route

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('AdvertiseAliasingBeforeAdPerEsRoute')

	@property
	def AdvertiseInclusiveMulticastRoute(self):
		"""Support Inclusive Multicast Ethernet Tag Route (RT Type 3)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('AdvertiseInclusiveMulticastRoute')

	@property
	def AliasingRouteGranularity(self):
		"""Aliasing Route Granularity

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('AliasingRouteGranularity')

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def AdvertiseAliasingAutomatically(self):
		"""Advertise Aliasing Automatically

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('advertiseAliasingAutomatically')

	@property
	def AggregatorAs(self):
		"""Aggregator AS

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregatorAs')

	@property
	def AggregatorId(self):
		"""Aggregator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('aggregatorId')

	@property
	def AsSetMode(self):
		"""AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('asSetMode')

	@property
	def AutoConfigureEsImport(self):
		"""Auto Configure ES-Import

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('autoConfigureEsImport')

	@property
	def BMacPrefix(self):
		"""B-MAC Prefix

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bMacPrefix')

	@property
	def BMacPrefixLength(self):
		"""B-MAC Prefix Length

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bMacPrefixLength')

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
	def DfElectionTimer(self):
		"""DF Election Timer(s)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dfElectionTimer')

	@property
	def EnableAggregatorId(self):
		"""Enable Aggregator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAggregatorId')

	@property
	def EnableAsPathSegments(self):
		"""Enable AS Path Segments

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAsPathSegments')

	@property
	def EnableAtomicAggregate(self):
		"""Enable Atomic Aggregate

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAtomicAggregate')

	@property
	def EnableCluster(self):
		"""Enable Cluster

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableCluster')

	@property
	def EnableCommunity(self):
		"""Enable Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableCommunity')

	@property
	def EnableExtendedCommunity(self):
		"""Enable Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableExtendedCommunity')

	@property
	def EnableLocalPreference(self):
		"""Enable Local Preference

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLocalPreference')

	@property
	def EnableMultiExitDiscriminator(self):
		"""Enable Multi Exit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableMultiExitDiscriminator')

	@property
	def EnableNextHop(self):
		"""Enable Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableNextHop')

	@property
	def EnableOrigin(self):
		"""Enable Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableOrigin')

	@property
	def EnableOriginatorId(self):
		"""Enable Originator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableOriginatorId')

	@property
	def EnableSingleActive(self):
		"""Enable Single-Active

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableSingleActive')

	@property
	def EnableStickyStaticFlag(self):
		"""Enable B-MAC Sticky/Static Flag

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableStickyStaticFlag')

	@property
	def EsImport(self):
		"""ES Import

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('esImport')

	@property
	def EsiLabel(self):
		"""ESI Label

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('esiLabel')

	@property
	def EsiType(self):
		"""ESI Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('esiType')

	@property
	def EsiValue(self):
		"""ESI Value

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('esiValue')

	@property
	def EvisCount(self):
		"""Number of EVIs

		Returns:
			number
		"""
		return self._get_attribute('evisCount')
	@EvisCount.setter
	def EvisCount(self, value):
		self._set_attribute('evisCount', value)

	@property
	def IncludeMacMobilityExtendedCommunity(self):
		"""Include MAC Mobility Extended Community

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('includeMacMobilityExtendedCommunity')

	@property
	def Ipv4NextHop(self):
		"""IPv4 Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv4NextHop')

	@property
	def Ipv6NextHop(self):
		"""IPv6 Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6NextHop')

	@property
	def LocalPreference(self):
		"""Local Preference

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('localPreference')

	@property
	def MultiExitDiscriminator(self):
		"""Multi Exit

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('multiExitDiscriminator')

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
	def NoOfASPathSegmentsPerRouteRange(self):
		"""Number Of AS Path Segments Per Route Range

		Returns:
			number
		"""
		return self._get_attribute('noOfASPathSegmentsPerRouteRange')
	@NoOfASPathSegmentsPerRouteRange.setter
	def NoOfASPathSegmentsPerRouteRange(self, value):
		self._set_attribute('noOfASPathSegmentsPerRouteRange', value)

	@property
	def NoOfClusters(self):
		"""Number of Clusters

		Returns:
			number
		"""
		return self._get_attribute('noOfClusters')
	@NoOfClusters.setter
	def NoOfClusters(self, value):
		self._set_attribute('noOfClusters', value)

	@property
	def NoOfCommunities(self):
		"""Number of Communities

		Returns:
			number
		"""
		return self._get_attribute('noOfCommunities')
	@NoOfCommunities.setter
	def NoOfCommunities(self, value):
		self._set_attribute('noOfCommunities', value)

	@property
	def NoOfExtendedCommunity(self):
		"""Number of Extended Communities

		Returns:
			number
		"""
		return self._get_attribute('noOfExtendedCommunity')
	@NoOfExtendedCommunity.setter
	def NoOfExtendedCommunity(self, value):
		self._set_attribute('noOfExtendedCommunity', value)

	@property
	def NoOfbMacMappedIpsV4(self):
		"""Number of B-MAC Mapped IPs

		Returns:
			number
		"""
		return self._get_attribute('noOfbMacMappedIpsV4')
	@NoOfbMacMappedIpsV4.setter
	def NoOfbMacMappedIpsV4(self, value):
		self._set_attribute('noOfbMacMappedIpsV4', value)

	@property
	def Origin(self):
		"""Origin

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('origin')

	@property
	def OriginatorId(self):
		"""Originator ID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('originatorId')

	@property
	def OverridePeerAsSetMode(self):
		"""Override Peer AS# Set Mode

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('overridePeerAsSetMode')

	@property
	def SetNextHop(self):
		"""Set Next Hop

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setNextHop')

	@property
	def SetNextHopIpType(self):
		"""Set Next Hop IP Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('setNextHopIpType')

	@property
	def SupportFastConvergence(self):
		"""Support Fast Convergence

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('supportFastConvergence')

	@property
	def SupportMultihomedEsAutoDiscovery(self):
		"""Support Multi-homed ES Auto Discovery

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('supportMultihomedEsAutoDiscovery')

	@property
	def UseControlWord(self):
		"""Use Control Word

		Returns:
			bool
		"""
		return self._get_attribute('useControlWord')
	@UseControlWord.setter
	def UseControlWord(self, value):
		self._set_attribute('useControlWord', value)

	@property
	def UseSameSequenceNumber(self):
		"""Use B-MAC Same Sequence Number

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('useSameSequenceNumber')

	def AdvertiseAdPerEsRoute(self, Arg2):
		"""Executes the advertiseAdPerEsRoute operation on the server.

		Advertise AD per ES Route.

		Args:
			Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('advertiseAdPerEsRoute', payload=locals(), response_object=None)

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

	def FlushRemoteCMACForwardingTable(self, Arg1):
		"""Executes the flushRemoteCMACForwardingTable operation on the server.

		Flush Remote CMAC Forwarding Table

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpEthernetSegmentV4 object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('flushRemoteCMACForwardingTable', payload=locals(), response_object=None)

	def FlushRemoteCMACForwardingTable(self, Arg1, SessionIndices):
		"""Executes the flushRemoteCMACForwardingTable operation on the server.

		Flush Remote CMAC Forwarding Table

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpEthernetSegmentV4 object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('flushRemoteCMACForwardingTable', payload=locals(), response_object=None)

	def FlushRemoteCMACForwardingTable(self, Arg1, SessionIndices):
		"""Executes the flushRemoteCMACForwardingTable operation on the server.

		Flush Remote CMAC Forwarding Table

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./bgpEthernetSegmentV4 object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('flushRemoteCMACForwardingTable', payload=locals(), response_object=None)

	def FlushRemoteCMACForwardingTable(self, Arg2):
		"""Executes the flushRemoteCMACForwardingTable operation on the server.

		Flush Remote CMAC Forwarding Table.

		Args:
			Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('flushRemoteCMACForwardingTable', payload=locals(), response_object=None)

	def WithdrawAdPerEsRoute(self, Arg2):
		"""Executes the withdrawAdPerEsRoute operation on the server.

		Withdraw AD per ES Route.

		Args:
			Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.

		Returns:
			list(str): ID to associate each async action invocation

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('withdrawAdPerEsRoute', payload=locals(), response_object=None)
