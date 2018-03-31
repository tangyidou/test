from mobile10mins.models import UserInfo
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication

class UserInfoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1,required=False)
    password = serializers.CharField(min_length=6,required=False)
    email = serializers.CharField(min_length=8,required=False)
    class Meta:
        model = UserInfo
        fields = '__all__'



@api_view(['GET','POST'])
@authentication_classes((TokenAuthentication,))
def userinfo(request):
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        userinfo_list = UserInfo.objects.order_by('-id')
        if request.auth:
            serializer = UserInfoSerializer(userinfo_list, many=True)
            return Response(serializer.data)
        else:
            serializer = UserInfoSerializer(userinfo_list[:0], many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        body = {
            'body': serializer.errors,
            'msg': '40001'
        }
        return Response(serializer.body, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@authentication_classes((TokenAuthentication,))
def useraction(request, id):
    useraction = UserInfo.objects.get(id=id)
    if request.method == 'PUT':
        serializer = UserInfoSerializer(useraction, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = UserInfoSerializer(useraction)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        useraction.delete()
        return Response({'msg':'M-OK'}, status=status.HTTP_201_CREATED)
