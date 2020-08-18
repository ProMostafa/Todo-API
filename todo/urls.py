
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import ListTodoViewSet

router=DefaultRouter()
router.register("ListTodo",ListTodoViewSet)
urlpatterns = [
    path("",include(router.urls))
]
