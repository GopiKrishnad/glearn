from tornadows import soaphandler
from tornadows import webservices
from tornadows import xmltypes
from tornadows.soaphandler import webservice

class HelloWorldService(soaphandler.SoapHandler):
	""" Service that return Hello World!!!, not uses input parameters """
	@webservice(_params=None,_returns=xmltypes.String)
	def sayHello(self):
		return "Hello World!!!"

#service = [('HelloWorldService',HelloWorldService)]
#app = webservices.WebService(service)
#ws  = tornado.httpserver.HTTPServer(app)
#ws.listen(8080)
#tornado.ioloop.IOLoop.instance().start()
