"""
This module implements a Flask web application that detects emotions
from a given text input. It provides an API endpoint to analyze text
and returns the detected emotions along with the dominant emotion.

The application uses the EmotionDetection library to process the text
and return the analysis results, including emotions like anger, disgust,
fear, joy, sadness, and the dominant emotion.

Author: [Your Name]
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create an instance of the Flask web application
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_detector():
    """
    Analyzes the emotion in a given text and returns the emotion analysis results.

    This function retrieves the text input from the URL query parameters, processes 
    the text using the emotion_detector, and returns the analysis of various emotions 
    (anger, disgust, fear, joy, sadness) along with the dominant emotion.

    Returns:
        str: A string representation of the emotion analysis results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again."

    return f"For the given statement, the system response is " \
           f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
           f"'joy': {joy}, and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the Emotion Detector application.

    Returns:
        str: The rendered HTML of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Start the Flask application on 0.0.0.0 to make it accessible externally on port 5000
    app.run(host="0.0.0.0", port=5000)
