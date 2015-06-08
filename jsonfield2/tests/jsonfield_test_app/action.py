# -*- coding: utf-8 -*-
import traceback

def doJsonTest(modeladmin, request, queryset):

    from protoLib.models import QueryJsonModel 

    try:

        data = [
            {"status": "A", "code": "lion", "info": "{}"},
            {"status": "0", "code": "cat", "info": "{}"},

            {"status": "A", "code": "Vito", "info": "{\"especie\": \"can\", \"sexo\": \"M\"}"},
            {"status": "0", "code": "Napa", "info": "{\"especie\": \"can\", \"sexo\": \"F\"}"}, 

            {"status": "A", "code": "Dario", "info": "{\"especie\": \"human\", \"sexo\": \"M\"}"},
            {"status": "A", "code": "Andrea", "info": "{\"especie\": \"human\", \"sexo\": \"F\"}"},
            {"status": "0", "code": "Xatli", "info": "{\"especie\": \"human\", \"sexo\": \"F\"}"}, 
        ]

        QueryJsonModel.objects.all().delete()

        for reg in data:
            QueryJsonModel.objects.create(**reg)


        rs = QueryJsonModel.objects.filter( info__especie = 'human')    
        info = rs[0].info
#         
#         rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human')    
#         rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human', info__sexo = 'M')
#          
#         rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human').count()
# 
#         rs = QueryJsonModel.objects.filter( status = 'A').order_by('code')
#         rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human').order_by('code')    
#         rs = QueryJsonModel.objects.filter( status = 'A', info__especie = 'human').order_by('-code')    
 
#         rs = QueryJsonModel.objects.filter( status = 'A', info__icontains = 'human')    

        pass 

#   Recorre los registros selccionados   
    except Exception as e:
        traceback.print_exc()
        pass

