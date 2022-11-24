import base64
import time
import hmac
import hashlib

from .models import Merchant


def b64_encode(message: str, cp: str = 'utf-8'):
    message_bytes = message.encode(cp)
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode(cp)
    return base64_message


def b64_decode(b64_message: str, cp: str = 'utf-8'):
    b64_message_bytes = b64_message.encode(cp)
    message_bytes = base64.b64decode(b64_message_bytes)
    message = message_bytes.decode(cp)
    return message


def hash_sha1(key: str, message: str, cp: str = 'utf-8'):
    # https://www.adamsmith.haus/python/examples/1953/hmac-construct-a-new-hmac-hash-using-the-sha1-algorithm
    
    h = hmac.new(key.encode(cp), msg=message.encode(cp), digestmod=hashlib.sha1)
    return h.hexdigest()

    

def prepare_payment(dic: dict):
    
    if not dic['INVOICE'].isdigit():
        raise Exception("Номерът на фактурата трябва да е само от цифри.")
    merchant = Merchant.objects.get(min=dic['MIN'])
    secret = merchant.secret
    
    exp_time = ''
    if 'sec' in dic and dic['sec'] != '':
        seconds = time.time()
        s2 = seconds + int(dic['sec'])
        st = time.localtime(s2)
        exp_time = time.strftime("%d.%m.%Y %H:%M:%S", st)
        
    if 'untilTime' in dic and dic['untilTime'] != '':
        exp_time = dic['untilTime']

    if exp_time == '':
        raise Exception('Не е зададвно време на валидност.')
    
    s = f'''MIN={dic['MIN']}
INVOICE={dic['INVOICE']}
AMOUNT={dic['AMOUNT']}
EXP_TIME={exp_time}
DESCR={dic['DESCR']}
ENCODING=utf-8
'''

    encoded = b64_encode(s)
    check_sum = hash_sha1(secret, encoded)
    
    dc: dict = {
        'ENCODED':  encoded,
        'CHECKSUM': check_sum
    }
    
    return dc
