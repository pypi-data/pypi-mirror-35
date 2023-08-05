from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisDceSimulatedTopologyConfig(Base):
	"""Fabric-Path Simulated Topology Configuration
	"""

	_SDM_NAME = 'isisDceSimulatedTopologyConfig'

	def __init__(self, parent):
		super(IsisDceSimulatedTopologyConfig, self).__init__(parent)

	@property
	def DceNodeTopologyList(self):
		"""Returns the one and only one DceNodeTopologyList object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dcenodetopologylist.DceNodeTopologyList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dcenodetopologylist import DceNodeTopologyList
		return self._read(DceNodeTopologyList(self), None)

	@property
	def Active(self):
		"""Activate/Deactivate Configuration

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('active')

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DceNodeTopologyCount(self):
		"""Node Topology Count(multiplier)

		Returns:
			number
		"""
		return self._get_attribute('dceNodeTopologyCount')
	@DceNodeTopologyCount.setter
	def DceNodeTopologyCount(self, value):
		self._set_attribute('dceNodeTopologyCount', value)

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def EnableHostName(self):
		"""Enable Host Name

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableHostName')

	@property
	def HostName(self):
		"""Host Name

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('hostName')

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
