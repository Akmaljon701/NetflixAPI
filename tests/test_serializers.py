from film.serializers import *
from unittest import TestCase

class TestAktyorSerializer(TestCase):
    def test_aktyor(self):
        aktyor = {
            "id": 3,
            "ism": "Abdulla Sarvarov",
            "davlat": "O'zbekiston",
            "tugilgan_yil": "1972-09-24",
            "jins": "Erkak"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == True
        # self.assertTrue(serializer.is_valid() == True)
        # self.assertEqual(serializer.is_valid() == True)

        malumot = serializer.validated_data
        assert malumot['ism'] == 'Abdulla Sarvarov'

    def test_invalid_ism(self):
        aktyor = {
            "id": 3,
            "ism": "Ab",
            "davlat": "O'zbekiston",
            "tugilgan_yil": "1972-09-24",
            "jins": "Erkak"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == False
        assert serializer.errors['ism'][0] == "Ism bunaqa kalta bo'lishi mumkin emas!"
        print(serializer.errors)

    def test_invalid_jins(self):
        aktyor = {
            "id": 3,
            "ism": "Abdulla Sarvarov",
            "davlat": "O'zbekiston",
            "tugilgan_yil": "1972-09-24",
            "jins": "Yigit"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == False
        assert serializer.errors['jins'][0] == "Bunday jins bo'lishi mumkin emas!"
        print(serializer.errors)

class TestKinoSerializer(TestCase):
    def test_kino(self):
        kino = {
            "id": 2,
            "nom": "Sotqin",
            "janr": "Action",
            "yil": "2018-11-11",
            "aktyorlar": [1, 2]
        }
        serializer = KinoCreateSerializer(data=kino)
        assert serializer.is_valid() == True
        assert serializer.validated_data['nom'] == "Sotqin"

