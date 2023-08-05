import json
import os
import sys

name = "rgpubsub"


def topic(topic_name, project_name=None):
    if not project_name:
        project_name = os.getenv('GOOGLE_CLOUD_PROJECT')

    return 'projects/%s/topics/%s' % (project_name, topic_name)


class Publisher:

    @classmethod
    def default_instance(cls):
        if sys.version_info[0] == 2:
            from rgpubsub.clients.google_rest import GoogleRestPublisher
            return GoogleRestPublisher()
        else:
            from rgpubsub.clients.google_clients import GoogleClientPublisher
            return GoogleClientPublisher()

    def create_topic(self, topic_name):
        return self._create_topic(topic_name)

    def publish(self, topic_name, payload, arguments=None):
        if not payload:
            raise ValueError('Expected payload to send')

        if isinstance(payload, dict):
            payload = json.dumps(payload)

        if isinstance(payload, str):
            payload = payload.encode('utf-8')

        if not isinstance(payload, bytes):
            raise ValueError('Payload must be in bytes, got %s' % type(payload))

        if not arguments:
            arguments = {}

        self._send(topic_name, payload, arguments)

    def _send(self, topic_name, payload, arguments):
        raise NotImplementedError()

    def _create_topic(self, topic_name):
        raise NotImplementedError()
