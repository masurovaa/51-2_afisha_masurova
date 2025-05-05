from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from .serializers import FilmListSerializer, FilmDetailSerializer


@api_view(['GET'])
def film_detail_api_view(request, id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = FilmDetailSerializer(film, many=False).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def film_list_api_view(request):
    
    #step 1: Получить (Queryset)
    films = Film.objects.filter(is_active=True)
    
    #step 2: Переформотировать (Serialize)
    data = FilmListSerializer(instance=films, many=True).data

    #step 3: Отдать в виде Response
    return Response(data=data, status = status.HTTP_200_OK)  # data = list / dict / list of dict
