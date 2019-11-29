from django.shortcuts import render
from moviesinfo.models import *
from moviesinfo.serializers import *
from rest_framework.viewsets import ModelViewSet,GenericViewSet
import json
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from rest_framework_swagger import renderers
from rest_framework.decorators import api_view,renderer_classes


# Create your views here.
def verify_manditory_fields(data):
    manditoryfields=['movieid','actorid']
    notavlfields=[]
    for item in manditoryfields:
        if not data.__contains__(item):
            notavlfields.append(item)
    if len(notavlfields)==0:
        return True
    return notavlfields

@api_view(['POST'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def assign_movie_to_actors(req):
    print('inside getallmovies')
    print('inside assign',req.data)
    result = verify_manditory_fields(req.data)
    if result==True:
        movieId= req.data.get("movieid")
        actorId = req.data.get("actorid")
        mvinstance = Movie.objects.get(id=movieId)
        for actid in actorId:
            mvact = MovieActor(movie=mvinstance,actor=Actor.objects.get(id=actid))
            mvact.save()
        return HttpResponse("Success")

    return HttpResponse(json.dumps(result))


@api_view(['GET',"POST"])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def get_allmovies_of_actors(req):
    print('inside getallmovies')
    allmovieactorsinfo = MovieActor.objects.all()
    moviesList = []
    for movieinfo in allmovieactorsinfo:#1 111  991
        if movieinfo.actor.id==req.data["id"]:
            #instance = Movie.objects.get(id=movieinfo.movie.id)
            instance = movieinfo.movie
            instance.__dict__.pop('_state')
            moviesList.append(instance.__dict__)
    print(moviesList)
    return HttpResponse(json.dumps(moviesList), content_type='application/json')



@api_view(['GET',"POST"])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def get_movie_actors(req):
    allmovieactorsinfo = MovieActor.objects.all()
    actorsList = []
    for movieinfo in allmovieactorsinfo:#1 111  991
        if movieinfo.movie.id==req.data["id"]:
            #instance = Actor.objects.get(id=movieinfo.actor.id)
            instance = movieinfo.actor
            instance.__dict__.pop('_state')
            actorsList.append(instance.__dict__)
    print(actorsList)
    return HttpResponse(json.dumps(actorsList), content_type='application/json')

    return HttpResponse("This is get actor based on movies")

class MovieViewset(ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer

class ActorViewset(ModelViewSet):
    queryset=Actor.objects.all()
    serializer_class = ActorSerializer