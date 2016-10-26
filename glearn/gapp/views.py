from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from pysimplesoap.server import SoapDispatcher, SOAPHandler, WSGISOAPHandler
from django.http import HttpResponse

def func(data):
    return data
# dispatcher declaration: however you like to declare it ;)
dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8000/gapp/dispatcher_handler/",
    action = 'http://localhost:8000/gapp/dispatcher_handler/',
    namespace = "http://blah.blah.org/blah/blah/local/",
    prefix="bl1",
    ns = "bl2")

# register func
dispatcher.register_function('func', func,
    returns={'result': str},
    args={'data': str})

@csrf_exempt
def dispatcher_handler(request):
    if request.method == "POST":
        response = HttpResponse(content_type="application/xml")
        response.write(dispatcher.dispatch(request.raw_post_data))
    else:
        response = HttpResponse(content_type="application/xml")
        response.write(dispatcher.wsdl())
    response['Content-length'] = str(len(response.content))
    return response

"""# Create your views here.
# -*- coding: utf-8 -*-
from soap import SoapView
from soap import soapmethod
from soap import soap_types, Array
from soap import ClassModel


class Item(ClassModel):
    __namespace__ = 'warehouse'
    pk = soap_types.Integer
    name = soap_types.String

@method_decorator(csrf_exempt, name='dispatch')
class MySoapService(SoapView):
    __tns__ = '[url]http://localhost/my-soap-service/[/url]'
    @soapmethod(soap_types.String,  _returns=soap_types.String)
    def say_hello(self, name):
        results = 'Hello, %s' %name
        return results

    @soapmethod(_returns=Array(Item))
    def get_items(self):
        return [Item(pk=1, name='Item 1'), Item(pk=2, name='Item 2')]

my_soap_service = MySoapService.as_view()
"""

"""
from tornadows import soaphandler
from tornadows import webservices
from tornadows import xmltypes
from tornadows.soaphandler
import webservice		
class MathService(soaphandler.SoapHandler):
    @webservice(_params=[int,int],_returns=int)
    def add(self, a, b):
        return a+b

def math_service(request):
    math = MathService()
"""
