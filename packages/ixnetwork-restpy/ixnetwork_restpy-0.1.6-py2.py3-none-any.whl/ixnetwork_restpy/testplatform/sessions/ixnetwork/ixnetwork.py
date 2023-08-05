from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ixnetwork(Base):
	"""
	"""

	_SDM_NAME = 'ixnetwork'

	def __init__(self, parent):
		super(Ixnetwork, self).__init__(parent)

	@property
	def AvailableHardware(self):
		"""Returns the one and only one AvailableHardware object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.availablehardware.AvailableHardware)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.availablehardware import AvailableHardware
		return self._read(AvailableHardware(self), None)

	@property
	def Globals(self):
		"""Returns the one and only one Globals object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.globals.Globals)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.globals import Globals
		return self._read(Globals(self), None)

	def Lag(self, AggregationStatus=None, Count=None, DescriptiveName=None, Name=None):
		"""Gets child instances of Lag from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Lag will be returned.

		Args:
			AggregationStatus (str(all|none|some|unconfigured)): aggregation status of LAG
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.lag.Lag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.lag import Lag
		return self._select(Lag(self), locals())

	def add_Lag(self, Name=None, Vports=None):
		"""Adds a child instance of Lag on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Vports (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): Virtual port information.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.lag.Lag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.lag import Lag
		return self._create(Lag(self), locals())

	@property
	def ResourceManager(self):
		"""Returns the one and only one ResourceManager object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.resourcemanager.resourcemanager.ResourceManager)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.resourcemanager.resourcemanager import ResourceManager
		return self._read(ResourceManager(self), None)

	@property
	def Statistics(self):
		"""Returns the one and only one Statistics object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statistics.Statistics)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.statistics import Statistics
		return self._read(Statistics(self), None)

	def Topology(self, DescriptiveName=None, Name=None, Note=None, PortCount=None, Status=None):
		"""Gets child instances of Topology from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Topology will be returned.

		Args:
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Note (str): Any Note about the Topology
			PortCount (number): Number of /vports or /lags assigned (including unmapped ports)
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.topology.Topology))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.topology import Topology
		return self._select(Topology(self), locals())

	def add_Topology(self, Name=None, Note="", Ports=None, Vports=None):
		"""Adds a child instance of Topology on the server.

		Args:
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Note (str): Any Note about the Topology
			Ports (list(str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/vport])): Logical port information.
			Vports (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): Virtual port information.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.topology.Topology)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.topology import Topology
		return self._create(Topology(self), locals())

	@property
	def Traffic(self):
		"""Returns the one and only one Traffic object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.traffic.Traffic)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.traffic import Traffic
		return self._read(Traffic(self), None)

	def Vport(self, ActualSpeed=None, AssignedTo=None, ConnectedTo=None, ConnectionInfo=None, ConnectionState=None, ConnectionStatus=None, InternalId=None, IsAvailable=None, IsConnected=None, IsMapped=None, IsPullOnly=None, IsVMPort=None, IxnChassisVersion=None, IxnClientVersion=None, IxosChassisVersion=None, Licenses=None, Name=None, RxMode=None, State=None, StateDetail=None, TransmitIgnoreLinkStatus=None, TxGapControlMode=None, TxMode=None, Type=None):
		"""Gets child instances of Vport from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Vport will be returned.

		Args:
			ActualSpeed (number): 
			AssignedTo (str): 
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port)): 
			ConnectionInfo (str): 
			ConnectionState (str(assignedInUseByOther|assignedUnconnected|connectedLinkDown|connectedLinkUp|connecting|unassigned)): Consolidated state of the vport. This combines the connection state with link state.
			ConnectionStatus (str): 
			InternalId (number): 
			IsAvailable (bool): 
			IsConnected (bool): 
			IsMapped (bool): 
			IsPullOnly (bool): 
			IsVMPort (bool): 
			IxnChassisVersion (str): 
			IxnClientVersion (str): 
			IxosChassisVersion (str): 
			Licenses (str): 
			Name (str): 
			RxMode (str(capture|captureAndMeasure|measure|packetImpairment)): 
			State (str(busy|down|unassigned|up|versionMismatch)): 
			StateDetail (str(busy|cpuNotReady|idle|inActive|l1ConfigFailed|protocolsNotSupported|versionMismatched|waitingForCPUStatus)): 
			TransmitIgnoreLinkStatus (bool): 
			TxGapControlMode (str(averageMode|fixedMode)): 
			TxMode (str(interleaved|interleavedCoarse|packetImpairment|sequential|sequentialCoarse)): 
			Type (str(atlasFourHundredGigLan|atlasFourHundredGigLanFcoe|atm|ethernet|ethernetFcoe|ethernetImpairment|ethernetvm|fc|fortyGigLan|fortyGigLanFcoe|hundredGigLan|hundredGigLanFcoe|krakenFourHundredGigLan|novusHundredGigLan|novusHundredGigLanFcoe|novusTenGigLan|novusTenGigLanFcoe|pos|tenFortyHundredGigLan|tenFortyHundredGigLanFcoe|tenGigLan|tenGigLanFcoe|tenGigWan|tenGigWanFcoe)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport import Vport
		return self._select(Vport(self), locals())

	def add_Vport(self, ConnectedTo=None, IsPullOnly=None, Name=None, RxMode=None, TransmitIgnoreLinkStatus=None, TxGapControlMode=None, TxMode=None, Type=None):
		"""Adds a child instance of Vport on the server.

		Args:
			ConnectedTo (str(None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port)): 
			IsPullOnly (bool): 
			Name (str): 
			RxMode (str(capture|captureAndMeasure|measure|packetImpairment)): 
			TransmitIgnoreLinkStatus (bool): 
			TxGapControlMode (str(averageMode|fixedMode)): 
			TxMode (str(interleaved|interleavedCoarse|packetImpairment|sequential|sequentialCoarse)): 
			Type (str(atlasFourHundredGigLan|atlasFourHundredGigLanFcoe|atm|ethernet|ethernetFcoe|ethernetImpairment|ethernetvm|fc|fortyGigLan|fortyGigLanFcoe|hundredGigLan|hundredGigLanFcoe|krakenFourHundredGigLan|novusHundredGigLan|novusHundredGigLanFcoe|novusTenGigLan|novusTenGigLanFcoe|pos|tenFortyHundredGigLan|tenFortyHundredGigLanFcoe|tenGigLan|tenGigLanFcoe|tenGigWan|tenGigWanFcoe)): 

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport.Vport)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.vport import Vport
		return self._create(Vport(self), locals())

	def ApplyITWizardConfiguration(self):
		"""Executes the applyITWizardConfiguration operation on the server.

		Applies the first Quick Test found in the current configuration.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('applyITWizardConfiguration', payload=locals(), response_object=None)

	def ApplyITWizardConfiguration(self, TestName):
		"""Executes the applyITWizardConfiguration operation on the server.

		Applies the specified Quick Test.

		Args:
			TestName (str): The name of the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('applyITWizardConfiguration', payload=locals(), response_object=None)

	def ApplyL1Blocking(self):
		"""Executes the applyL1Blocking operation on the server.

		Apply L1 blocking.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('applyL1Blocking', payload=locals(), response_object=None)

	def AssignPorts(self, Arg1, Arg2, Arg3, Arg4):
		"""Executes the assignPorts operation on the server.

		Assign hardware ports to virtual ports.

		Args:
			Arg1 (list(dict(arg1:str,arg2:str,arg3:str))): A list of chassis, card, port combinations to include.
			Arg2 (list(dict(arg1:str,arg2:str,arg3:str))): A list of chassis, card, port combinations to exclude.
			Arg3 (list(str[None|/api/v1/sessions/1/ixnetwork/vport])): A list of virtual port object references that hardware ports will be attached to.
			Arg4 (bool): If true, it will clear ownership on the hardware ports.

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport]): Returns a list of virtual port object references that were successfully connected.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('assignPorts', payload=locals(), response_object=None)

	def ClearAppLibraryStats(self):
		"""Executes the clearAppLibraryStats operation on the server.

		Clears the statistics published by AppLibrary.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearAppLibraryStats', payload=locals(), response_object=None)

	def ClearCPDPStats(self):
		"""Executes the clearCPDPStats operation on the server.

		Clear control plane and data plane statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearCPDPStats', payload=locals(), response_object=None)

	def ClearPortsAndTrafficStats(self):
		"""Executes the clearPortsAndTrafficStats operation on the server.

		The command to clear the existing port and traffic statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearPortsAndTrafficStats', payload=locals(), response_object=None)

	def ClearPortsAndTrafficStats(self, Arg1):
		"""Executes the clearPortsAndTrafficStats operation on the server.

		The command to clear the existing port and traffic statistics with option to wait to refresh traffic statistics.

		Args:
			Arg1 (list(str[waitForPortStatsRefresh|waitForTrafficStatsRefresh])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearPortsAndTrafficStats', payload=locals(), response_object=None)

	def ClearProtocolStats(self):
		"""Executes the clearProtocolStats operation on the server.

		Clear the protocol statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearProtocolStats', payload=locals(), response_object=None)

	def ClearStats(self):
		"""Executes the clearStats operation on the server.

		The command to clear the existing statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearStats', payload=locals(), response_object=None)

	def ClearStats(self, Arg1):
		"""Executes the clearStats operation on the server.

		The command to clear the existing statistics with option to wait to refresh traffic statistics.

		Args:
			Arg1 (list(str[waitForPortStatsRefresh|waitForTrafficStatsRefresh])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearStats', payload=locals(), response_object=None)

	def CloseAllTabs(self):
		"""Executes the closeAllTabs operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('closeAllTabs', payload=locals(), response_object=None)

	def CloseAllTabs(self, Arg1):
		"""Executes the closeAllTabs operation on the server.

		Args:
			Arg1 (list(str)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('closeAllTabs', payload=locals(), response_object=None)

	def CollectLogs(self, Arg1):
		"""Executes the collectLogs operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('collectLogs', payload=locals(), response_object=None)

	def CollectLogs(self, Arg1, Arg2):
		"""Executes the collectLogs operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (list(str[currentInstance|specificProfile])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('collectLogs', payload=locals(), response_object=None)

	def CollectLogs(self, Arg1, Arg2, Arg3):
		"""Executes the collectLogs operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (list(str[currentInstance|specificProfile])): 
			Arg3 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('collectLogs', payload=locals(), response_object=None)

	def CollectLogs(self, Arg1, Arg2, Arg3, Arg4):
		"""Executes the collectLogs operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (list(str[currentInstance|specificProfile])): 
			Arg3 (str): 
			Arg4 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('collectLogs', payload=locals(), response_object=None)

	def CollectLogs(self, Arg1, Arg2, Arg3, Arg4, Arg5):
		"""Executes the collectLogs operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (list(str[currentInstance|specificProfile])): 
			Arg3 (str): 
			Arg4 (str): 
			Arg5 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('collectLogs', payload=locals(), response_object=None)

	def CollectLogs(self, Arg1, Arg2):
		"""Executes the collectLogs operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('collectLogs', payload=locals(), response_object=None)

	def CollectLogs(self, Arg1, Arg2, Arg3):
		"""Executes the collectLogs operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (str): 
			Arg3 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('collectLogs', payload=locals(), response_object=None)

	def CopyFile(self, Arg1, Arg2):
		"""Executes the copyFile operation on the server.

		Copies from first stream into the second stream.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): The source file for the copy operation. This stream must be readable.
			Arg2 (obj(ixnetwork_restpy.files.Files)): The destination file for the copy operation. This stream must be writable.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		self._check_arg_type(Arg2, Files)
		return self._execute('copyFile', payload=locals(), response_object=None)

	def GenerateReport(self):
		"""Executes the generateReport operation on the server.

		This report feature generates an integrated test report file.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('generateReport', payload=locals(), response_object=None)

	def GetAggregatedDeviceGroupStatus(self):
		"""Executes the getAggregatedDeviceGroupStatus operation on the server.

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:list[dict(arg1:str,arg2:number)])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAggregatedDeviceGroupStatus', payload=locals(), response_object=None)

	def GetAllPorts(self):
		"""Executes the getAllPorts operation on the server.

		The command to get all the ports.

		Returns:
			str: A string with all the ports.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAllPorts', payload=locals(), response_object=None)

	def GetAvailableProtocolStats(self):
		"""Executes the getAvailableProtocolStats operation on the server.

		The command to get available protocol statistics.

		Returns:
			str: A string with all the legacy protocols statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAvailableProtocolStats', payload=locals(), response_object=None)

	def GetAvailableSlotLicense(self, Arg1):
		"""Executes the getAvailableSlotLicense operation on the server.

		This exec returns number of AppLibrary Slot License avaibale for use in the chassis.

		Args:
			Arg1 (str): The IPv4 address of the chassis.

		Returns:
			number: The number of AppLibrary Slot License available for use in the chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAvailableSlotLicense', payload=locals(), response_object=None)

	def GetAvailableStatsForProtocol(self, Arg1):
		"""Executes the getAvailableStatsForProtocol operation on the server.

		The command to get available statistics for the protocol.

		Args:
			Arg1 (str): Protocol name.

		Returns:
			str: A string with all the available statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAvailableStatsForProtocol', payload=locals(), response_object=None)

	def GetAvailableStatsForSourceType(self, Arg1):
		"""Executes the getAvailableStatsForSourceType operation on the server.

		The command to get available statistics for the source type.

		Args:
			Arg1 (str): Source type.

		Returns:
			str: A string with all the available statistics.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getAvailableStatsForSourceType', payload=locals(), response_object=None)

	def GetConfiguredProtocols(self):
		"""Executes the getConfiguredProtocols operation on the server.

		The command to get the configured protocols.

		Returns:
			str: A list with all the protocols configured in the test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getConfiguredProtocols', payload=locals(), response_object=None)

	def GetConfiguredProtocolsForPort(self, Arg1):
		"""Executes the getConfiguredProtocolsForPort operation on the server.

		The command to get the configured protocols for the port.

		Args:
			Arg1 (number): Port ID.

		Returns:
			str: A string with all the available protocols configured on the port.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getConfiguredProtocolsForPort', payload=locals(), response_object=None)

	def GetCsvColumnNames(self, Arg1):
		"""Executes the getCsvColumnNames operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 

		Returns:
			list(str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('getCsvColumnNames', payload=locals(), response_object=None)

	def GetDefaultSnapshotSettings(self):
		"""Executes the GetDefaultSnapshotSettings operation on the server.

		Gets the default snapshot settings.

		Returns:
			list(str): An array with settings.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('GetDefaultSnapshotSettings', payload=locals(), response_object=None)

	def GetInstalledSlotLicenseCount(self, Arg1):
		"""Executes the getInstalledSlotLicenseCount operation on the server.

		This exec returns number of AppLibrary Slot License installed in the chassis.

		Args:
			Arg1 (str): The IPv4 address of the chassis.

		Returns:
			number: The number of AppLibrary Slot License installed in the chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getInstalledSlotLicenseCount', payload=locals(), response_object=None)

	def GetIntersectionPortsForProtocols(self, Arg1):
		"""Executes the getIntersectionPortsForProtocols operation on the server.

		The command to get intersection ports for the protocols.

		Args:
			Arg1 (list(str)): A list of protocol names.

		Returns:
			str: The list of port IDs that have all the given protocols configured.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getIntersectionPortsForProtocols', payload=locals(), response_object=None)

	def GetNetworkGroupSize(self):
		"""Executes the getNetworkGroupSize operation on the server.

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:list[dict(arg1:str,arg2:number)])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getNetworkGroupSize', payload=locals(), response_object=None)

	def GetPortsForProtocol(self, Arg1):
		"""Executes the getPortsForProtocol operation on the server.

		The command to get ports for the protocol.

		Args:
			Arg1 (str): Protocol name.

		Returns:
			str: A string with all the port IDs having the protocol configured.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getPortsForProtocol', payload=locals(), response_object=None)

	def GetRecommendedSettings(self, Arg1, Arg2):
		"""Executes the getRecommendedSettings operation on the server.

		It will get the recommended settings for the given copper type. Available choices are: oneMeter, threeMeters, fiveMeters.

		Args:
			Arg1 (str): 
			Arg2 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getRecommendedSettings', payload=locals(), response_object=None)

	def GetSlotLicenseInUse(self, Arg1):
		"""Executes the getSlotLicenseInUse operation on the server.

		This exec returns a list of slots/cards of the chassis that are currently using the AppLibrary Slot Licenses.

		Args:
			Arg1 (str): The IPv4 address of the chassis.

		Returns:
			list(number): An array of slot/card numbers of the chassis that currently checked-out AppLibrary Slot Licenses.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getSlotLicenseInUse', payload=locals(), response_object=None)

	def GetTapSettings(self):
		"""Executes the getTapSettings operation on the server.

		Get TAP Settings for all the connected chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getTapSettings', payload=locals(), response_object=None)

	def GetTopologyStatus(self):
		"""Executes the getTopologyStatus operation on the server.

		Returns:
			list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*],arg2:list[dict(arg1:str,arg2:number)],arg3:str[notstarted\~starting\~started\~stopping\~error\~mixed])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getTopologyStatus', payload=locals(), response_object=None)

	def GetUnionPortsForProtocols(self, Arg1):
		"""Executes the getUnionPortsForProtocols operation on the server.

		The command to get union ports for the protocols.

		Args:
			Arg1 (list(str)): A list of protocol names.

		Returns:
			str: The list of port IDs that have at least one of the given protocols configured.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getUnionPortsForProtocols', payload=locals(), response_object=None)

	def Import(self, File):
		"""Executes the import operation on the server.

		Imports a legacy IxAutomate configuration from the specified file.

		Args:
			File (str): The IxAutomate configuration file that will be imported.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('import', payload=locals(), response_object=None)

	def LoadConfig(self, Arg1):
		"""Executes the loadConfig operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('loadConfig', payload=locals(), response_object=None)

	def MergeCapture(self, Arg1, Arg2, Arg3, Arg4):
		"""Executes the mergeCapture operation on the server.

		Args:
			Arg1 (str): 
			Arg2 (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=capture)): 
			Arg3 (str(control|data)): 
			Arg4 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('mergeCapture', payload=locals(), response_object=None)

	def MergeCapture(self, Arg1, Arg2, Arg3):
		"""Executes the mergeCapture operation on the server.

		Args:
			Arg1 (str): 
			Arg2 (str): 
			Arg3 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('mergeCapture', payload=locals(), response_object=None)

	def NewConfig(self):
		"""Executes the newConfig operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('newConfig', payload=locals(), response_object=None)

	def Refresh(self, Arg1):
		"""Executes the refresh operation on the server.

		Args:
			Arg1 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('refresh', payload=locals(), response_object=None)

	def RemoveAllTclViews(self):
		"""Executes the removeAllTclViews operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('removeAllTclViews', payload=locals(), response_object=None)

	def SaveCapture(self, Arg1):
		"""Executes the saveCapture operation on the server.

		Args:
			Arg1 (str): Directory for saving the captures

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('saveCapture', payload=locals(), response_object=None)

	def SaveCapture(self, Arg1, Arg2):
		"""Executes the saveCapture operation on the server.

		Args:
			Arg1 (str): Directory for saving the captures
			Arg2 (str): Suffix used for naming the capture files

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('saveCapture', payload=locals(), response_object=None)

	def SaveCaptureFiles(self, Arg1):
		"""Executes the saveCaptureFiles operation on the server.

		Args:
			Arg1 (str): Directory for saving the captures

		Returns:
			list(str): A list of relative paths of all the captures saved

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('saveCaptureFiles', payload=locals(), response_object=None)

	def SaveCaptureFiles(self, Arg1, Arg2):
		"""Executes the saveCaptureFiles operation on the server.

		Args:
			Arg1 (str): Directory for saving the captures
			Arg2 (str): Suffix used for naming the capture files

		Returns:
			list(str): A list of relative paths of all the captures saved

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('saveCaptureFiles', payload=locals(), response_object=None)

	def SaveConfig(self, Arg1):
		"""Executes the saveConfig operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('saveConfig', payload=locals(), response_object=None)

	def Scriptgen(self):
		"""Executes the scriptgen operation on the server.

		Returns:
			str: 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('scriptgen', payload=locals(), response_object=None)

	def Scriptgen(self, Arg1):
		"""Executes the scriptgen operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('scriptgen', payload=locals(), response_object=None)

	def Scriptgen(self, Arg1, Arg2):
		"""Executes the scriptgen operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('scriptgen', payload=locals(), response_object=None)

	def Scriptgen(self, Arg1, Arg2, Arg3):
		"""Executes the scriptgen operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (str): 
			Arg3 (list(str)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('scriptgen', payload=locals(), response_object=None)

	def Scriptgen(self, Arg1, Arg2, Arg3, Arg4, Arg5):
		"""Executes the scriptgen operation on the server.

		Args:
			Arg1 (obj(ixnetwork_restpy.files.Files)): 
			Arg2 (str): 
			Arg3 (list(str)): 
			Arg4 (number): 
			Arg5 (number): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._check_arg_type(Arg1, Files)
		return self._execute('scriptgen', payload=locals(), response_object=None)

	def Select(self, Selects):
		"""Executes the select operation on the server.

		Select nodes and properties from the hierarchy

		Args:
			Selects (list(dict(from:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(child:str,properties:list[str])]))): A list of select structures.Each select structure consists of a starting point in the hierarchy. This starting point must exist and is defined as the 'from' value.Properties for the 'from' value are optional and can be retrieved using the 'properties' list.To retrieve all properties specify the '*' wildcard. Regex is not supported in the 'properties' list.Individual nodes under the starting point can be retrieved. These are specified in the 'children' list.Each item in the children list contains a 'child' name, a list of 'properties' and a list of filters by which to reduce the result set.The 'child' name can be a single name or a regex.Properties that reference another object can have that object's content inlined by specifying inline children.Any child nodes below the object reference can be expanded as long as they are specified in the inline children.

		Returns:
			str: A json encoded string of result sets.The encoded string will contain a list of result sets with each select producing a result set.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('select', payload=locals(), response_object=None)

	def SetGuardRailVersion(self, Arg1):
		"""Executes the setGuardRailVersion operation on the server.

		Args:
			Arg1 (str): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('setGuardRailVersion', payload=locals(), response_object=None)

	def SetLoggingLevel(self, Arg1):
		"""Executes the setLoggingLevel operation on the server.

		Args:
			Arg1 (str(kDebug|kError|kFatal|kInfo|kNothing|kWarn)): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('setLoggingLevel', payload=locals(), response_object=None)

	def SetPortTransmitDuration(self, Arg1):
		"""Executes the setPortTransmitDuration operation on the server.

		Set the port transmit duration.

		Args:
			Arg1 (list(dict(arg1:number,arg2:list[str[None|/api/v1/sessions/1/ixnetwork/lag|/api/v1/sessions/1/ixnetwork/traffic|/api/v1/sessions/1/ixnetwork/traffic?deepchild=trafficItem|/api/v1/sessions/1/ixnetwork/traffic?deepchild=highLevelStream|/api/v1/sessions/1/ixnetwork/vport]]))): An array of structures. Each structure is an duration and a valid object reference.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('setPortTransmitDuration', payload=locals(), response_object=None)

	def SetSnapshotSettingsToDefault(self, Arg1):
		"""Executes the SetSnapshotSettingsToDefault operation on the server.

		Set the settings of snapshot to default.

		Args:
			Arg1 (str): The setting name.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('SetSnapshotSettingsToDefault', payload=locals(), response_object=None)

	def SetTapSettings(self):
		"""Executes the setTapSettings operation on the server.

		Send TAP Settings to IxServer for all the connected chassis.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('setTapSettings', payload=locals(), response_object=None)

	def StartAllProtocols(self):
		"""Executes the startAllProtocols operation on the server.

		Starts all configured protocols under /vport/protocols, /vport/protocolStack and /topology

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startAllProtocols', payload=locals(), response_object=None)

	def StartAllProtocols(self, Arg1):
		"""Executes the startAllProtocols operation on the server.

		Starts all configured protocols under /vport/protocols, /vport/protocolStack and /topology

		Args:
			Arg1 (str(async|sync)): An enum indicating whether or not the exec will be executed synchronously or asynsynchronously

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startAllProtocols', payload=locals(), response_object=None)

	def StartCapture(self):
		"""Executes the startCapture operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('startCapture', payload=locals(), response_object=None)

	def StopAllProtocols(self):
		"""Executes the stopAllProtocols operation on the server.

		Stops all configured protocols under /vport/protocols, /vport/protocolStack and /topology

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopAllProtocols', payload=locals(), response_object=None)

	def StopAllProtocols(self, Arg1):
		"""Executes the stopAllProtocols operation on the server.

		Stops all configured protocols under /vport/protocols, /vport/protocolStack and /topology

		Args:
			Arg1 (str(async|sync)): An enum indicating whether or not the exec will be executed synchronously or asynsynchronously

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopAllProtocols', payload=locals(), response_object=None)

	def StopCapture(self):
		"""Executes the stopCapture operation on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopCapture', payload=locals(), response_object=None)

	def StopTestConfiguration(self):
		"""Executes the stopTestConfiguration operation on the server.

		Stops the currently running Quick Test.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stopTestConfiguration', payload=locals(), response_object=None)

	def SyncStatisticsStartTimeWithClientClock(self, Arg1):
		"""Executes the syncStatisticsStartTimeWithClientClock operation on the server.

		Args:
			Arg1 (bool): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('syncStatisticsStartTimeWithClientClock', payload=locals(), response_object=None)

	def TakeViewCSVSnapshot(self, Arg1, Arg2):
		"""Executes the TakeViewCSVSnapshot operation on the server.

		Performs Snapshot CSV on the given views.

		Args:
			Arg1 (list(str)): A list of views for which to take a snapshot.
			Arg2 (list(str)): A list of settings, given in the form of SettingName:SettingValue.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('TakeViewCSVSnapshot', payload=locals(), response_object=None)

	def WaitForLicenseBroadcast(self, Arg1):
		"""Executes the waitForLicenseBroadcast operation on the server.

		Args:
			Arg1 (number): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('waitForLicenseBroadcast', payload=locals(), response_object=None)
