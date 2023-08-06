from slerp.validator import Key, Number, Blank
from slerp.logger import logging
from slerp.app import db

from entity.models import Address


log = logging.getLogger(__name__)


class AddressService(object):
	def __init__(self):
		super(AddressService, self).__init__()

	@Key(['address', 'latitude', 'longitude'])
	def add_address(self, domain):
		address = Address(domain)
		address.save()
		return {'payload': address.to_dict()}