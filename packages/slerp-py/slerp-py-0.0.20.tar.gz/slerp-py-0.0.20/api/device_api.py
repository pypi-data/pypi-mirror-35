from flask import Blueprint, request
from slerp.logger import logging

from service.device_service import DeviceService

log = logging.getLogger(__name__)

device_api_blue_print = Blueprint('device_api_blue_print', __name__)
api = device_api_blue_print
device_service = DeviceService()


@api.route('/add_device', methods=['POST'])
def add_device():
    """
    {
    "user_id": "Long",
    "manufactured": "String",
    "product": "String",
    "model": "String",
    "token": "String"
    }
    """
    domain = request.get_json()
    return device_service.add_device(domain)