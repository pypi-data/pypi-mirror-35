from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Vport(Base):
	"""
	"""

	_SDM_NAME = 'vport'

	def __init__(self, parent):
		super(Vport, self).__init__(parent)

	@property
	def Capture(self):
		"""Returns the one and only one Capture object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.capture.Capture)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.capture.capture import Capture
		return self._read(Capture(self), None)

	@property
	def L1Config(self):
		"""Returns the one and only one L1Config object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.l1config.L1Config)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.l1config import L1Config
		return self._read(L1Config(self), None)

	@property
	def ActualSpeed(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('actualSpeed')

	@property
	def AssignedTo(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('assignedTo')

	@property
	def ConnectedTo(self):
		"""

		Returns:
			str(None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port)
		"""
		return self._get_attribute('connectedTo')
	@ConnectedTo.setter
	def ConnectedTo(self, value):
		self._set_attribute('connectedTo', value)

	@property
	def ConnectionInfo(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('connectionInfo')

	@property
	def ConnectionState(self):
		"""Consolidated state of the vport. This combines the connection state with link state.

		Returns:
			str(assignedInUseByOther|assignedUnconnected|connectedLinkDown|connectedLinkUp|connecting|unassigned)
		"""
		return self._get_attribute('connectionState')

	@property
	def ConnectionStatus(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('connectionStatus')

	@property
	def InternalId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('internalId')

	@property
	def IsAvailable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isAvailable')

	@property
	def IsConnected(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isConnected')

	@property
	def IsMapped(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isMapped')

	@property
	def IsPullOnly(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isPullOnly')
	@IsPullOnly.setter
	def IsPullOnly(self, value):
		self._set_attribute('isPullOnly', value)

	@property
	def IsVMPort(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isVMPort')

	@property
	def IxnChassisVersion(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixnChassisVersion')

	@property
	def IxnClientVersion(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixnClientVersion')

	@property
	def IxosChassisVersion(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('ixosChassisVersion')

	@property
	def Licenses(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('licenses')

	@property
	def Name(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def RxMode(self):
		"""

		Returns:
			str(capture|captureAndMeasure|measure|packetImpairment)
		"""
		return self._get_attribute('rxMode')
	@RxMode.setter
	def RxMode(self, value):
		self._set_attribute('rxMode', value)

	@property
	def State(self):
		"""

		Returns:
			str(busy|down|unassigned|up|versionMismatch)
		"""
		return self._get_attribute('state')

	@property
	def StateDetail(self):
		"""

		Returns:
			str(busy|cpuNotReady|idle|inActive|l1ConfigFailed|protocolsNotSupported|versionMismatched|waitingForCPUStatus)
		"""
		return self._get_attribute('stateDetail')

	@property
	def TransmitIgnoreLinkStatus(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('transmitIgnoreLinkStatus')
	@TransmitIgnoreLinkStatus.setter
	def TransmitIgnoreLinkStatus(self, value):
		self._set_attribute('transmitIgnoreLinkStatus', value)

	@property
	def TxGapControlMode(self):
		"""

		Returns:
			str(averageMode|fixedMode)
		"""
		return self._get_attribute('txGapControlMode')
	@TxGapControlMode.setter
	def TxGapControlMode(self, value):
		self._set_attribute('txGapControlMode', value)

	@property
	def TxMode(self):
		"""

		Returns:
			str(interleaved|interleavedCoarse|packetImpairment|sequential|sequentialCoarse)
		"""
		return self._get_attribute('txMode')
	@TxMode.setter
	def TxMode(self, value):
		self._set_attribute('txMode', value)

	@property
	def Type(self):
		"""

		Returns:
			str(atlasFourHundredGigLan|atlasFourHundredGigLanFcoe|atm|ethernet|ethernetFcoe|ethernetImpairment|ethernetvm|fc|fortyGigLan|fortyGigLanFcoe|hundredGigLan|hundredGigLanFcoe|krakenFourHundredGigLan|novusHundredGigLan|novusHundredGigLanFcoe|novusTenGigLan|novusTenGigLanFcoe|pos|tenFortyHundredGigLan|tenFortyHundredGigLanFcoe|tenGigLan|tenGigLanFcoe|tenGigWan|tenGigWanFcoe)
		"""
		return self._get_attribute('type')
	@Type.setter
	def Type(self, value):
		self._set_attribute('type', value)

	@property
	def ValidTxModes(self):
		"""

		Returns:
			list(str[interleaved|interleavedCoarse|packetImpairment|sequential|sequentialCoarse])
		"""
		return self._get_attribute('validTxModes')

	def remove(self):
		"""Deletes a child instance of Vport on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def Import(self, Arg2):
		"""Executes the import operation on the server.

		Imports the port file (also supports legacy port files).

		Args:
			Arg2 (obj(ixnetwork_restpy.files.Files)): The file to be imported.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		self._check_arg_type(Arg2, Files)
		return self._execute('import', payload=locals(), response_object=None)

	def PullPort(self):
		"""Executes the pullPort operation on the server.

		Pulls config onto vport or group of vports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('pullPort', payload=locals(), response_object=None)

	def RestartPppNegotiation(self):
		"""Executes the restartPppNegotiation operation on the server.

		Restarts the PPP negotiation on the port.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('restartPppNegotiation', payload=locals(), response_object=None)
