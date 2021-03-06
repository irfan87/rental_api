from rest_framework import routers
from rental import views

router = routers.DefaultRouter()
router.register(r'friends', views.FriendViewset)
router.register(r'belongings', views.BelongingViewset)
router.register(r'borrowings', views.BorrowedViewset)

# urlpatterns = router.urls