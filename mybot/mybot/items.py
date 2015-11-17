# -*- coding: utf-8 -*-

from scrapy_djangoitem import DjangoItem
from scrapy.item import Field

from myapp.models import Person


class PersonItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = Person