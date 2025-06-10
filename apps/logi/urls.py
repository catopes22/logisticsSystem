from django.urls import path
from .views import RouteListView, RouteDetailView, RouteFromCategory, RouteCreateView, RouteUpdateView

urlpatterns = [
    path('', RouteListView.as_view(), name='home'),
    path('route/create/', RouteCreateView.as_view(), name='route_create'),
    path('route/<str:slug>/update/', RouteUpdateView.as_view(), name='route_update'),
    path('route/<str:slug>/', RouteDetailView.as_view(), name='route_detail'),
    path('category/<str:slug>/', RouteFromCategory.as_view(), name="route_by_category"),

]