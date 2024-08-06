from django.template import loader # type: ignore
from django.http import HttpResponse # type: ignore

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())