import logging
from unittest import TestCase
from unittest.mock import Mock

from awsLexAlexa.event_handler import EventHandler, LEX, ALEXA, DEFAULT_INTENT
from test.json_events import INPUT_EVENT_LEX, INPUT_EVENT_ALEXA


class TestHandler(TestCase):
    def setUp(self):
        logging.getLogger("awsLexAlexa").setLevel(logging.NOTSET)

    def test_bot_platform_detection(self):
        self.assertEqual(EventHandler._detect_bot_platform(INPUT_EVENT_LEX), LEX)
        self.assertEqual(EventHandler._detect_bot_platform(INPUT_EVENT_ALEXA), ALEXA)

    def test_call_specific_intent(self):
        ev = EventHandler()
        mock_function_specific = Mock()
        mock_function_specific2 = Mock()
        mock_function_default = Mock()

        ev.handler_intent["intent_name"] = mock_function_specific
        ev.handler_intent["intent_name2"] = mock_function_specific
        ev.handler_intent[DEFAULT_INTENT] = mock_function_default

        json_event_specific = {'currentIntent': {'name': "intent_name"}}

        ev.execute(json_event_specific)
        self.assertTrue(mock_function_specific.called, msg="Specific function did not be called")
        self.assertFalse(mock_function_specific2.called, msg="Specific function called not correct")
        self.assertFalse(mock_function_default.called,
                         msg="Generic function called when specific function was expected")

    def test_call_generic_intent(self):
        ev = EventHandler()
        mock_function_default = Mock()
        mock_function_specific = Mock()

        ev.handler_intent["intent_name"] = mock_function_specific
        ev.handler_intent["intent_name2"] = mock_function_specific
        ev.handler_intent[DEFAULT_INTENT] = mock_function_default

        json_event_generic = {'currentIntent': {'name': "intent_name_fail"}}

        ev.execute(json_event_generic)
        self.assertTrue(mock_function_default.called, msg="Default function did not be called")
        self.assertFalse(mock_function_specific.called, msg="Specific function called when default was expected")
