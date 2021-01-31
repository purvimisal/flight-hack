from flask import Flask, request, flash, jsonify, redirect, render_template
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from dotenv import load_dotenv
import os
from messages import get_message
import dialogflow_v2 as dialogflow
import six
from google.cloud import translate_v2 as translate
from utils import get_news, get_stats, regulations
import psycopg2



load_dotenv()
app = Flask(__name__)

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "chatterbotter-195d413ff986.json"
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "chatterbotter"
twilio = Client()
translate_client = translate.Client()
EVENT, STATIC_MESSAGE, DETECTED_LANGUAGE = None, None, "en"


def detect_intent_from_text(text: str,
                            session_id: int,
                            language_code='en') -> str:
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text,
                                            language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session,
                                                       query_input=query_input)
    print(response)
    return response.query_result


def detect_language(text: str) -> str:
    """Detects the text's language."""
    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    return str(translate_client.detect_language(text)["language"])


def translate_text(target: str, text: str) -> str:
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    return translate_client.translate(text,
                                      target_language=target)["translatedText"]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send/<phone_number>/<event>', methods=['GET'])
def send_notification(phone_number, event):
    conn = psycopg2.connect(
        database='defaultdb',
        user='user1',
        port=26257,
        sslmode='verify-full',
        host='mature-hyena-8jv.gcp-us-west2.cockroachlabs.cloud',
        sslrootcert='certs/mature-hyena-ca.crt',
        password='user123456789'
    )
    global EVENT
    EVENT = event
    message = get_message(event)
    global STATIC_MESSAGE
    STATIC_MESSAGE = message
    response_message = '\n'.join(message['text'])
    translate_response = translate_text(
            DETECTED_LANGUAGE, str(response_message)
        ) if DETECTED_LANGUAGE != "en" else str(
            response_message)

    twilio.messages.create(from_=TWILIO_NUMBER,
                           to='whatsapp:+' + phone_number,
                           body=translate_response,
                           media_url=message['image'])
    with conn.cursor() as cur:
        print(f'INSERT INTO notifications (notification_type, phone_number) VALUES ({event}, {phone_number});')
        cur.execute(f"INSERT INTO notifications (notification_type, phone_number) VALUES ('{event}', '{phone_number}');")
    conn.commit()

    return jsonify({'status_code': 200, 'message': 'Message sent!'})


@app.route('/bot', methods=['POST'])
def bot():
    global DETECTED_LANGUAGE
    data = request.form
    incoming_msg = request.values.get('Body', '').lower()
    phone_number = data.get("From").replace("whatsapp:+", "")
    DETECTED_LANGUAGE = detect_language(incoming_msg)
    incoming_msg = translate_text("en", incoming_msg) if DETECTED_LANGUAGE != "en" else incoming_msg
    response = MessagingResponse()

    
    if 'details' in incoming_msg and EVENT:
        translate_response = translate_text(
            DETECTED_LANGUAGE, str('Here is the link: ')
        ) if DETECTED_LANGUAGE != "en" else str(
            'Here is the link: ')
        message = response.message(translate_response +
                                STATIC_MESSAGE['link'])
        message.media(STATIC_MESSAGE['detailed_image'])
        return str(response)

    elif 'opt in' in incoming_msg or 'optin' in incoming_msg:
        send_notification(phone_number, 'Welcome_to_aa')

    elif 'news' in incoming_msg:
        result = get_news(incoming_msg)
        for i in result:
            response.message(i)
        return str(response)
    elif 'stats' in incoming_msg or 'statistics' in incoming_msg:
        result = get_stats(incoming_msg)
        response.message(result)
        return str(response)
    elif 'regulations' in incoming_msg:
        result = regulations(incoming_msg)
        response.message(result)
        return str(response)
    else: 
        response_dialogFlow = detect_intent_from_text(str(incoming_msg),
                                                    phone_number)
        translate_response = translate_text(
            DETECTED_LANGUAGE, str(response_dialogFlow.fulfillment_text)
        ) if DETECTED_LANGUAGE != "en" else str(
            response_dialogFlow.fulfillment_text)
        response.message(translate_response)
        return str(response)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
