Django-JSONField2 
===================

``django-json-field2`` It is a compilation and adaptation of the following projects 

* https://bitbucket.org/schinckel/django-jsonfield 
* https://github.com/derek-schaefer/django-json-field
* https://github.com/bradjasper/django-jsonfield
* https://github.com/certae/django-softmachine/blob/master/src/protoLib/fields.py
* https://github.com/frol/django-quering-jsonfield
* http://cramer.io/2009/04/14/cleaning-up-with-json-and-sql/ 
* http://natebeacham.com/blog/nate-beacham/31/


Feature	Description
-------------------
South support 	
Form field
Form widget
Model field
Python3 support


``django-jsonfield2`` is also compatible with South, Django 1.8 and Python 3.


Installation
------------

Install from PyPI:

    ``pip install django-jsonfield2``


Source:
-------

    ``git clone git://github.com/DarioGT/django-jsonfield2.git``


Configuration
-------------

Add ``jsonfield2`` to your ``PYTHONPATH`` and ``INSTALLED_APPS`` setting:

::

    INSTALLED_APPS = (
        ...
        'jsonfield2',
        ...
    )



Usage
-----

::
    from django.db import models
	from jsonfield2 import JSONField, JSONAwareManager

	class JsonModel(models.Model):
	    code = models.CharField( blank=False, null=False, max_length=20 )
	    status = models.CharField( blank=True, null=True, max_length=20 )

	    info = JSONField(default={})
	    
	    objects = JSONAwareManager(json_fields = ['info'])
	    
	    def __str__(self):
	        return self.code


Json Query 
----------

::
    ...
    obj = Person.objects.create(name = "Bill")
    obj.info = {
        'sex': 'male',
        'address': {
            'country', 'Canada',
        }
    }
    obj.save()
    Person.objects.filter(info__address__country = 'Canada')
    >>> [Person: "Bill"]



Usage
-----

Now, it will validate the JSON on entry, and store it as a text in the database.  When you instantiate/fetch the object, it will be turned back into a python list/dict/string.



jsonify templatetag
-------------------
This allows you to convert a python data structure into JSON within a template::

    {% load jsonify %}

    <script>
    var foo = {{ bar|jsonify }};
    </script>


Tests 
----------

    ``python runtest.py``


Todo
----------

Allow order_by when json criteria are used 


License
-------

``django-jsonfield2`` is licensed under the New BSD license.

