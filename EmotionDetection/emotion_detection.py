import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=obj, headers=header)

    if response.status_code == 400:
        emotion_scores =  {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
        return emotion_scores

    # Parse the JSON response
    formatted_response = json.loads(response.text)
    
    # Extract the emotions
    if 'emotionPredictions' in formatted_response and len(formatted_response['emotionPredictions']) > 0:
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']

        # Extract the emotion scores
        anger_score = emotion_predictions.get('anger', 0)
        disgust_score = emotion_predictions.get('disgust', 0)
        fear_score = emotion_predictions.get('fear', 0)
        joy_score = emotion_predictions.get('joy', 0)
        sadness_score = emotion_predictions.get('sadness', 0)

        # Create a dictionary with all emotion scores
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # Find the dominant emotion, which is the emotion with the highest score
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        # Add the dominant emotion to the dictionary
        emotion_scores['dominant_emotion'] = dominant_emotion
    else:
        emotion_scores = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    # Return the formatted dictionary
    return emotion_scores
