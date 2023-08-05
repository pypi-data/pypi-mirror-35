from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Lag(Base):
	"""Represents a Ixia port in CPF framework
	"""

	_SDM_NAME = 'lag'

	def __init__(self, parent):
		super(Lag, self).__init__(parent)

	def ProtocolStack(self, Count=None, DescriptiveName=None, Enabled=None, Multiplier=None, Name=None, Status=None):
		"""Gets child instances of ProtocolStack from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of ProtocolStack will be returned.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Enabled (obj(ixnetwork_restpy.multivalue.Multivalue)): Enables/disables device.
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario
			Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.protocolstack.ProtocolStack))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.protocolstack import ProtocolStack
		return self._select(ProtocolStack(self), locals())

	def add_ProtocolStack(self, Multiplier="1", Name=None):
		"""Adds a child instance of ProtocolStack on the server.

		Args:
			Multiplier (number): Number of device instances per parent device instance (multiplier)
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.protocolstack.ProtocolStack)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.lag.protocolstack import ProtocolStack
		return self._create(ProtocolStack(self), locals())

	def RestartDown(self, Targets):
		"""Executes the restartDown operation on the server.

		Stop and start interfaces and sessions in Device Group that are in 'Down' state.

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./protocolStack object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restartDown', child='protocolStack', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./protocolStack object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='protocolStack', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/lag])): This parameter requires a list of /lag/./protocolStack object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='protocolStack', payload=locals(), response_object=None)

	@property
	def AggregationStatus(self):
		"""aggregation status of LAG

		Returns:
			str(all|none|some|unconfigured)
		"""
		return self._get_attribute('aggregationStatus')

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
	def Vports(self):
		"""Virtual port information.

		Returns:
			list(str[None|/api/v1/sessions/1/ixnetwork/vport])
		"""
		return self._get_attribute('vports')
	@Vports.setter
	def Vports(self, value):
		self._set_attribute('vports', value)

	def remove(self):
		"""Deletes a child instance of Lag on the server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()
