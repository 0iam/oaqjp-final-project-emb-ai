"""
Flask application for emotion detection.

This module defines the web routes used by the Emotion Detector
application. It accepts text from the web interface, sends the text
to the emotion detection service, and displays the detected emotion
scores along with the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_predictor():
    """
    Analyze text submitted through the web interface.

    The function retrieves text from the request, passes it to the
    emotion_detector function, and returns the emotion scores and
    dominant emotion.

    Returns:
        str: A formatted string containing the detected emotions
        and their corresponding scores.
    """
    # Retrieve the text entered by the user from the request parameters.
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion detection function.
    response = emotion_detector(text_to_analyze)

    # Return an error message when black text is submitted
    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."

    # Format and return the emotion scores and dominant emotion.
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the application's main HTML page.

    Returns:
        str: The rendered index.html template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
