from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', view=my_viewHome),
    path('sobre/', view=my_viewAbout),
    path('contato/', view=my_viewContact)
]
