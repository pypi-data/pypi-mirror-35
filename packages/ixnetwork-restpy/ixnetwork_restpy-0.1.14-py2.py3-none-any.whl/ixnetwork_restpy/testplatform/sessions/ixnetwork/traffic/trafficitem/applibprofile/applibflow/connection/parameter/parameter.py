from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Parameter(Base):
	"""
	"""

	_SDM_NAME = 'parameter'

	def __init__(self, parent):
		super(Parameter, self).__init__(parent)

	def Bool(self, Default=None, Value=None):
		"""Gets child instances of Bool from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Bool will be returned.

		Args:
			Default (bool): (Read only) Parameter default value.
			Value (bool): Parameter bool value.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.bool.bool.Bool))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.bool.bool import Bool
		return self._select(Bool(self), locals())

	def Choice(self, Default=None, Value=None):
		"""Gets child instances of Choice from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Choice will be returned.

		Args:
			Default (str): (Read only) Parameter choice default value.
			Value (str): Parameter choice selected value.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.choice.choice.Choice))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.choice.choice import Choice
		return self._select(Choice(self), locals())

	def Hex(self, Default=None, Value=None):
		"""Gets child instances of Hex from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Hex will be returned.

		Args:
			Default (str): (Read only) Parameter default value.
			Value (str): Parameter hex value.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.hex.hex.Hex))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.hex.hex import Hex
		return self._select(Hex(self), locals())

	def Number(self, Default=None, MaxValue=None, MinValue=None, Value=None):
		"""Gets child instances of Number from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Number will be returned.

		Args:
			Default (number): (Read only) Parameter default value.
			MaxValue (number): (Read only) Maximum supported value for parameter.
			MinValue (number): (Read only) Minimum supported value for parameter.
			Value (number): Parameter integer value.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.number.number.Number))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.number.number import Number
		return self._select(Number(self), locals())

	def Range(self, From=None, MaxValue=None, MinValue=None, To=None):
		"""Gets child instances of Range from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Range will be returned.

		Args:
			From (number): Start range value.
			MaxValue (number): (Read only) Maximum supported value for parameter range.
			MinValue (number): (Read only) Minimum supported value for parameter range.
			To (number): End range value.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.range.range.Range))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.range.range import Range
		return self._select(Range(self), locals())

	def String(self, Default=None, Value=None):
		"""Gets child instances of String from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of String will be returned.

		Args:
			Default (str): (Read only) Parameter default value.
			Value (str): Parameter string value.

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.string.string.String))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.applibprofile.applibflow.connection.parameter.string.string import String
		return self._select(String(self), locals())

	@property
	def DisplayValue(self):
		"""Current parameter UI Display Value

		Returns:
			str
		"""
		return self._get_attribute('displayValue')

	@property
	def Option(self):
		"""Each parameter has one or multiple options. Runtime supported options for specific parameter can be retrieved from supportedOptions attribute

		Returns:
			str(choice|range|value)
		"""
		return self._get_attribute('option')
	@Option.setter
	def Option(self, value):
		self._set_attribute('option', value)

	@property
	def SupportedOptions(self):
		"""Runtime supported options for a specific parameter

		Returns:
			list(str[choice|range|value])
		"""
		return self._get_attribute('supportedOptions')
