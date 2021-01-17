from django.conf.urls import url, include
from users import views


urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", views.dashboard, name="dashboard"),
]

