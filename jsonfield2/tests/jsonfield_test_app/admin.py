# -*- coding: utf-8 -*-
from django.contrib  import admin


# =================   TESTS QueryJsonModel  

from .models import QueryJsonModel
from .actions import doJsonTest

class QueryJsonModelAdmin(admin.ModelAdmin):
    actions = [ doJsonTest, ]

admin.site.register(QueryJsonModel, QueryJsonModelAdmin)
