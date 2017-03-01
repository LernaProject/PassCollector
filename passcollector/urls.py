from django.conf.urls import url

from main.views import index, collect


urlpatterns = [
    url(r"^$", index),
    url(r"^(?P<user_id>\d+)$", collect),
]
