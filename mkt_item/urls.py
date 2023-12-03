from django.urls import path

from . import views

app_name = "mkt_item"


urlpatterns = [
    path("", views.browse, name="browse"),
    path("new/", views.new_mkt_item, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete')
]
