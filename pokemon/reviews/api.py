from rest_framework import parsers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import requests
import json

@api_view()
def collection_evolution_chain(request):
    r"""
    Evolution chains are essentially family trees. They start with the lowest stage within a family 
    and detail evolution conditions for each as well as Pokémon they can evolve into up through the hierarchy.
    """

    r = requests.get('https://pokeapi.co/api/v2/evolution-chain/')
    data = r.json()

    return Response(data)

@api_view()
def resource_evolution_chain(request, id):
    r"""
    Evolution chains are essentially family trees. They start with the lowest stage within a family 
    and detail evolution conditions for each as well as Pokémon they can evolve into up through the hierarchy.
    """
    print("Request: {}".format(id))
    r = requests.get('https://pokeapi.co/api/v2/evolution-chain/{}'.format(id))
    data = r.json()

    return Response(data)