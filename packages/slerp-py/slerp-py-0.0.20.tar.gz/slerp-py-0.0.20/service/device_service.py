from slerp.validator import Key, Number, Blank
from slerp.logger import logging
from slerp.app import db

from entity.models import Device


log = logging.getLogger(__name__)


class DeviceService(object):
	def __init__(self):
		super(DeviceService, self).__init__()

	@Key(['user_id', 'manufactured', 'product', 'model', 'token'])
	def add_device(self, domain):
		device = Device(domain)
		device.save()
		return {'payload': device.to_dict()}