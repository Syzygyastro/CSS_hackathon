# CSS_hackathon

#Link to FIGMA prototype:
https://www.figma.com/file/LcmxodzUhbEGKGzOWW8zVl/RESERVOIR-FIGMA-2?node-id=0%3A1&t=N38ursNyfXUprTOu-0


##Sentiment Analyzer Chatbot

This is a simple Flask application that implements a chatbot with sentiment analysis capabilities. The chatbot uses the Azure Cognitive Services Text Analytics API to analyze the sentiment of user input, and generates an appropriate response based on the sentiment score.

#Installation
1.Clone this repository.

2.Install the required dependencies with the following command:

pip install -r requirements.txt

3. Add your Azure Cognitive Services API key and endpoint to the web_app.py file:

SUBSCRIPTION_KEY = "YOUR_SUBSCRIPTION_KEY_HERE"
TEXT_ANALYTICS_ENDPOINT = "YOUR_TEXT_ANALYTICS_ENDPOINT_HERE"

4. Start the Flask development server by running the following command:
python web_app.py

5. Open a web browser and navigate to http://localhost:5000/ to access the chatbot interface.

#Usage
1. Enter a message in the input field and click "Send".
2. The chatbot will analyze the sentiment of your message and generate an appropriate response.
3. The chatbot will also generate a sentiment score trend chart over the past week.

#Code Overview
The main application logic is implemented in the web_app.py file. The file contains the following components:

1. Flask application initialization.
2. Routes for the chatbot interface (/) and chatbot logic (/chatbot).
3. Functionality for calling the Azure Text Analytics API for sentiment analysis.
4. Customization of the chatbot response based on sentiment analysis results.
5. Generation of a sentiment score trend chart using the Seaborn and Matplotlib libraries.
