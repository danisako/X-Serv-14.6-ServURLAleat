import webaleatorias
import random
class UrlApp(webaleatorias.webApp):


	def process(self, parsedRequest): 
		num = random.randint(1,1000)
		return ("200 OK", "<html><body><h1>Hola. <a href = 'http://localhost:1234/" + str(num)+ "'>Dame otra! </a></h1></body></html>") 
 

if __name__ == "__main__":
    testWebApp = UrlApp("localhost", 1234)