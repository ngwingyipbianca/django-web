from django.http import HttpResponse
from django.template import loader
from .models import List_of_items

def landing_page(request):
  template = loader.get_template('landing_page.html')
  return HttpResponse(template.render())

def line_items(request):
  my_list = List_of_items.objects.all().values()
  template = loader.get_template('list_page.html')
  context = {
    'my_list_of_items' : my_list,
  }
  return HttpResponse(template.render(context, request))