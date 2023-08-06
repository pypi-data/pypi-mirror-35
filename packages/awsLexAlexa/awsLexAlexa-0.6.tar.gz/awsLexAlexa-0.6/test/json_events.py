INPUT_EVENT_LEX = {
    'messageVersion': '1.0',
    'invocationSource': 'FulfillmentCodeHook',
    'userId': 'some_user_id',
    'sessionAttributes': {"sessionAttributeKey": "sessionAttributeValue"},
    'requestAttributes': None,
    'bot': {'name': 'bot_name', 'alias': '$LATEST', 'version': '$LATEST'},
    'outputDialogMode': 'Text',
    'currentIntent': {
        'name': 'test',
        'slots': {'Uniforms': 'now'},
        'slotDetails': {'Uniforms': {'resolutions': [{'value': 'now'}], 'originalValue': 'now'}},
        'confirmationStatus': 'None'
    },
    'inputTranscript': 'now'
}

INPUT_EVENT_ALEXA = {
    "version": "1.0",  # Version, String
    "context": {
        "System": {
            "application": {
                "applicationId": "<skill_id>"  # Skill id, String
            },
            "user": {
                "userId": "amzn1.ask.account.VEBA...",  # Skill user id, String
                "accessToken": "<access_token>",  # Token to identify user in 3P
                "permissions": {
                    "consentToken": "Atza|IgEB..."  # Token to call Lists API
                }
            },
            "apiEndpoint": "https://api.amazonalexa.com"  # Endpoint to call Lists API
        }
    },
    "request": {
        "type": "AlexaHouseholdListEvent.ItemsCreated",
        "requestId": "913e4588-62f9-4d5b-b7ba-c0d3c1210ce9",  # String
        "timestamp": "2017-09-15T01:46:14Z",  # Timestamp, YYYY-MM-DD'T'hh:mm:ss'Z'
        "body": {
            "listId": "09d9d7df-05be-438c-veba-9d32968b4509",  # List id, String
            "listItemIds": [
                "520a9f98-8e73-4fb8-veba-bfb6576cf623"  # Item ids, String
            ]

        }
    },
    "session": {
        "attributes": {}
    }
}
