import uuid
from mock.constants import DEFAULT_STATUS


def return_transaction(data):
    return {
        'brinkspayTransactionId': data['brinkspayTransactionId'],
        'partnerTransactionId': data['externalIdentifier'],#data['storeId'] + data['collectorId'] + data['partnerId'],
        'status': DEFAULT_STATUS['partner_transaction']
        }
