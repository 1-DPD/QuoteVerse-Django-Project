# quoteverse/admin.py

from django.contrib import admin
from .models import Bookshelf, Quote

admin.site.register(Bookshelf)
admin.site.register(Quote)
