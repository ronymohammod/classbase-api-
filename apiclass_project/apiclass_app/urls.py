from django.urls import path
from apiclass_app.views import *


urlpatterns = [
       path('blogs/', BlogAPIview.as_view()),
       path('blog-detail/<str:id>/', BlogDetail.as_view()),
]