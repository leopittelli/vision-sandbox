import os
import base64

import jinja2
import webapp2

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
FEATURE_TYPES = {
    '0': 'TEXT_DETECTION'
}

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({'section': 'upload'}))

    def post(self):
        image_content = base64.b64encode(self.request.get('img'))
        feature_type = 0 #FEATURE_TYPES[self.request.get('type')]

        credentials = GoogleCredentials.get_application_default()
        service = discovery.build('vision', 'v1', credentials=credentials,
                                  discoveryServiceUrl=DISCOVERY_URL)

        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': feature_type
                }]
            }]
        })
        response = service_request.execute()
        result = False

        if ('textAnnotations' in response['responses'][0]):
            result = response['responses'][0]['textAnnotations'][0]['description']

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({'result': result, 'image': image_content, 'section': 'result'}))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)