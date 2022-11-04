from django.urls import path
from . import views


# Create your urls here

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.AdvocateList.as_view(), name='advocates'),
    path('advocates/<str:username>', views.AdvocateDetail.as_view()),
    path('companies/', views.company_list, name="company_list"),
    # path('companies/<int:id>', views.company_detail, name='company_detail'),
]
