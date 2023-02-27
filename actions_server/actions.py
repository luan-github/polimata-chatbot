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
                    "computação":{"geolocation": {"latitude": -0.002937,
                                  "longitude": -51.084196},
                                  "name": "Curso de Ciência da Computação"},
                    "coordenação":{"geolocation": {"latitude": -0.0029435945030728662,
                                    "longitude": -51.08438355944174},
                                    "name": "Coordenação de Ciência da Computação"},
                    "engenharia eletrica":{"geolocation": {"latitude": -0.002937,
                                    "longitude": -51.084196},
                                    "name": "Curso de Engenharia Elétrica"},
                    "letras":{"geolocation": {"latitude": -0.004166005594351067,
                              "longitude": -51.08418297799158},
                              "name": "Curso de Letras"},
                    "anfiteatro":{"geolocation": {"latitude": -0.007215790482183133,
                                  "longitude": -51.0835086813143},
                                  "name": "Anfiteatro da UNIFAP"},
                    "ru":{"geolocation": {"latitude": -0.008080799437680657,
                          "longitude": -51.083689730713985},
                          "name": "Restaurante Universitário"},
                    "biblioteca":{"geolocation": {"latitude": -0.007298635579484426,
                                  "longitude": -51.084805364437294},
                                  "name": "Biblioteca da UNIFAP"},
                    "ginasio":{"geolocation": {"latitude": -0.005511126816573149,
                               "longitude": -51.08325324851948},
                               "name": "Ginásio da UNIFAP"},
                    "reitoria":{"geolocation": {"latitude": -0.006650882433062583,
                                "longitude": -51.08380154857428},
                                "name": "Reitoria da UNIFAP"},
                    "derca":{"geolocation": {"latitude": -0.006039698644908812,
                             "longitude": -51.084188435835166},
                             "name": "Departamento de Registro e Controle Acadêmico"},
                    "dcet":{"geolocation": {"latitude": -0.006046553503424945,
                            "longitude": -51.08446370835129},
                            "name": "Departamento de Ciências Exatas e Tecnológicas"},
                    "nai":{"geolocation": {"latitude": -0.007547903721781402,
                           "longitude": -51.08473866865888},
                           "name": "Núcleo de Acessibilidade e Inclusão"},
                    "posto de saude":{"geolocation": {"latitude": -0.009502598385964829,
                                      "longitude": -51.088881901030305},
                                      "name": "Unidade Básica de Saúde"},
                    "nti":{"geolocation": {"latitude": -0.0060490249275337,
                           "longitude": -51.08479139781439},
                           "name": "Núcleo de Tecnologia e Informática"},
                    "xerox":{"geolocation": {"latitude": -0.008218507124738528,
                             "longitude": -51.0850496714252},
                             "name": "Xerox"}
                }

        slot = tracker.get_slot("lugar")
        if slot is None or slot not in places:
            dispatcher.utter_message(text = "Desculpe, ainda não sei informar o local solicitado ou não entendi sua solicitação")
        elif slot in places:
            place = places[slot]["geolocation"]
            name = places[slot]["name"]
            dispatcher.utter_message(text = "Essas são as coordenadas que eu disponho para: {}".format(name), json_message = place)

        return[SlotSet("lugar", None)]
