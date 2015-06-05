#:coding=utf-8:

from django.test import TestCase as DjangoTestCase
# from django.utils.encoding import force_text

from jsonfield2.tests.jsonfield_test_app.models import QueryJsonModel

class QJsonModelTest(DjangoTestCase):

    def setUp(self):

        data = [
            {"status": "A", "code": "lion", "info": "{}"},
            {"status": "0", "code": "cat", "info": "{}"},

            {"status": "A", "code": "Vito", "info": "{\"especie\": \"can\", \"sexo\": \"M\"}"},
            {"status": "0", "code": "Napa", "info": "{\"especie\": \"can\", \"sexo\": \"F\"}"}, 

            {"status": "A", "code": "Dario", "info": "{\"especie\": \"human\", \"sexo\": \"M\"}"},
            {"status": "A", "code": "Andrea", "info": "{\"especie\": \"human\", \"sexo\": \"F\"}"},
            {"status": "0", "code": "Xatli", "info": "{\"especie\": \"human\", \"sexo\": \"F\"}"}, 
        ]

        for reg in data:
            QueryJsonModel.objects.create(**reg)


    def test_q_nojson(self):
        rs = QueryJsonModel.objects.filter( status = 'A', info__icontains = 'human')    
        self.assertEqual(rs.count(), 2)

    def test_q_only_data(self):
        rs = QueryJsonModel.objects.filter( status = 'A')    
        self.assertEqual(rs.count(), 4)

    def test_q_only_json(self):
        rs = QueryJsonModel.objects.filter( info__especie = 'human')    
        self.assertEqual(rs.count(), 3)

    def test_q_data_json(self):
        rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human')    
        self.assertEqual(rs.count(), 2)

    def test_q_data_json2(self):
        rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human', info__sexo = 'M')
        self.assertEqual(rs.count(), 1)

    def test_s_only_data(self):
        rs = QueryJsonModel.objects.filter( status = 'A').order_by('code')
        self.assertEqual(rs.count(), 4)

    def test_s_only_json(self):
        rs = QueryJsonModel.objects.filter( info__especie = 'human').order_by('code')    
        self.assertEqual(rs.count(), 3)

    def test_s_data_json(self):
        rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human').order_by('code')    
        self.assertEqual(rs.count(), 2)

    def test_s_data_json2(self):
        rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human', info__sexo = 'M').order_by('code')
        self.assertEqual(rs.count(), 1)




