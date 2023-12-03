from django.urls import path

from . import views

app_name = "mkt_item"


urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
    path("new/", views.new_mkt_item, name="new"),
]