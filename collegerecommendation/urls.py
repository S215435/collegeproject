from django.urls import path
from .views import index, recommendation

urlpatterns = [
    # root url for entering user data
    path('', index, name="index"),
    # root url for recommending college based of user entered data
    # path(url_name, view, name="url-name")
    # 
    path('recommendation', recommendation, name="recommendation-page"),
]
