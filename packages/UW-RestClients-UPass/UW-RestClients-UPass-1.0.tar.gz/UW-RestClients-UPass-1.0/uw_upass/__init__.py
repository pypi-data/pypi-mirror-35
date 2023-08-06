"""
This is the interface for interacting with the UPass service.

"""

from uw_upass.dao import UPass_DAO
from restclients_core.exceptions import DataFailureException
from uw_upass.models import UPassStatus, CURRENT, NOT_CURRENT


DAO = UPass_DAO()


def get_upass_status(netid):
    url = get_upass_url(netid)
    response = DAO.getURL(url, {})

    response_data = str(response.data)
    if response.status != 200:
        raise DataFailureException(url, response.status, response_data)

    if len(response_data) == 0 or\
            not(CURRENT in response_data or NOT_CURRENT in response_data):
        raise Exception("%s Unexpected Response Data: %s" %
                        (url, response_data))

    status = UPassStatus.create(response_data)
    return status


def get_upass_url(netid):
    return ("/MyUWUpass/MyUWUpass.aspx?id=%s" % netid)
