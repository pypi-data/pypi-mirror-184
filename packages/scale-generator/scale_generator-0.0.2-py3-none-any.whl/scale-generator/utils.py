import json
import logging

logger = logging.getLogger("ScaleGeneratorLogger")
logger.setLevel("WARNING")

NATURAL_C = 261.6
NATURAL_D = 293.6
NATURAL_E = 329.6
NATURAL_F = 349.2
NATURAL_G = 392.0
NATURAL_A = 440.0
NATURAL_B = 493.9

NOTE_NAMES = {
    "occidental": ('C', 'D', 'E', 'F', 'G', 'A', 'B'),
    "romanian": ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'),
    "byzantine": ('Ni', 'Pa', 'Vu', 'Ga', 'Di', 'Ke', 'Zo')
}

config = {
    "default_scales": {
        "temperate": {
            "info": {
                "name": "Scara temperată",
                "sections": 12
            },
            "values": {
                "base": ("La", NATURAL_A),
                "notes": NOTE_NAMES["romanian"],
                "intervals": (2, 2, 1, 2, 2, 2, 1),
            }
        },
        "1": {
            "info": {
                "name": "Glasul întâi diatonic",
                "sections": 72
            },
            "values": {
                "base": ("Ke", NATURAL_A),
                "notes": NOTE_NAMES["byzantine"],
                "intervals": (12, 10, 8, 12, 12, 10, 8),
            }
        },
        "2": {},
        "3": {},
        "4": {},
        "5": {},
        "6": {},
        "7": {},
        "8": {},
    }
}

try:
    with open("config.json") as conf:
        config.update(json.loads(conf.read()))
except FileNotFoundError as err:
    logger.warning(err)
