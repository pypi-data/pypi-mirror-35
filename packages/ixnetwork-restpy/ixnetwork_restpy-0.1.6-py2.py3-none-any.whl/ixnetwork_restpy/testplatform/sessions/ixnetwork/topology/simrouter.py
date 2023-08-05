from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SimRouter(Base):
	"""Simulated router specific configuration inside a Network Topology.
	"""

	_SDM_NAME = 'simRouter'

	def __init__(self, parent):
		super(SimRouter, self).__init__(parent)

	def Connector(self, ConnectedTo=None, Count=None, PropagateMultiplier=None):
		"""Gets child instances of Connector from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Connector will be returned.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Scenario element this connector is connecting to
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			PropagateMultiplier (bool): The Connector will propagate the multiplicity of destination back to the source and its parent NetworkElementSet

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
		return self._select(Connector(self), locals())

	def add_Connector(self, ConnectedTo=None):
		"""Adds a child instance of Connector on the server.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*)): Scenario element this connector is connecting to

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
		return self._create(Connector(self), locals())

	def IsisL3PseudoRouter(self, Active=None, AdvertiseSRLB=None, AdvertiseSidAsLocator=None, Algorithm=None, ConfigureSIDIndexLabel=None, Count=None, DBit=None, DBitForSRv6Cap=None, DBitInsideSRv6SidTLV=None, DescriptiveName=None, EFlag=None, EFlagOfSRv6CapTlv=None, Enable=None, EnableMTIPv6=None, EnableSR=None, EnableWMforTEinNetworkGroup=None, EnableWideMetric=None, Funcflags=None, Function=None, IncludeMaximumEndDSrhTLV=None, IncludeMaximumEndPopSrhTLV=None, IncludeMaximumSLTLV=None, IncludeMaximumTEncapSrhTLV=None, IncludeMaximumTInsertSrhTLV=None, Ipv4Flag=None, Ipv6Flag=None, Ipv6MTMetric=None, Ipv6NodePrefix=None, Ipv6Srh=None, LFlag=None, LocatorPrefixLength=None, Mask=None, MaxEndD=None, MaxEndPopSrh=None, MaxSL=None, MaxTEncap=None, MaxTInsert=None, NFlag=None, Name=None, NodePrefix=None, OFlagOfSRv6CapTlv=None, PFlag=None, PrefixLength=None, RFlag=None, Redistribution=None, RedistributionForSRv6=None, ReservedInsideFlagsOfSRv6SidTLV=None, ReservedInsideSRv6CapFlag=None, RouteMetric=None, RouteOrigin=None, RtrcapId=None, RtrcapIdForSrv6=None, SBit=None, SBitForSRv6Cap=None, SIDIndexLabel=None, SRAlgorithmCount=None, SRGBRangeCount=None, SrlbDescriptorCount=None, SrlbFlags=None, TERouterId=None, VFlag=None):
		"""Gets child instances of IsisL3PseudoRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisL3PseudoRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			AdvertiseSRLB (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables advertisement of Segment Routing Local Block (SRLB) Sub-Tlv in Router Capability Tlv
			AdvertiseSidAsLocator (obj(ixnetwork_restpy.multivalue.Multivalue)): If enabled, then the configured IPv6 Node SID gets advertised as a reachable IPv6 prefix
			Algorithm (obj(ixnetwork_restpy.multivalue.Multivalue)): Algorithm
			ConfigureSIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure SID/Index/Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DBit (obj(ixnetwork_restpy.multivalue.Multivalue)): When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear
			DBitForSRv6Cap (obj(ixnetwork_restpy.multivalue.Multivalue)): When the IS-IS Router CAPABILITY TLV is leaked from level-2 to level-1, the D bit MUST be set, else it should be clear
			DBitInsideSRv6SidTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): When the SID is leaked from level-2 to level-1, the D bit MUST be set. Otherwise, this bit MUST be clear.
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Explicit NULL flag
			EFlagOfSRv6CapTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then router is able to apply T.Encap operation
			Enable (obj(ixnetwork_restpy.multivalue.Multivalue)): TE Enabled
			EnableMTIPv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable MT for IPv6
			EnableSR (bool): Enable Segment Routing
			EnableWMforTEinNetworkGroup (obj(ixnetwork_restpy.multivalue.Multivalue)): Hidden field is to disable wide Metric, when user disable TE Router in Network Group
			EnableWideMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable Wide Metric
			Funcflags (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the function flags
			Function (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies endpoint function codes
			IncludeMaximumEndDSrhTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Maximum End D SRH TLV in SRv6 capability
			IncludeMaximumEndPopSrhTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Max-End-Pop-SRH TLV in SRv6 capability
			IncludeMaximumSLTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Maximum SL TLV in SRv6 capability
			IncludeMaximumTEncapSrhTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Maximum T.Encap SRH TLV in SRv6 capability
			IncludeMaximumTInsertSrhTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, then include Maximum T.Insert SRH TLV in SRv6 capability
			Ipv4Flag (obj(ixnetwork_restpy.multivalue.Multivalue)): MPLS IPv4 Flag
			Ipv6Flag (obj(ixnetwork_restpy.multivalue.Multivalue)): MPLS IPv6 Flag
			Ipv6MTMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 MT Metric
			Ipv6NodePrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): IPv6 Node Prefix
			Ipv6Srh (obj(ixnetwork_restpy.multivalue.Multivalue)): Router will advertise and process IPv6 SR related TLVs
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local Flag
			LocatorPrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Locator Prefix Length
			Mask (obj(ixnetwork_restpy.multivalue.Multivalue)): Mask
			MaxEndD (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum number of SIDs in an SRH when applying End.DX6 and End.DT6 functions. If this field is zero, then the router cannot apply End.DX6 or End.DT6 functions if the extension header right underneath the outer IPv6 header is an SRH.
			MaxEndPopSrh (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum number of SIDs in the top SRH in an SRH stack that the router can apply PSP or USP flavors to. If the value of this field is zero, then the router cannot apply PSP or USP flavors.
			MaxSL (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum value of the Segments Left (SL) field in the SRH of a received packet before applying the function associated with a SID.
			MaxTEncap (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum number of SIDs that can be included as part of the T.Encap behavior. If this field is zero and the E flag is set, then the router can apply T.Encap by encapsulating the incoming packet in another IPv6 header without SRH the same way IPinIP encapsulation is performed. If the E flag is clear, then this field SHOULD be transmitted as zero and MUST be ignored on receipt.
			MaxTInsert (obj(ixnetwork_restpy.multivalue.Multivalue)): This field specifies the maximum number of SIDs that can be inserted as part of the T.insert behavior. If the value of this field is zero, then the router cannot apply any variation of the T.insert behavior.
			NFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Nodal prefix flag
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NodePrefix (obj(ixnetwork_restpy.multivalue.Multivalue)): Node Prefix
			OFlagOfSRv6CapTlv (obj(ixnetwork_restpy.multivalue.Multivalue)): If set, it indicates that this packet is an operations and management (OAM) packet.
			PFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): No-PHP flag. If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID.
			PrefixLength (obj(ixnetwork_restpy.multivalue.Multivalue)): Prefix Length
			RFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution flag
			Redistribution (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution
			RedistributionForSRv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Redistribution
			ReservedInsideFlagsOfSRv6SidTLV (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the reserved field (part of flags field of SRv6 SID TLV)
			ReservedInsideSRv6CapFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the reserved field (as part of Flags field of SRv6 Capability TLV)
			RouteMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Metric
			RouteOrigin (obj(ixnetwork_restpy.multivalue.Multivalue)): Route Origin
			RtrcapId (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Capability Id
			RtrcapIdForSrv6 (obj(ixnetwork_restpy.multivalue.Multivalue)): Router Capability Id
			SBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels
			SBitForSRv6Cap (obj(ixnetwork_restpy.multivalue.Multivalue)): Enabling S bit lets the IS-IS Router CAPABILITY TLV to get flooded across the entire routing domain, otherwise the TLV not be leaked between levels
			SIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): SID/Index/Label
			SRAlgorithmCount (number): SR Algorithm Count
			SRGBRangeCount (number): SRGB Range Count
			SrlbDescriptorCount (number): Count of the SRLB descriptor entries, each being a tuple having format {Start SID/Label, SID Count}
			SrlbFlags (obj(ixnetwork_restpy.multivalue.Multivalue)): This specifies the value of the SRLB flags field
			TERouterId (obj(ixnetwork_restpy.multivalue.Multivalue)): TE Router ID
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudorouter.IsisL3PseudoRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudorouter import IsisL3PseudoRouter
		return self._select(IsisL3PseudoRouter(self), locals())

	def LdpPseudoRouter(self, Active=None, Count=None, DescriptiveName=None, LabelValue=None, Name=None):
		"""Gets child instances of LdpPseudoRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of LdpPseudoRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LabelValue (obj(ixnetwork_restpy.multivalue.Multivalue)): Label Value Start
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldppseudorouter.LdpPseudoRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldppseudorouter import LdpPseudoRouter
		return self._select(LdpPseudoRouter(self), locals())

	def OspfPseudoRouter(self, Active=None, AdvertiseRouterIdAsStubNetwork=None, Algorithm=None, BBit=None, ConfigureSIDIndexLabel=None, Count=None, DescriptiveName=None, EBit=None, EFlag=None, EnableSegmentRouting=None, LFlag=None, MFlag=None, Name=None, NpFlag=None, SRAlgorithmCount=None, SidIndexLabel=None, SrgbRangeCount=None, VFlag=None):
		"""Gets child instances of OspfPseudoRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of OspfPseudoRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/DeActivate OSPF Simulated Router
			AdvertiseRouterIdAsStubNetwork (obj(ixnetwork_restpy.multivalue.Multivalue)): Advertise RouterId As Stub Network
			Algorithm (obj(ixnetwork_restpy.multivalue.Multivalue)): Algorithm for the Node SID/Label
			BBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router-LSA B-Bit
			ConfigureSIDIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): Configure SID/Index/Label
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router-LSA E-Bit
			EFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Explicit-Null Flag
			EnableSegmentRouting (bool): Enable Segment Routing
			LFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Local or Global Flag
			MFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Mapping Server Flag
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NpFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): No-PHP Flag
			SRAlgorithmCount (number): SR Algorithm Count
			SidIndexLabel (obj(ixnetwork_restpy.multivalue.Multivalue)): SID/Index/Label
			SrgbRangeCount (number): SRGB Range Count
			VFlag (obj(ixnetwork_restpy.multivalue.Multivalue)): Value or Index Flag

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudorouter.OspfPseudoRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudorouter import OspfPseudoRouter
		return self._select(OspfPseudoRouter(self), locals())

	def Ospfv3PseudoRouter(self, Active=None, BBit=None, Count=None, DescriptiveName=None, EBit=None, Name=None):
		"""Gets child instances of Ospfv3PseudoRouter from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Ospfv3PseudoRouter will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			BBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router-LSA B-Bit
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EBit (obj(ixnetwork_restpy.multivalue.Multivalue)): Router-LSA E-Bit
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3pseudorouter.Ospfv3PseudoRouter))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3pseudorouter import Ospfv3PseudoRouter
		return self._select(Ospfv3PseudoRouter(self), locals())

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
	def RouterId(self):
		"""4 Byte Router Id in dotted decimal format.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('routerId')

	@property
	def SystemId(self):
		"""6 Byte System Id in hex format.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('systemId')

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

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./simRouter object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./simRouter object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
