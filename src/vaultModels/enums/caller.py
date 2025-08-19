from enum import IntEnum

class Caller(IntEnum):
    CLOUDGAME = 100
    IOSSERVER = 200
    COMMONCORN = 300
    TENANT_SERVICE = 400
    EXTERNAL_SERVICE = 500
    RAZORPAY = 600
