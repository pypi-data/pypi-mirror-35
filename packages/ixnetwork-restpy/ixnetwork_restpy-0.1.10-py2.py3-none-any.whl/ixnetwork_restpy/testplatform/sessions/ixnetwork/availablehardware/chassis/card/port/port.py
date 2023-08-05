from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Port(Base):
	"""
	"""

	_SDM_NAME = 'port'

	def __init__(self, parent):
		super(Port, self).__init__(parent)

	def TapSettings(self):
		"""Gets child instances of TapSettings from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of TapSettings will be returned.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.port.tapsettings.tapsettings.TapSettings))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.port.tapsettings.tapsettings import TapSettings
		return self._select(TapSettings(self), locals())

	@property
	def Description(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('description')

	@property
	def IsAvailable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isAvailable')

	@property
	def IsBusy(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isBusy')

	@property
	def IsLinkUp(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isLinkUp')

	@property
	def IsUsable(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('isUsable')

	@property
	def Owner(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('owner')

	@property
	def PortId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('portId')

	def CopyTapSettings(self, Arg2):
		"""Executes the copyTapSettings operation on the server.

		It will copy the values from a port to the given ports.

		Args:
			Arg2 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('copyTapSettings', payload=locals(), response_object=None)
