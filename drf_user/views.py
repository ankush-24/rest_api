from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import viewsets
from drf_user import serializers


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.


class UserViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer  
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly,
 #                          IsOwnerOrReadOnly]
	# @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	# def user(self, request, *args, **kwargs):
	# 	user = self.get_object()
	# 	return Response(user)
	# def perform_create(self, serializer):
	# 	serializer.save(owner=self.request.user)



















# @api_view(['GET', 'POST'])
# def post_collection(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         data = {'text': request.DATA.get('the_post'), 'author': request.user.pk}
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)