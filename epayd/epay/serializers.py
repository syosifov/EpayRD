from pyexpat import model
from rest_framework import serializers

class EpayRequestSerializer(serializers.Serializer):
    MIN = serializers.CharField()
    INVOICE = serializers.CharField()
    AMOUNT = serializers.CharField()
    EXP_TIME = serializers.CharField()
    DESCR = serializers.CharField()
    ENCODED = serializers.CharField()
    CHECKSUM = serializers.CharField()
    PAGE = serializers.CharField()
    ENCODING = serializers.CharField()
    
    

class ErrorMessageSerializer(serializers.Serializer):
    message = serializers.CharField()


