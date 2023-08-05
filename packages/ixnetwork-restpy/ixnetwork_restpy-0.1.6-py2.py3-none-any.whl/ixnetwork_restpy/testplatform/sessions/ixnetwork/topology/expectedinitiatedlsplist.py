from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ExpectedInitiatedLspList(Base):
	"""This specifies the Expected Initiated LSPs from the PCE for traffic generation.
	"""

	_SDM_NAME = 'expectedInitiatedLspList'

	def __init__(self, parent):
		super(ExpectedInitiatedLspList, self).__init__(parent)

	def Tag(self, __id__=None, Count=None, Enabled=None, Name=None):
		"""Gets child instances of Tag from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Tag will be returned.

		Args:
			__id__ (obj(ixnetwork_restpy.multivalue.Multivalue)): the tag ids that this entity will use/publish
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return self._select(Tag(self), locals())

	def add_Tag(self, Enabled="False", Name=None):
		"""Adds a child instance of Tag on the server.

		Args:
			Enabled (bool): Enables/disables tags
			Name (str): specifies the name of the tag the entity will be part of

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag.Tag)

		Raises:
			AlreadyExistsError: The requested resource already exists on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag import Tag
		return self._create(Tag(self), locals())

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
	def InsertIpv6ExplicitNull(self):
		"""Insert IPv6 Explicit Null MPLS header if the traffic type is of type IPv6

		Returns:
			bool
		"""
		return self._get_attribute('insertIpv6ExplicitNull')
	@InsertIpv6ExplicitNull.setter
	def InsertIpv6ExplicitNull(self, value):
		self._set_attribute('insertIpv6ExplicitNull', value)

	@property
	def MaxExpectedSegmentCount(self):
		"""This control is used to set the maximum Segment count/ MPLS labels that would be present in the generted traffic.

		Returns:
			number
		"""
		return self._get_attribute('maxExpectedSegmentCount')
	@MaxExpectedSegmentCount.setter
	def MaxExpectedSegmentCount(self, value):
		self._set_attribute('maxExpectedSegmentCount', value)

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
	def SourceIpv4Address(self):
		"""This is used to set the Source IPv4 address in the IP header of the generated traffic.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIpv4Address')

	@property
	def SourceIpv6Address(self):
		"""This is used to set the Source IPv6 address in the IP header of the generated traffic.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('sourceIpv6Address')

	@property
	def SymbolicPathName(self):
		"""This is used for generating the traffic for those LSPs from PCE for which the Symbolic Path Name is configured and matches the value.

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('symbolicPathName')

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
