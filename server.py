from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Renders the main application page over the Flask server.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """
    Retrieves the text to analyze from the user interface and passes it
    to the emotion_detector function. Formats the response to match the
    customer's requested string format.
    """
    # Retrieve the text to analyze from the GET request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_detector function and store the dictionary
    response = emotion_detector(text_to_analyze)
    
    # Format the output string exactly as requested by the customer
    formatted_string = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return formatted_string

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)