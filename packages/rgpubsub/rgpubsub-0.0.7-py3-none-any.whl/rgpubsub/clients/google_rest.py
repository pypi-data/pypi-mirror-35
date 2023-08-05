import base64
import json

import google
from google.auth.transport.requests import AuthorizedSession
from rgpubsub import Publisher

# https://cloud.google.com/pubsub/docs/reference/rest/

class GoogleRestPublisher(Publisher):

    def __init__(self):
        credentials, project = google.auth.default(scopes=[
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/pubsub'])

        self.session = AuthorizedSession(credentials)

    def _create_topic(self, topic_name):
        url = 'https://pubsub.googleapis.com/v1/%s' % topic_name
        response = self.session.put(url, json={})

        if response.status_code == 200:
            return True
        elif response.status_code == 409:
            return False
        else:
            raise ValueError('Got unexpected response from Pubsub: status %s content %s', response.status_code, response.text)

    def _send(self, topic, payload, arguments):
        url = 'https://pubsub.googleapis.com/v1/%s:publish' % topic
        response = self.session.post(url, json=payload)

        # TODO Add check on response

    @staticmethod
    def _encode(payload):
        json_payload = json.dumps(payload)
        return base64.urlsafe_b64encode(json_payload)





