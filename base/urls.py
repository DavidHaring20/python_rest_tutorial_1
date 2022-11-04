from nturl2path import url2pathname
from django.urls import path
from . import views


# Create your urls here

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.AdvocateList.as_view(), name='advocates'),
    # path('advocates/<str:username>', views.advocate_detail),
    path('advocates/<str:username>', views.AdvocateDetail.as_view())
]
