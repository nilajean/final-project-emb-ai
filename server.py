from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return "Please provide some text to analyze using the 'textToAnalyze' query parameter.", 400
    
    response = emotion_detector(text_to_analyze)

    anger_score = response.get('anger', 0)
    disgust_score = response.get('disgust', 0)
    fear_score = response.get('fear', 0)
    joy_score = response.get('joy', 0)
    sadness_score = response.get('sadness', 0)

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    result = f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

    return render_template('result.html', result=result)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
