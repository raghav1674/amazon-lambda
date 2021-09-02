import requests
import numpy 

def test_handler(event,context):
        
        
	print(event)
        print(numpy.ones(10))
        return {
		
		"message": 'Hello World',
	}
