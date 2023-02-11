# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionUtterLocation(Action):

    def name(self) -> Text:
        return "action_utter_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        places = {
                    "unifap":{"latitude": -0.006323019979364349,
                                    "longitude": -51.08270659116776},
                    "computação":{"latitude": -0.002937,
                                    "longitude": -51.084196},
                    "engenharia eletrica":{"latitude": -0.002937,
                                    "longitude": -51.084196},
                    "letras":{"latitude": -0.004166005594351067,
                                    "longitude": -51.08418297799158},
                    "anfiteatro":{"latitude": -0.007215790482183133,
                                    "longitude": -51.0835086813143},
                    "ru":{"latitude": -0.008080799437680657,
                                    "longitude": -51.083689730713985},
                    "biblioteca":{"latitude": -0.007298635579484426,
                                    "longitude": -51.084805364437294},
                    "ginasio":{"latitude": -0.005511126816573149,
                                    "longitude": -51.08325324851948},
                    "reitoria":{"latitude": -0.006650882433062583,
                                    "longitude": -51.08380154857428},
                    "derca":{"latitude": -0.006039698644908812,
                                    "longitude": -51.084188435835166},
                    "dcet":{"latitude": -0.006046553503424945,
                                    "longitude": -51.08446370835129},
                    "nai":{"latitude": -0.007547903721781402,
                                    "longitude": -51.08473866865888},
                    "posto de saude":{"latitude": -0.009502598385964829,
                                        "longitude": -51.088881901030305},
                    "nti":{"latitude": -0.0060490249275337,
                                        "longitude": -51.08479139781439},
                    "xerox":{"latitude": -0.008218507124738528,
                                        "longitude": -51.0850496714252}
                }

        slot = tracker.get_slot("lugar")
        if 'banheiro' in slot:
            dispatcher.utter_message(text = "Geralmente fica no final do \
            corredor de cada um dos blocos dos cursos. Não posso fornecer uma \
            informação mais precisa pois não tenho informação sobre todos os \
                                                                        locais")
        elif slot in places:
            place = places[slot]
            dispatcher.utter_message(text = "Essas são as coordenadas que eu \
                        disponho para: {}".format(slot.upper()), json_message = place)
        else:
            dispatcher.utter_message(text = "Desculpe, ainda não sei informar \
                            o local solicitado ou não entendi sua solicitação")
        return[SlotSet("lugar", None)]
