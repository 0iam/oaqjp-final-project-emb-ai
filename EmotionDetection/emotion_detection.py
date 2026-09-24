"""
This module provides utility function for emotion prediction
"""
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    ''' This code receives the text from the HTML interface and
        runs emotion detection analysis over it using watson.
        The output returned shows the emotions and corresponding scores.
    '''

    # URL of the emotion predictor service
    url = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Handle blank or invalid input returned by the server.
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Format the server response
    formatted_response = response.json()

    # Extract the emotion scores
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_predictions.items(), key=lambda item: item[1])[0]

    # Add the dominant emotion to the result.
    emotion_predictions['dominant_emotion'] = dominant_emotion

    # Returning a dictionary containing emotion predictions
    return emotion_predictions
