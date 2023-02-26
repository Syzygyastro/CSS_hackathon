import os
import requests
from flask import Flask, request, jsonify, render_template
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


app = Flask(__name__)

# Add your Azure Cognitive Services API key and endpoint here
SUBSCRIPTION_KEY = "6a1504350e484b63882efe45cfe1ac2a"
TEXT_ANALYTICS_ENDPOINT = "https://hackaton-css-serendipity.cognitiveservices.azure.com/"
text_analytics_client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=AzureKeyCredential(SUBSCRIPTION_KEY))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_message = data['message']

    try:
        # Call the Azure Text Analytics API for sentiment analysis
        documents = [user_message]
        response = text_analytics_client.analyze_sentiment(documents=documents)[0]

        sentiment_api_result = response.sentiment
        sentiment_score = response.confidence_scores[sentiment_api_result]

        # Customize the response based on the sentiment analysis results
        if sentiment_api_result == 'positive':
            bot_response = 'That\'s great to hear!'
            questions = ['What made you feel positive today?', 'What are you looking forward to?', 'What are some of your successes?']
        elif sentiment_api_result == 'negative':
            bot_response = 'I\'m sorry to hear that.'
            questions = ['What is making you feel down?', 'Is there anything you would like to talk about?', 'What would make you feel better?']
        else:
            bot_response = 'Interesting!'
            questions = ['Can you tell me more about that?', 'What else is on your mind?', 'What do you enjoy doing?']

        # Add an advice question to all responses
        questions.append('Have you tried talking to someone about this? It might help.')

        # Generate a demo chart with sentimentality score trend over a week
        week_dates = [datetime.now().date() - timedelta(days=i) for i in range(7)]
        sentiment_scores = [0.5, 0.3, 0.2, 0.6, 0.7, 0.8, 0.9] # dummy data for sentiment scores
        plt.figure(figsize=(8, 4))
        ax = sns.lineplot(x=week_dates, y=sentiment_scores)
        ax.set(xlabel='Date', ylabel='Sentiment Score', title='Sentiment Score Trend over a Week')
        chart_img = ax.get_figure()
        chart_img.savefig('chart.png')

        # Return the bot's response, sentiment score, and advice questions
        return jsonify({'bot_response': bot_response, 'sentiment': sentiment_api_result, 'questions': questions})
    except Exception as ex:
        return jsonify({'bot_response': 'Oops! Something went wrong.', 'sentiment': 'unknown', 'error': str(ex)})


if __name__ == '__main__':
    app.run(debug=True)

