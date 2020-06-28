from django.conf.urls import url
from .views import index, new_url

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^new_url/$", new_url, name="new_url"),
]

