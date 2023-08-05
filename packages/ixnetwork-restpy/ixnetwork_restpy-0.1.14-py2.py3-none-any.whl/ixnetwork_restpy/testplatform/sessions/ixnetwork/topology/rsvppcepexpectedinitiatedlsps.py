from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class RsvpPcepExpectedInitiatedLsps(Base):
	"""RSVP-TE PCEP Expected Initiated LSPs
	"""

	_SDM_NAME = 'rsvpPcepExpectedInitiatedLsps'

	def __init__(self, parent):
		super(RsvpPcepExpectedInitiatedLsps, self).__init__(parent)

	def RsvpIngressRROSubObjectsList(self, BandwidthProtection=None, CType=None, Count=None, DescriptiveName=None, GlobalLabel=None, Ip=None, Label=None, Name=None, NodeProtection=None, ProtectionAvailable=None, ProtectionInUse=None, Type=None):
		"""Gets child instances of RsvpIngressRROSubObjectsList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of RsvpIngressRROSubObjectsList will be returned.

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
			Type (obj(ixnetwork_restpy.multivalue.Multivalue)): Reservation Style

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist.RsvpIngressRROSubObjectsList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.rsvpingressrrosubobjectslist import RsvpIngressRROSubObjectsList
		return self._select(RsvpIngressRROSubObjectsList(self), locals())

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
	def BackupLspId(self):
		"""

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('backupLspId')

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
	def EnableRRO(self):
		"""Enable RRO

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableRRO')

	@property
	def LocalIp(self):
		"""Local IP

		Returns:
			list(str)
		"""
		return self._get_attribute('localIp')

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
	def SessionInformation(self):
		"""Logs additional information about the RSVP session state

		Returns:
			list(str[lastErrLSPAdmissionControlFailure|lastErrLSPBadAdSpecValue|lastErrLSPBadExplicitRoute|lastErrLSPBadFlowspecValue|lastErrLSPBadInitialSubobject|lastErrLSPBadLooseNode|lastErrLSPBadStrictNode|lastErrLSPBadTSpecValue|lastErrLSPDelayBoundNotMet|lastErrLSPMPLSAllocationFailure|lastErrLSPMTUTooBig|lastErrLSPNonRSVPRouter|lastErrLSPNoRouteAvailable|lastErrLSPPathErr|lastErrLSPPathTearSent|lastErrLSPRequestedBandwidthUnavailable|lastErrLSPReservationTearReceived|lastErrLSPReservationTearSent|lastErrLSPReservationTimeout|lastErrLSPRoutingLoops|lastErrLSPRoutingProblem|lastErrLSPRSVPSystemError|lastErrLSPServiceConflict|lastErrLSPServiceUnsupported|lastErrLSPTrafficControlError|lastErrLSPTrafficControlSystemError|lastErrLSPTrafficOrganizationError|lastErrLSPTrafficServiceError|lastErrLSPUnknownObjectClass|lastErrLSPUnknownObjectCType|lastErrLSPUnsupportedL3PID|lSPAdmissionControlFailure|lSPBadAdSpecValue|lSPBadExplicitRoute|lSPBadFlowspecValue|lSPBadInitialSubobject|lSPBadLooseNode|lSPBadStrictNode|lSPBadTSpecValue|lSPDelayBoundNotMet|lSPMPLSAllocationFailure|lSPMTUTooBig|lSPNonRSVPRouter|lSPNoRouteAvailable|lSPPathErr|lSPPathTearSent|lSPPceInitiatedMsgNotReceived|lSPRequestedBandwidthUnavailable|lSPReservationNotReceived|lSPReservationTearReceived|lSPReservationTearSent|lSPReservationTimeout|lSPRoutingLoops|lSPRoutingProblem|lSPRSVPSystemError|lSPServiceConflict|lSPServiceUnsupported|lSPTrafficControlError|lSPTrafficControlSystemError|lSPTrafficOrganizationError|lSPTrafficServiceError|lSPUnknownObjectClass|lSPUnknownObjectCType|lSPUnsupportedL3PID|mbbCompleted|mbbTriggered|none])
		"""
		return self._get_attribute('sessionInformation')

	@property
	def State(self):
		"""State

		Returns:
			list(str[down|none|notStarted|pceRequestNotReceived|up])
		"""
		return self._get_attribute('state')

	@property
	def SymbolicPathName(self):
		"""This is used for generating the traffic for those LSPs from PCE for which the Symbolic Path Name is configured and matches the value.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('symbolicPathName')

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
