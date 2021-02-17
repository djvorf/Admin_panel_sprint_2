from django.urls import include
from django.urls import path

urlpatterns = [
    path('v1/', include('movie.api.v1.urls'))
]
