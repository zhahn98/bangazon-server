from bangazonapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']
   
    user = User.objects.filter(uid=uid).first()

    
    if user is not None:
        data = {
            'id': user.id,
            'uid': user.uid
        }
        return Response(data)
    else:
        
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new rare_user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    
    user = User.objects.create(
        uid=request.data['uid']
    )
    
    data = {
        'id': user.id,
        'uid': user.uid
    }
    return Response(data)
