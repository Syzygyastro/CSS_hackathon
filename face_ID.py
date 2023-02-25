import cv2
import requests
import json

# Set the API endpoint and subscription key
face_api_url = 'https://<UK South>.api.cognitive.microsoft.com/face/v1.0/detect'
subscription_key = '<98b70ba7-67cf-419f-9b9d-dcf47bf2748c>'

# Set the API parameters
params = {
    'returnFaceAttributes': 'emotion'
}

# Set the API headers
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key
}

# Set up the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to bytes
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = img_encoded.tobytes()

    # Make the API request
    response = requests.post(face_api_url, headers=headers, params=params, data=img_bytes)

    # Parse the response
    json_data = json.loads(response.text)
    if len(json_data) > 0:
        emotions = json_data[0]['faceAttributes']['emotion']
        print(emotions)
    else:
        print('No faces detected.')

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy the window
cap.release()
cv2.destroyAllWindows()
