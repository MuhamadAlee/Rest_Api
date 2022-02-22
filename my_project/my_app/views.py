from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def Helloworld(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data.get("text")})
    return Response({"message": "Hello, world!"})