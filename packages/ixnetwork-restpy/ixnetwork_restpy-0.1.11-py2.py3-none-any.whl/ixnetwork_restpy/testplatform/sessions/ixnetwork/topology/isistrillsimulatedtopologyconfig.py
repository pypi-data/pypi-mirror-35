from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisTrillSimulatedTopologyConfig(Base):
	"""TRILL Simulated Topology Configuration
	"""

	_SDM_NAME = 'isisTrillSimulatedTopologyConfig'

	def __init__(self, parent):
		super(IsisTrillSimulatedTopologyConfig, self).__init__(parent)

	@property
	def TrillNodeTopologyList(self):
		"""Returns the one and only one TrillNodeTopologyList object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trillnodetopologylist.TrillNodeTopologyList)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.trillnodetopologylist import TrillNodeTopologyList
		return self._read(TrillNodeTopologyList(self), None)

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

	@property
	def TrillNodeTopologyCount(self):
		"""Node Topology Count(multiplier)

		Returns:
			number
		"""
		return self._get_attribute('trillNodeTopologyCount')
	@TrillNodeTopologyCount.setter
	def TrillNodeTopologyCount(self, value):
		self._set_attribute('trillNodeTopologyCount', value)

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
