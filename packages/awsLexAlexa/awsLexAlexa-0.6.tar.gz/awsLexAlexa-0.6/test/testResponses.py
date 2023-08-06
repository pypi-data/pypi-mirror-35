import logging
from unittest import TestCase

from awsLexAlexa.events.alexaEvent import AlexaEvent
from awsLexAlexa.events.lexEvent import LexEvent
from test.json_events import INPUT_EVENT_LEX


class TestLexResponses(TestCase):
    def setUp(self):
        logging.getLogger("awsLexAlexa").setLevel(logging.NOTSET)

        self.lex = LexEvent(INPUT_EVENT_LEX)

    def test_delegate(self):
        json_delegate = {
            "sessionAttributes": {"sessionAttributeKey": "sessionAttributeValue"},
            "dialogAction": {
                "type": "Delegate",
                "slots": {'Uniforms': "now"},
            }
        }

        self.assertEqual(self.lex.delegate_response(), json_delegate)

    def test_elicit_slot_response(self):
        json_elicit_slot = {
            "sessionAttributes": {"sessionAttributeKey": "sessionAttributeValue"},
            "dialogAction": {
                "type": "ElicitSlot",
                "message": {
                    "contentType": "PlainText",
                    "content": "message"
                },
                "intentName": "test",
                "slots": {'Uniforms': None},
                "slotToElicit": "Uniforms"
            }
        }
        self.assertEqual(self.lex.elicit_slot_response("Uniforms", "message"), json_elicit_slot)


class TestALexResponses(TestCase):
    def setUp(self):
        logging.getLogger("awsLexAlexa").setLevel(logging.NOTSET)

        self.alexa = AlexaEvent(INPUT_EVENT_LEX)

    def test_delegate(self):
        json_delegate = {
            "sessionAttributes": {"sessionAttributeKey": "sessionAttributeValue"},
            "dialogAction": {
                "type": "Delegate",
                "slots": {'Uniforms': 'now'},
            }
        }

        # self.assertEqual(self.alexa.delegate_response(), json_delegate)

    def test_elicit_slot_response(self):
        json_elicit_slot = {
            "sessionAttributes": {"sessionAttributeKey": "sessionAttributeValue"},
            "dialogAction": {
                "type": "ElicitSlot",
                "message": {
                    "contentType": "PlainText",
                    "content": "message"
                },
                "intentName": "test",
                "slots": {'Uniforms': None},
                "slotToElicit": "Uniforms"
            }
        }
        # self.assertEqual(self.alexa.elicit_slot_response("Uniforms", "message", "casa"), json_elicit_slot)
