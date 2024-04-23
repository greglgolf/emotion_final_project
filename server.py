''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotional_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    size = len(text_to_analyze)
    if size == 0:
        return "Please enter a sentence."

    response = emotion_detector(text_to_analyze)
    dom_value = response['dominant_emotion']
    if dom_value is None:
        return "invalid entry! Try again."

    return jsonify(response)

@app.route("/")
def render_index_page():
    '''
        render the index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5017)
