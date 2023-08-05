from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Tables(Base):
	"""Openflow Controller Table Configuration
	"""

	_SDM_NAME = 'tables'

	def __init__(self, parent):
		super(Tables, self).__init__(parent)

	def FlowSet(self, Active=None, Cookie=None, CookieMask=None, Count=None, DescriptiveName=None, FlowAdvertise=None, FlowFlags=None, FlowMatchType=None, FlowSetId=None, HardTimeout=None, IdleTimeout=None, Name=None, NumberOfFlows=None, Priority=None):
		"""Gets child instances of FlowSet from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of FlowSet will be returned.

		Args:
			Active (obj(ixnetwork_restpy.multivalue.Multivalue)): Activate/Deactivate Configuration
			Cookie (obj(ixnetwork_restpy.multivalue.Multivalue)): Cookie of the flow entry that was looked up. This is the opaque controller-issued identifier.
			CookieMask (obj(ixnetwork_restpy.multivalue.Multivalue)): The mask used to restrict the cookie bits.
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			FlowAdvertise (bool): If selected, the flows are advertised by the OF Channel.
			FlowFlags (obj(ixnetwork_restpy.multivalue.Multivalue)): Allows to configure the Flow Flags. Options are: 1) Send Flow Removed 2) Check Overlap 3) Reset Counts 4) No Packet Count 5) No Byte Count
			FlowMatchType (obj(ixnetwork_restpy.multivalue.Multivalue)): The type of match to be configured. Options include the following: 1) Strict 2) Loose
			FlowSetId (str): Specify the controller Flow Set identifier.
			HardTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The inactive time in seconds after which the Flow range will hard timeout and close.
			IdleTimeout (obj(ixnetwork_restpy.multivalue.Multivalue)): The inactive time in seconds after which the Flow range will timeout and become idle.
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			NumberOfFlows (number): The number of flows to be configured for the controller table.
			Priority (obj(ixnetwork_restpy.multivalue.Multivalue)): The priority level for the Flow Range.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flowset.FlowSet))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.flowset import FlowSet
		return self._select(FlowSet(self), locals())

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def ChannelIndex(self):
		"""Parent Channel Index

		Returns:
			list(str)
		"""
		return self._get_attribute('channelIndex')

	@property
	def ChannelRemoteIp(self):
		"""The remote IP address of the OF Channel. This field is auto-populated and cannot be changed.

		Returns:
			list(str)
		"""
		return self._get_attribute('channelRemoteIp')

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
	def NumberOfFlowSet(self):
		"""Specify the number of Flow Set for this controller configuration.

		Returns:
			number
		"""
		return self._get_attribute('numberOfFlowSet')
	@NumberOfFlowSet.setter
	def NumberOfFlowSet(self, value):
		self._set_attribute('numberOfFlowSet', value)

	@property
	def TableId(self):
		"""Specify the controller table identifier. Lower numbered tables are consulted first.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tableId')

	@property
	def TableName(self):
		"""Specify the name of the controller table.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('tableName')

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
