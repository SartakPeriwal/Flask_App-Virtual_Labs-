import urllib,json
import unittest
from flask import Flask
from flask_testing import LiveServerTestCase 
from urllib import request, parse
# Testing with LiveServer
class MyTest(LiveServerTestCase):
    '''
    this function is there for unit testing for the get method  
    it checks for the return code to be 200
    it checks if the render_template is working
    '''
    # if the create_app is not implemented NotImplemen	tedError will be raised
    SERVER="http://0.0.0.0:8080/"
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 0
        return app 
    def test_controller_is_up_and_running(self):
        urls=["","theory.html","objective.html","experiment.html","manual.html","feedback.html","introduction.html","quizzes.html","procedure.html","refrences.html", "checkAnswers","numberselect"]
        for i in range(10):
            response = urllib.request.urlopen(self.SERVER+urls[i])
            self.assertEqual(response.code, 200)
            assert "" != response.read()

# Data dict
    def test_check_post_1(self):
        '''
        this function is there for unit testing for the post method  
        it checks for the return code to be 200
        '''
        data = { 'hidbit1':'','hidnum':28.125,'hidind':'','hidans':1,'sm':0,'exp':10000011,'mantes':'110000100..'}

        data = parse.urlencode(data).encode()
        req =  request.Request("http://0.0.0.0:8080/checkAnswers", data=data) # this will make the method "POST"
        resp = request.urlopen(req)
    def test_check_post_2(self):
        data = { 'dropddbit':'1'}

        data = parse.urlencode(data).encode()
        req =  request.Request("http://0.0.0.0:8080/bitselect", data=data) # this will make the method "POST"
        resp = request.urlopen(req)
    def test_check_post_3(self):
        data = {'hidbit':'1','dropddnumber':'28.125'}

        data = parse.urlencode(data).encode()
        req =  request.Request("http://0.0.0.0:8080/numberselect", data=data) # this will make the method "POST"
        resp = request.urlopen(req)
# Dict to Json
# Difference is { "test":10, "test2":20 }

# Convert to String

# Convert string to byte

# Post Method is invoked if data != None

# Response
if __name__ == '__main__':
    unittest.main()
