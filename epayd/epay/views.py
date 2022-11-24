from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import prepare_payment


@api_view(['POST'])
def pay(request):          # /epay/pay/
    
    try:
        r = prepare_payment(request.data)
        # raise Exception("Test exception")
    except Exception as e:
        return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(r, status=status.HTTP_201_CREATED)

