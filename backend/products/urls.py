from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductAPIView.as_view()),
    path('<int:pk>/',views.ProductDetailView.as_view()),
    path('<int:pk>/update/',views.ProductUpdateView.as_view()),
    path('<int:pk>/delete/',views.ProductDeleteView.as_view())
]
