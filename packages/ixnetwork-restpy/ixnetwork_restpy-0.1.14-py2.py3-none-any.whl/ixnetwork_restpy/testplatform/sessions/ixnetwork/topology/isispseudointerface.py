from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class IsisPseudoInterface(Base):
	"""Information for Simulated Router Interfaces
	"""

	_SDM_NAME = 'isisPseudoInterface'

	def __init__(self, parent):
		super(IsisPseudoInterface, self).__init__(parent)

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

	def Disconnect(self, Arg1):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisDcePseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint1Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisDcePseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint1Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisDcePseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisDcePseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint1Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisDcePseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint1Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisDcePseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='isisDcePseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='isisDcePseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

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

	def Disconnect(self, Arg1):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisDcePseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint2Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisDcePseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint2Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisDcePseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisDcePseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint2Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisDcePseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint2Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisDcePseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='isisDcePseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisDcePseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='isisDcePseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

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

	def Disconnect(self, Arg1):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisL3PseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint1Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisL3PseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint1Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisL3PseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisL3PseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint1Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisL3PseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint1Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisL3PseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='isisL3PseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='isisL3PseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

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

	def Disconnect(self, Arg1):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisL3PseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint2Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisL3PseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint2Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisL3PseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisL3PseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint2Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisL3PseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint2Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisL3PseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='isisL3PseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisL3PseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='isisL3PseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

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

	def Disconnect(self, Arg1):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisSpbPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint1Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisSpbPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint1Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisSpbPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisSpbPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint1Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisSpbPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint1Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisSpbPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='isisSpbPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='isisSpbPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

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

	def Disconnect(self, Arg1):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisSpbPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint2Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisSpbPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint2Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisSpbPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisSpbPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint2Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisSpbPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint2Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisSpbPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='isisSpbPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisSpbPseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='isisSpbPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

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

	def Disconnect(self, Arg1):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisTrillPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint1Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisTrillPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint1Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisTrillPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisTrillPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint1Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisTrillPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint1Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisTrillPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='isisTrillPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint1Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='isisTrillPseudoIfaceAttPoint1Config', payload=locals(), response_object=None)

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

	def Disconnect(self, Arg1):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisTrillPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint2Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisTrillPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Disconnect(self, Arg1, SessionIndices):
		"""Executes the disconnect operation on the server.

		Disconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint2Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('disconnect', child='isisTrillPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisTrillPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint2Config object references
			SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisTrillPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Reconnect(self, Arg1, SessionIndices):
		"""Executes the reconnect operation on the server.

		Reconnect Simulated Interface

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint2Config object references
			SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('reconnect', child='isisTrillPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Start(self, Targets):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('start', child='isisTrillPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

	def Stop(self, Targets):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Targets (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): This parameter requires a list of /topology/./isisTrillPseudoIfaceAttPoint2Config object references

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('stop', child='isisTrillPseudoIfaceAttPoint2Config', payload=locals(), response_object=None)

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
	def LinkType(self):
		"""Link Type

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('linkType')

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
