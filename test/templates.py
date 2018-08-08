from django.conf import settings
from django import template
import os

# settings.configure()
# t=template.Template('my name is {{name}}.')
# c=template.Context({'name':'Book'})
# print t.render(c)
print os.path.join(os.path.dirname(__file__))