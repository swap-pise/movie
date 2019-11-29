from rest_framework.routers import SimpleRouter
from moviesinfo.views import *

routerInstance = SimpleRouter()
routerInstance.register('movies',MovieViewset)
routerInstance.register('actors',ActorViewset)

from django.conf.urls import url

urlpatterns = [
    url('custom/mvactors/', get_movie_actors),
    url('custom/actormvs/', get_allmovies_of_actors),
    url('custom/assign/', assign_movie_to_actors),

]

urlpatterns += routerInstance.urls

