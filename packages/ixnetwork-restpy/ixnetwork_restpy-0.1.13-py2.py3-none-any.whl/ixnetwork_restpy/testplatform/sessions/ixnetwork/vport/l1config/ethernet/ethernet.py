from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ethernet(Base):
	"""
	"""

	_SDM_NAME = 'ethernet'

	def __init__(self, parent):
		super(Ethernet, self).__init__(parent)

	@property
	def Fcoe(self):
		"""Returns the one and only one Fcoe object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.fcoe.fcoe.Fcoe)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.fcoe.fcoe import Fcoe
		return self._read(Fcoe(self), None)

	@property
	def Oam(self):
		"""Returns the one and only one Oam object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.oam.oam.Oam)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.oam.oam import Oam
		return self._read(Oam(self), None)

	@property
	def TxLane(self):
		"""Returns the one and only one TxLane object from the server.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.txlane.txlane.TxLane)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.txlane.txlane import TxLane
		return self._read(TxLane(self), None)

	@property
	def AutoInstrumentation(self):
		"""

		Returns:
			str(endOfFrame|floating)
		"""
		return self._get_attribute('autoInstrumentation')
	@AutoInstrumentation.setter
	def AutoInstrumentation(self, value):
		self._set_attribute('autoInstrumentation', value)

	@property
	def AutoNegotiate(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('autoNegotiate')
	@AutoNegotiate.setter
	def AutoNegotiate(self, value):
		self._set_attribute('autoNegotiate', value)

	@property
	def EnablePPM(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enablePPM')
	@EnablePPM.setter
	def EnablePPM(self, value):
		self._set_attribute('enablePPM', value)

	@property
	def EnabledFlowControl(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabledFlowControl')
	@EnabledFlowControl.setter
	def EnabledFlowControl(self, value):
		self._set_attribute('enabledFlowControl', value)

	@property
	def FlowControlDirectedAddress(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('flowControlDirectedAddress')
	@FlowControlDirectedAddress.setter
	def FlowControlDirectedAddress(self, value):
		self._set_attribute('flowControlDirectedAddress', value)

	@property
	def Loopback(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('loopback')
	@Loopback.setter
	def Loopback(self, value):
		self._set_attribute('loopback', value)

	@property
	def MasterSlaveMode(self):
		"""

		Returns:
			str(master|slave)
		"""
		return self._get_attribute('masterSlaveMode')
	@MasterSlaveMode.setter
	def MasterSlaveMode(self, value):
		self._set_attribute('masterSlaveMode', value)

	@property
	def Media(self):
		"""

		Returns:
			str(copper|fiber|sgmii)
		"""
		return self._get_attribute('media')
	@Media.setter
	def Media(self, value):
		self._set_attribute('media', value)

	@property
	def NegotiateMasterSlave(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('negotiateMasterSlave')
	@NegotiateMasterSlave.setter
	def NegotiateMasterSlave(self, value):
		self._set_attribute('negotiateMasterSlave', value)

	@property
	def Ppm(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('ppm')
	@Ppm.setter
	def Ppm(self, value):
		self._set_attribute('ppm', value)

	@property
	def Speed(self):
		"""

		Returns:
			str(auto|speed1000|speed100fd|speed100hd|speed10fd|speed10hd)
		"""
		return self._get_attribute('speed')
	@Speed.setter
	def Speed(self, value):
		self._set_attribute('speed', value)

	@property
	def SpeedAuto(self):
		"""

		Returns:
			list(str[all|speed1000|speed100fd|speed100hd|speed10fd|speed10hd])
		"""
		return self._get_attribute('speedAuto')
	@SpeedAuto.setter
	def SpeedAuto(self, value):
		self._set_attribute('speedAuto', value)
