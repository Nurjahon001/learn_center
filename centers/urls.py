from .views import CenterListDetailUpdateDeleteAPIView,CenterReviewDetailUpdateDeleteAPIView,CenterList,CenterDetailView
from django.urls import path

app_name = 'centers'


urlpatterns = [
    path('centers-list', CenterListDetailUpdateDeleteAPIView.as_view()),
    path('centers-list/<int:pk>/', CenterReviewDetailUpdateDeleteAPIView.as_view()),

    path('',CenterList.as_view(), name='centers-list'),
    path('<int:pk>/centers-detail/', CenterDetailView.as_view(), name='centers-detail'),

]
