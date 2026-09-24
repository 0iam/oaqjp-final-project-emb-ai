# Emotion Detector

A Flask-based web application that analyzes text and identifies the emotions expressed in it.

The application sends user-provided text to an emotion detection service and returns scores for the following emotions:

Anger, Disgust, Fear, Joy, Sadness

It also identifies the **dominant emotion**, which is the emotion with the highest score.

## Project Overview

This project was developed as part of the IBM Generative AI Engineering coursework.

The application consists of:

* An emotion detection module that communicates with the Watson NLP emotion prediction service
* A Flask web server that handles user requests
* A web interface where users can enter text for analysis
* Error handling for blank or invalid input

## Features

* Analyze text for multiple emotions
* Return emotion confidence scores
* Determine the dominant emotion
* Handle blank input gracefully
* Display results through a Flask web interface
* Modular Python application structure

## Technologies Used

* Python
* Flask
* Requests
* IBM Watson NLP Emotion Prediction Service
* HTML
* Git
## Project Structure

```text
final_project
├── EmotionDetection
│   ├── emotion_detection.py
│   └── __init__.py
├── LICENSE
├── README.md
├── server.py
├── static
│   └── mywebscript.js
├── templates
│   └── index.html
└── test_emotion_detection.py
```

## Emotion Detection Module

The `emotion_detection.py` module contains the `emotion_detector()` function.

The function:

1. Accepts text as input.
2. Sends the text to the emotion prediction API.
3. Extracts the emotion scores from the API response.
4. Determines the emotion with the highest score.
5. Returns the emotion scores and dominant emotion as a Python dictionary.

Example output:

```python
{
    "anger": 0.0138,
    "disgust": 0.0085,
    "fear": 0.0184,
    "joy": 0.8323,
    "sadness": 0.1725,
    "dominant_emotion": "joy"
}
```
## Error Handling

The application handles blank or invalid input.

If the emotion prediction service returns HTTP status code `400`, the emotion detector returns:

```python
{
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None
}
```

The Flask server checks the value of `dominant_emotion`.

If it is `None`, the application displays:

```text
Invalid text! Please try again!
```

## Running the Application

Install the required Python packages:

```bash
pip install flask requests
```

Run the Flask application:

```bash
python server.py
```

Depending on the lab environment, the application may also be started using Flask:

```bash
flask --app server run
```

Open the application in your browser and enter text to analyze its emotional content.

## Example

Input:

```text
I am really glad this happened.
```

Example result:

```text
For the given statement, the system response is
'anger': 0.0138,
'disgust': 0.0085,
'fear': 0.0184,
'joy': 0.8323 and
'sadness': 0.1725.
The dominant emotion is joy.
```

## API Endpoint

The application exposes the following endpoint:

```text
/emotionDetector
```

The text to analyze is passed using the `textToAnalyze` query parameter.

Example:

```text
/emotionDetector?textToAnalyze=I am happy today
```

## Repository

GitHub repository:

```text
https://github.com/0iam/oaqjp-final-project-emb-ai
```
