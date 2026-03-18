# # This files contains your custom actions which can be used to run
# # custom Python code.

# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/core/actions/#custom-actions/


# # This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from database_conn import GetData
import google.generativeai as genai
import os



class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text =tracker.latest_message['text']
        dispatcher.utter_message(text=f"That's a nice name {text}!")
        return [SlotSet("name",text)]

class ActionReceiveDelight(Action):
    def name(self) -> Text:
        return "action_receive_delight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text =tracker.latest_message['text']
        dispatcher.utter_message(text=f"Great!")
        return [SlotSet("user_delight",text)]

class ActionReceiveMood(Action):
    def name(self) -> Text:
        return "action_receive_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(template="utter_submit")
        return [SlotSet("journal",tracker.latest_message['text'])]


        

class ActionGetData(Action):
    def name(self) -> Text:
        return "action_get_data"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(text=" Your Name is {0}\n Your Feedback is {1}".format(tracker.get_slot("name"),tracker.get_slot("journal")))
        GetData( tracker.get_slot("name"),tracker.get_slot("journal"))
        dispatcher.utter_message('Thanks for the feedback!')
        return[]
# keeps track of every conversation
class ActionSessionId(Action):
    def name(self) -> Text:
        return "action_session_id"
    
    async def run(
        self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            conversation_id=tracker.sender_id

            dispatcher.utter_message("The conversation id is {}".format(conversation_id))

            return []

class ActionDefaultAskQuestion(Action):
    def name(self) -> Text:
        return "action_default_ask_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the API key from environment variables
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            dispatcher.utter_message(text="I'm sorry, but I'm not configured to answer questions right now. The API key is missing.")
            return []

        genai.configure(api_key=api_key)
        user_question = tracker.latest_message.get('text')
        
        try:
            model = genai.GenerativeModel(
                'gemini-1.5-flash',
                system_instruction="You are Lumi, a calm, compassionate, caring, and pampering mental health assistant with a retro pixel pet tamagotchi vibe. Your role is to provide helpful, safe, understanding, and cozy information. Do not give medical advice, but you can provide general knowledge and supportive guidance. If a user seems to be in crisis, gently suggest they contact a crisis hotline or mental health professional."
            )
            response = model.generate_content(user_question)
            answer = response.text
            dispatcher.utter_message(text=answer)
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            dispatcher.utter_message(text="I'm sorry, I encountered a problem while trying to find an answer for you. Please try again later.")

        return []