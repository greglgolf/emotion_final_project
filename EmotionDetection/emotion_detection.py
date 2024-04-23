import json, requests


def emotion_detector(text_to_analyse):

    formatted_data = {
            'anger':'None',
            'disgust':'None',
            'fear':'None',
            'joy':'None',
            'sadness':'None',
            'dominant_emotion':'None'
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 400:
        return formatted_data

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    max_emo = max(emotions, key=emotions.get)
    max_emo_score = emotions[max_emo]
    if response.status_code == 200:
        formatted_data = {
            'anger':emotions['anger'],
            'disgust':emotions['disgust'],
            'fear':emotions['fear'],
            'joy':emotions['joy'],
            'sadness':emotions['sadness'],
            'dominant_emotion':max_emo
        }

    return formatted_data