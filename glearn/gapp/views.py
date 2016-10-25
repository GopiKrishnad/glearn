from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from soap import SoapView
from soap import soapmethod
from soap import soap_types, Array
from soap import ClassModel


class Item(ClassModel):
    __namespace__ = 'warehouse'
    pk = soap_types.Integer
    name = soap_types.String

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
