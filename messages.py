# messages.py

import random

MESSAGES = {
    "Capricornio": [
        "Capricornio es responsable y disciplinado.",
        "Capricornio es ambicioso y práctico.",
        "Capricornio es paciente y perseverante.",
        "Capricornio es realista y confiable.",
        "Capricornio es organizado y determinado."
    ],
    "Acuario": [
        "Acuario es innovador y original.",
        "Acuario es independiente y humanitario.",
        "Acuario es visionario y amable.",
        "Acuario es intelectual y progresista.",
        "Acuario es creativo y auténtico."
    ],
    "Piscis": [
        "Piscis es compasivo y artístico.",
        "Piscis es intuitivo y sensible.",
        "Piscis es amable y generoso.",
        "Piscis es imaginativo y sabio.",
        "Piscis es adaptable y soñador."
    ],
    "Aries": [
        "Aries es valiente y energético.",
        "Aries es entusiasta y seguro.",
        "Aries es competitivo y audaz.",
        "Aries es honesto y apasionado.",
        "Aries es líder natural y dinámico."
    ],
    "Tauro": [
        "Tauro es confiable y paciente.",
        "Tauro es práctico y decidido.",
        "Tauro es dedicado y estable.",
        "Tauro es amable y cariñoso.",
        "Tauro es perseverante y fuerte."
    ],
    "Géminis": [
        "Géminis es adaptable y curioso.",
        "Géminis es comunicativo y ingenioso.",
        "Géminis es sociable y versátil.",
        "Géminis es inteligente y divertido.",
        "Géminis es inquieto y expresivo."
    ],
    "Cáncer": [
        "Cáncer es protector y cariñoso.",
        "Cáncer es intuitivo y emocional.",
        "Cáncer es amable y leal.",
        "Cáncer es sensible y compasivo.",
        "Cáncer es imaginativo y afectuoso."
    ],
    "Leo": [
        "Leo es orgulloso y generoso.",
        "Leo es creativo y apasionado.",
        "Leo es valiente y dominante.",
        "Leo es optimista y divertido.",
        "Leo es líder nato y entusiasta."
    ],
    "Virgo": [
        "Virgo es analítico y meticuloso.",
        "Virgo es práctico y confiable.",
        "Virgo es perfeccionista y dedicado.",
        "Virgo es inteligente y modesto.",
        "Virgo es organizado y detallista."
    ],
    "Libra": [
        "Libra es diplomático y amable.",
        "Libra es justo y sociable.",
        "Libra es equilibrado y armonioso.",
        "Libra es encantador y cooperativo.",
        "Libra es pacífico y considerado."
    ],
    "Escorpio": [
        "Escorpio es apasionado y valiente.",
        "Escorpio es determinado y leal.",
        "Escorpio es intuitivo y profundo.",
        "Escorpio es misterioso y reservado.",
        "Escorpio es poderoso y decidido."
    ],
    "Sagitario": [
        "Sagitario es optimista y aventurero.",
        "Sagitario es honesto y filosófico.",
        "Sagitario es entusiasta y libre.",
        "Sagitario es generoso y divertido.",
        "Sagitario es curioso y abierto."
    ],
}

def get_random_message(sign):
    messages = MESSAGES.get(sign)
    if messages:
        return random.choice(messages)
    else:
        return "No hay mensajes disponibles para este signo."
