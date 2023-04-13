from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

class HelloAPI(APIView):
    def get(self, request):
        content = {
            'xabar': 'Salom. Dunyo!'
        }
        return Response(content)

    def post(self, request):
        data = request.data
        content = {
            "xabar": "Post so'rov qabul qilindi!",
            "malumot": data
        }
        return Response(content)

# class AktyorlarAPIView(APIView):
#     def get(self, request):
#         akytorlar = Aktyor.objects.all()
#         serializer = AktyorSerializer(akytorlar, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#         aktyor = request.data
#         serializer = AktyorSerializer(data=aktyor)
#         if serializer.is_valid():
#             Aktyor.objects.create(
#                 ism=serializer.validated_data.get('ism'),
#                 davlat=serializer.validated_data.get('davlat'),
#                 jins=serializer.validated_data.get('jins'),
#                 tugilgan_yil=serializer.validated_data.get('tugilgan_yil'),
#             )
#             content = {
#                 "success": "True",
#                 "ma'lumot": serializer.data
#             }
#             return Response(content)
#         return Response({"succes":"False", "xatolik": serializer.errors})
#
# class AktyorAPIView(APIView):
#     def get(self, request, pk):
#         a1 = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(a1)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         ser = AktyorSerializer(aktyor, data=request.data)
#         if ser.is_valid():
#             aktyor.ism = ser.validated_data.get('ism')
#             aktyor.davlat = ser.validated_data.get('davlat')
#             aktyor.jins = ser.validated_data.get('jins')
#             aktyor.tugilgan_yil = ser.validated_data.get('tugilgan_yil')
#             aktyor.save()
#             return Response(ser.data, status=status.HTTP_202_ACCEPTED)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         aktyor = Aktyor.objects.filter(id=pk)
#         if aktyor:
#             aktyor.delete()
#             return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

class AktyorlarViewSet(ModelViewSet):
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSerializer

    filter_backends =[filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ism']
    ordering_fields = ['tugilgan_yil']

class TariflarAPIView(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializer(tariflar, many=True)

        return Response(serializer.data)

    def post(self, request):
        tarif = request.data
        serializer = TarifSerializer(data=tarif)
        if serializer.is_valid():
            Tarif.objects.create(
                nom=serializer.validated_data.get('nom'),
                muddat=serializer.validated_data.get('muddat'),
                narx=serializer.validated_data.get('narx'),
            )
            return Response({"succes": "True", "ma'lumot": serializer.data})
        return Response({"succes": "False", "xatolik": serializer.errors})

class TarifAPIView(APIView):
    def get(self, request, pk):
        t1 = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(t1)
        return Response(serializer.data)

    def put(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif, data=request.data)
        if serializer.is_valid():
            tarif.nom = serializer.validated_data.get('nom')
            tarif.muddat = serializer.validated_data.get('muddat')
            tarif.narx = serializer.validated_data.get('narx')
            tarif.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarif = Tarif.objects.filter(id=pk)
        if tarif:
            tarif.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# class KinolarAPIView(APIView):
#     def get(self, request):
#         kinolar = Kino.objects.all()
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = KinoCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class KinoAPIView(APIView):
#     def get(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         serializer = KinoSerializer(kino)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         serializer = KinoCreateSerializer(kino, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

class KinolarViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom']
    ordering_fields = ['yil']

class IzohlarViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer

    def get_queryset(self):
        queryset = Izoh.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()