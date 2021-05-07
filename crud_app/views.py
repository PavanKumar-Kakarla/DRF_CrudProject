from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def person_List(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person,many=True )
    return Response(serializer.data)

@api_view(['GET'])
def person_Detail(request,pk):
    persons = Person.objects.get(id=pk)
    serializer = PersonSerializer(persons,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def person_Create(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def person_Update(request,pk):
    person = Person.objects.get(id=pk)
    serializer = PersonSerializer(instance=person,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def person_Delete(request,pk):
    person = Person.objects.get(id=pk)
    person.delete()
    return Response("Data Successfully deleted!")





