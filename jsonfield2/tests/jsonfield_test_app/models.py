from django.db import models
from jsonfield2 import JSONField, JSONAwareManager

class JSONFieldTestModel(models.Model):
    json = JSONField("test", null=True, blank=True)

    class Meta:
        app_label = 'jsonfield2'


class JSONFieldWithDefaultTestModel(models.Model):
    json = JSONField(default={"sukasuka": "YAAAAAZ"})

    class Meta:
        app_label = 'jsonfield2'


class BlankJSONFieldTestModel(models.Model):
    null_json = JSONField(null=True)
    blank_json = JSONField(blank=True)

    class Meta:
        app_label = 'jsonfield2'


class CallableDefaultModel(models.Model):
    json = JSONField(default=lambda: {'x': 2})

    class Meta:
        app_label = 'jsonfield2'


class QueryJsonModel(models.Model):
    code = models.CharField( blank=False, null=False, max_length=20 )
    status = models.CharField( blank=True, null=True, max_length=20 )

    info = JSONField(default={})
    
    objects = JSONAwareManager(json_fields = ['info'])
    
    def __str__(self):
        return self.code

    class Meta:
        app_label = 'jsonfield2'
