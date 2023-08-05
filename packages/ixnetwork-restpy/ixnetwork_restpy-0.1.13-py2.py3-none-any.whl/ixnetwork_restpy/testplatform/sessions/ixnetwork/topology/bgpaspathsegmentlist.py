from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class BgpAsPathSegmentList(Base):
	"""Bgp Non VPN RR AS Path segments
	"""

	_SDM_NAME = 'bgpAsPathSegmentList'

	def __init__(self, parent):
		super(BgpAsPathSegmentList, self).__init__(parent)

	def BgpAsNumberList(self, AsNumber=None, Count=None, DescriptiveName=None, EnableASNumber=None, Name=None):
		"""Gets child instances of BgpAsNumberList from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of BgpAsNumberList will be returned.

		Args:
			AsNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): AS#
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			EnableASNumber (obj(ixnetwork_restpy.multivalue.Multivalue)): Enable AS Number
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpasnumberlist.BgpAsNumberList))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bgpasnumberlist import BgpAsNumberList
		return self._select(BgpAsNumberList(self), locals())

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
	def EnableASPathSegment(self):
		"""Enable AS Path Segment

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('enableASPathSegment')

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
	def NumberOfAsNumberInSegment(self):
		"""Number of AS Number In Segment

		Returns:
			number
		"""
		return self._get_attribute('numberOfAsNumberInSegment')
	@NumberOfAsNumberInSegment.setter
	def NumberOfAsNumberInSegment(self, value):
		self._set_attribute('numberOfAsNumberInSegment', value)

	@property
	def SegmentType(self):
		"""SegmentType

		Returns:
			obj(ixnetwork_restpy.multivalue.Multivalue)
		"""
		return self._get_attribute('segmentType')

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
