from flask import Blueprint, request
from slerp.logger import logging

from service.address_service import AddressService

log = logging.getLogger(__name__)

address_api_blue_print = Blueprint('address_api_blue_print', __name__)
api = address_api_blue_print
address_service = AddressService()


@api.route('/add_address', methods=['POST'])
def add_address():
    """
    {
    "address": "String",
    "latitude": "Long",
    "longitude": "Long"
    }
    """
    domain = request.get_json()
    return address_service.add_address(domain)