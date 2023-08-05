from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Layer23TrafficPortFilter(Base):
	"""
	"""

	_SDM_NAME = 'layer23TrafficPortFilter'

	def __init__(self, parent):
		super(Layer23TrafficPortFilter, self).__init__(parent)

	@property
	def PortFilterIds(self):
		"""

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/statistics?deepchild=availablePortFilter])
		"""
		return self._get_attribute('portFilterIds')
	@PortFilterIds.setter
	def PortFilterIds(self, value):
		self._set_attribute('portFilterIds', value)

	def remove(self):
		"""Deletes a child instance of Layer23TrafficPortFilter on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()
