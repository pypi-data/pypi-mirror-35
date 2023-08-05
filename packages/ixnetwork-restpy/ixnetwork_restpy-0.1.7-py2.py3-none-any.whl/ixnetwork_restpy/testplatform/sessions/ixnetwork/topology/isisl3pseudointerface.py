from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisL3PseudoInterface(Base):
	"""ISIS-L3 Pseudo Interafce Configuration
	"""

	_SDM_NAME = 'isisL3PseudoInterface'

	def __init__(self, parent):
		super(IsisL3PseudoInterface, self).__init__(parent)

	def IsisDcePseudoIfaceAttPoint1Config(self, Active=None, Count=None, DescriptiveName=None, LinkMetric=None, Name=None):
		"""Gets child instances of IsisDcePseudoIfaceAttPoint1Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisDcePseudoIfaceAttPoint1Config will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Flag.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config.IsisDcePseudoIfaceAttPoint1Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint1config import IsisDcePseudoIfaceAttPoint1Config
		return self._select(IsisDcePseudoIfaceAttPoint1Config(self), locals())

	def IsisDcePseudoIfaceAttPoint2Config(self, Active=None, Count=None, DescriptiveName=None, LinkMetric=None, Name=None):
		"""Gets child instances of IsisDcePseudoIfaceAttPoint2Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisDcePseudoIfaceAttPoint2Config will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Flag.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config.IsisDcePseudoIfaceAttPoint2Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisdcepseudoifaceattpoint2config import IsisDcePseudoIfaceAttPoint2Config
		return self._select(IsisDcePseudoIfaceAttPoint2Config(self), locals())

	def IsisL3PseudoIfaceAttPoint1Config(self, Active=None, Count=None, DescriptiveName=None, LinkMetric=None, Name=None):
		"""Gets child instances of IsisL3PseudoIfaceAttPoint1Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisL3PseudoIfaceAttPoint1Config will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Flag.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config.IsisL3PseudoIfaceAttPoint1Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint1config import IsisL3PseudoIfaceAttPoint1Config
		return self._select(IsisL3PseudoIfaceAttPoint1Config(self), locals())

	def IsisL3PseudoIfaceAttPoint2Config(self, Active=None, Count=None, DescriptiveName=None, LinkMetric=None, Name=None):
		"""Gets child instances of IsisL3PseudoIfaceAttPoint2Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisL3PseudoIfaceAttPoint2Config will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Flag.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config.IsisL3PseudoIfaceAttPoint2Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudoifaceattpoint2config import IsisL3PseudoIfaceAttPoint2Config
		return self._select(IsisL3PseudoIfaceAttPoint2Config(self), locals())

	def IsisSpbPseudoIfaceAttPoint1Config(self, Active=None, Count=None, DescriptiveName=None, LinkMetric=None, Name=None):
		"""Gets child instances of IsisSpbPseudoIfaceAttPoint1Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisSpbPseudoIfaceAttPoint1Config will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Flag.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config.IsisSpbPseudoIfaceAttPoint1Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint1config import IsisSpbPseudoIfaceAttPoint1Config
		return self._select(IsisSpbPseudoIfaceAttPoint1Config(self), locals())

	def IsisSpbPseudoIfaceAttPoint2Config(self, Active=None, Count=None, DescriptiveName=None, LinkMetric=None, Name=None):
		"""Gets child instances of IsisSpbPseudoIfaceAttPoint2Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisSpbPseudoIfaceAttPoint2Config will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Flag.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config.IsisSpbPseudoIfaceAttPoint2Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbpseudoifaceattpoint2config import IsisSpbPseudoIfaceAttPoint2Config
		return self._select(IsisSpbPseudoIfaceAttPoint2Config(self), locals())

	def IsisTrillPseudoIfaceAttPoint1Config(self, Active=None, Count=None, DescriptiveName=None, LinkMetric=None, Name=None):
		"""Gets child instances of IsisTrillPseudoIfaceAttPoint1Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisTrillPseudoIfaceAttPoint1Config will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Flag.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config.IsisTrillPseudoIfaceAttPoint1Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint1config import IsisTrillPseudoIfaceAttPoint1Config
		return self._select(IsisTrillPseudoIfaceAttPoint1Config(self), locals())

	def IsisTrillPseudoIfaceAttPoint2Config(self, Active=None, Count=None, DescriptiveName=None, LinkMetric=None, Name=None):
		"""Gets child instances of IsisTrillPseudoIfaceAttPoint2Config from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of IsisTrillPseudoIfaceAttPoint2Config will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Flag.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			LinkMetric (obj(ixnetwork_restpy.multivalue.Multivalue)): Link Metric
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config.IsisTrillPseudoIfaceAttPoint2Config))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillpseudoifaceattpoint2config import IsisTrillPseudoIfaceAttPoint2Config
		return self._select(IsisTrillPseudoIfaceAttPoint2Config(self), locals())

	def SrlgValueList(self, Count=None, DescriptiveName=None, Name=None, SrlgValue=None):
		"""Gets child instances of SrlgValueList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of SrlgValueList will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			SrlgValue (obj(ixnetwork_restpy.multivalue.Multivalue)): This is the SRLG Value for the link between two mentioned interfaces.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist.SrlgValueList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.srlgvaluelist import SrlgValueList
		return self._select(SrlgValueList(self), locals())

	@property
	def AdjSID(self):
		"""AdjSID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('adjSID')

	@property
	def AdministratorGroup(self):
		"""Administrator Group

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('administratorGroup')

	@property
	def BFlag(self):
		"""Backup Flag, if set, the Adj-SID is eligible for protection

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bFlag')

	@property
	def BandwidthPriority0_Bps(self):
		"""Bandwidth for Priority 0 (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthPriority0_Bps')

	@property
	def BandwidthPriority1_Bps(self):
		"""Bandwidth for Priority 1 (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthPriority1_Bps')

	@property
	def BandwidthPriority2_Bps(self):
		"""Bandwidth for Priority 2 (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthPriority2_Bps')

	@property
	def BandwidthPriority3_Bps(self):
		"""Bandwidth for Priority 3 (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthPriority3_Bps')

	@property
	def BandwidthPriority4_Bps(self):
		"""Bandwidth for Priority 4 (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthPriority4_Bps')

	@property
	def BandwidthPriority5_Bps(self):
		"""Bandwidth for Priority 5 (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthPriority5_Bps')

	@property
	def BandwidthPriority6_Bps(self):
		"""Bandwidth for Priority 6 (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthPriority6_Bps')

	@property
	def BandwidthPriority7_Bps(self):
		"""Bandwidth for Priority 7 (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('bandwidthPriority7_Bps')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DedicatedOnePlusOne(self):
		"""This is a Protection Scheme with value 0x10. It means that a dedicated disjoint link is protecting this link. However, the protecting link is not advertised in the link state database and is therefore not available for the routing of LSPs.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dedicatedOnePlusOne')

	@property
	def DedicatedOneToOne(self):
		"""This is a Protection Scheme with value 0x08. It means that there is one dedicated disjoint link of type Extra Traffic that is protecting this link.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('dedicatedOneToOne')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableAdjSID(self):
		"""Enable Adj SID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableAdjSID')

	@property
	def EnableIPv6SID(self):
		"""Enable IPv6 SID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableIPv6SID')

	@property
	def EnableLinkProtection(self):
		"""This enables the link protection on the ISIS link between two mentioned interfaces.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableLinkProtection')

	@property
	def EnableSRLG(self):
		"""This enables the SRLG on the ISIS link between two mentioned interfaces.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableSRLG')

	@property
	def Enhanced(self):
		"""This is a Protection Scheme with value 0x20. It means that a protection scheme that is more reliable than Dedicated 1+1, e.g., 4 fiber BLSR/MS-SPRING, is being used to protect this link.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enhanced')

	@property
	def ExtraTraffic(self):
		"""This is a Protection Scheme with value 0x01. It means that the link is protecting another link or links. The LSPs on a link of this type will be lost if any of the links it is protecting fail.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('extraTraffic')

	@property
	def FFlag(self):
		"""Address Family Flag,False value refers to an adjacency with outgoing IPv4 encapsulationTrue value refers to an adjacency with outgoing IPv6 encapsulation

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('fFlag')

	@property
	def Funcflags(self):
		"""This is the function flags

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('funcflags')

	@property
	def Function(self):
		"""This specifies endpoint function codes

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('function')

	@property
	def Ipv6SidValue(self):
		"""IPv6 Adj SID

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('ipv6SidValue')

	@property
	def LFlag(self):
		"""Local Flag, if set, then the value/index carried by the Adj-SID has local significance

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('lFlag')

	@property
	def LinkType(self):
		"""Link Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkType')

	@property
	def MaxBandwidth_Bps(self):
		"""Maximum Bandwidth (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxBandwidth_Bps')

	@property
	def MaxReservableBandwidth_Bps(self):
		"""Maximum Reservable Bandwidth (B/sec)

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('maxReservableBandwidth_Bps')

	@property
	def MetricLevel(self):
		"""Metric Level

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('metricLevel')

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
	def OverrideFFlag(self):
		"""When false, then F flag value in the packet will be set TRUE/ FALSE depending on whether IPv6/ IPv4 stack is present beside ISIS respectively. When true, then F flag value will be the one as configured.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('overrideFFlag')

	@property
	def PFlag(self):
		"""Persistent flag: when set, this indicates that the Adj-SID value remains persistent across router restart and/or interface flap.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('pFlag')

	@property
	def Reserved0x40(self):
		"""This is a Protection Scheme with value 0x40.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reserved0x40')

	@property
	def Reserved0x80(self):
		"""This is a Protection Scheme with value 0x80.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('reserved0x80')

	@property
	def SFlag(self):
		"""Set flag: when set, this indicates that the Adj-SID refers to a set of adjacencies

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sFlag')

	@property
	def Shared(self):
		"""This is a Protection Scheme with value 0x04. It means that there are one or more disjoint links of type Extra Traffic that are protecting this link. These Extra Traffic links are shared between one or more links of type Shared.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('shared')

	@property
	def SrlgCount(self):
		"""This field value shows how many SRLG Value columns would be there in the GUI.

		Returns:
			number
		"""
		return self._get_attribute('srlgCount')
	@SrlgCount.setter
	def SrlgCount(self, value):
		self._set_attribute('srlgCount', value)

	@property
	def Srv6SidFlags(self):
		"""This specifies the value of the SRv6 SID Flags

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('srv6SidFlags')

	@property
	def Unprotected(self):
		"""This is a Protection Scheme with value 0x02. It means that there is no other link protecting this link. The LSPs on a link of this type will be lost if the link fails.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('unprotected')

	@property
	def VFlag(self):
		"""Value Flag, if set, the Adjacency SID carries a value

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('vFlag')

	@property
	def Weight(self):
		"""Weight

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('weight')

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
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoInterface object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoInterface object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', payload=locals(), response_object=None)
