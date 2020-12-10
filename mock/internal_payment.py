import uuid, datetime, pytz
from mock.constants import DEFAULT_STATUS

def return_internal_payment():
    return {
        'data': {
            'transactionId': uuid.uuid1(),
            'transactionDate': pytz.utc.localize(datetime.datetime.utcnow()).isoformat()
        }
    }
