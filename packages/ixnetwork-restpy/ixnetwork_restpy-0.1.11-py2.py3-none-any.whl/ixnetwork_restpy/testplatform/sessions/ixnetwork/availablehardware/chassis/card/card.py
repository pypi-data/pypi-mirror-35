from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Card(Base):
	"""
	"""

	_SDM_NAME = 'card'

	def __init__(self, parent):
		super(Card, self).__init__(parent)

	def Aggregation(self, ActivePort=None, Mode=None):
		"""Gets child instances of Aggregation from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Aggregation will be returned.

		Args:
			ActivePort (str(None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port)): 
			Mode (str(atlasEightByFiftyGigFanOut|atlasFourByOneHundredGigFanOut|atlasOneByFourHundredGigNonFanOut|atlasTwoByTwoHundredGigNonFanOut|dualMode|eightByTenGigFanOut|fortyGig|fortyGigCapturePlayback|fortyGigFanOut|fortyGigNonFanOut|fourByTenGigFanOut|fourByTwentyFiveGigNonFanOut|hundredGigCapturePlayback|hundredGigNonFanOut|incompatibleMode|krakenFourByFiftyGigFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|normal|novusFourByTenGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusHundredGigNonFanOut|novusOneByFortyGigNonFanOut|novusTwoByFiftyGigNonFanOut|oneByFiftyGigNonFanOut|oneByTenGigFanOut|singleMode|tenGig|threeByTenGigFanOut|twoByTwentyFiveGigNonFanOut)): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.aggregation.aggregation.Aggregation))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.aggregation.aggregation import Aggregation
		return self._select(Aggregation(self), locals())

	def Port(self, Description=None, IsAvailable=None, IsBusy=None, IsLinkUp=None, IsUsable=None, Owner=None, PortId=None):
		"""Gets child instances of Port from the server.

		Use the named parameters as selection criteria to find specific instances.
		All named parameters support regex.
		If no named parameters are specified then all instances of Port will be returned.

		Args:
			Description (str): 
			IsAvailable (bool): 
			IsBusy (bool): 
			IsLinkUp (bool): 
			IsUsable (bool): 
			Owner (str): 
			PortId (number): 

		Returns:
			list(obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.port.port.Port))

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.card.port.port import Port
		return self._select(Port(self), locals())

	def ClearOwnership(self, Arg1):
		"""Executes the clearOwnership operation on the server.

		Clears ownership on a list of hardware ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): An array of valid ports references.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('clearOwnership', child='port', payload=locals(), response_object=None)

	def DeleteCustomDefaults(self, Arg1):
		"""Executes the deleteCustomDefaults operation on the server.

		It will delete custom defaults for the given ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('deleteCustomDefaults', child='port', payload=locals(), response_object=None)

	def GetTapSettings(self, Arg1):
		"""Executes the getTapSettings operation on the server.

		Get TAP Settings for the given ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('getTapSettings', child='port', payload=locals(), response_object=None)

	def RestoreCustomDefaults(self, Arg1):
		"""Executes the restoreCustomDefaults operation on the server.

		It will restore custom defaults for the given ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restoreCustomDefaults', child='port', payload=locals(), response_object=None)

	def RestoreDefaults(self, Arg1):
		"""Executes the restoreDefaults operation on the server.

		Restore de default values for the given ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('restoreDefaults', child='port', payload=locals(), response_object=None)

	def SaveCustomDefaults(self, Arg1):
		"""Executes the saveCustomDefaults operation on the server.

		It will save custom defaults for the given ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('saveCustomDefaults', child='port', payload=locals(), response_object=None)

	def SetTapSettings(self, Arg1):
		"""Executes the setTapSettings operation on the server.

		Send TAP Settings to IxServer for the given ports.

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/availableHardware?deepchild=port])): 

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._execute('setTapSettings', child='port', payload=locals(), response_object=None)

	@property
	def AggregationMode(self):
		"""

		Returns:
			str(atlasEightByFiftyGigFanOut|atlasFourByOneHundredGigFanOut|atlasOneByFourHundredGigNonFanOut|atlasTwoByTwoHundredGigNonFanOut|dualMode|eightByTenGigFanOut|fortyGigAggregation|fortyGigCapturePlayback|fortyGigFanOut|fortyGigNonFanOut|fourByTenGigFanOut|fourByTwentyFiveGigNonFanOut|hundredGigCapturePlayback|hundredGigNonFanOut|incompatibleMode|krakenFourByFiftyGigFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|mixed|normal|notSupported|novusFourByTenGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusHundredGigNonFanOut|novusOneByFortyGigNonFanOut|novusTwoByFiftyGigNonFanOut|oneByFiftyGigNonFanOut|oneByTenGigFanOut|singleMode|tenGigAggregation|threeByTenGigFanOut|twoByTwentyFiveGigNonFanOut)
		"""
		return self._get_attribute('aggregationMode')
	@AggregationMode.setter
	def AggregationMode(self, value):
		self._set_attribute('aggregationMode', value)

	@property
	def AggregationSupported(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('aggregationSupported')

	@property
	def AvailableModes(self):
		"""

		Returns:
			list(str[atlasEightByFiftyGigFanOut|atlasFourByOneHundredGigFanOut|atlasOneByFourHundredGigNonFanOut|atlasTwoByTwoHundredGigNonFanOut|dualMode|eightByTenGigFanOut|fortyGigAggregation|fortyGigCapturePlayback|fortyGigFanOut|fortyGigNonFanOut|fourByTenGigFanOut|fourByTwentyFiveGigNonFanOut|hundredGigCapturePlayback|hundredGigNonFanOut|incompatibleMode|krakenFourByFiftyGigFanOut|krakenOneByFourHundredGigNonFanOut|krakenOneByTwoHundredGigNonFanOut|krakenTwoByOneHundredGigFanOut|mixed|normal|notSupported|novusFourByTenGigNonFanOut|novusFourByTwentyFiveGigNonFanOut|novusHundredGigNonFanOut|novusOneByFortyGigNonFanOut|novusTwoByFiftyGigNonFanOut|oneByFiftyGigNonFanOut|oneByTenGigFanOut|singleMode|tenGigAggregation|threeByTenGigFanOut|twoByTwentyFiveGigNonFanOut])
		"""
		return self._get_attribute('availableModes')

	@property
	def CardId(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('cardId')

	@property
	def Description(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('description')
