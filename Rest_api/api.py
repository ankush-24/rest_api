from rest_framework import routers
from drf_user import views
# from user import views

router = routers.DefaultRouter()
router.register(r'user',views.UserViewset,basename='user')

