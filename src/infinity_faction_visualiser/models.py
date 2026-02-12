from collections import OrderedDict
from dataclasses import dataclass
from enum import Enum
import pathlib


class Army(str, Enum):
    PANO = 'PanO'
    JSA = 'JSA'
    ALEPH = 'Aleph'
    NOMADS = 'Nomads'
    HAQQISLAM = 'Haqqislam'
    TOHAA = 'Tohaa'
    COMBINED_ARMY = 'Combined Army'
    ARIADNA = 'Ariadna'
    NA2 = 'NA2'
    O12 = 'O-12'
    YU_JING = 'Yu Jing'

class Sectorial(str, Enum):
    PANOCEANIA = "PanOceania"
    MILITARY_ORDERS = "Military Orders"
    NEOTERRAN_CAPITALINE_ARMY = "Neoterran Capitaline Army"
    SVALARHEIMAS_WINTER_FORCE = "Svalarheima's Winter Force"
    KESTREL_COLONIAL_FORCE = "Kestrel Colonial Force"
    SHOCK_ARMY_OF_ACONTECIMENTO = "Shock Army of Acontecimento"
    VARUNA_IMMEDIATE_REACTION_DIVISION = "Varuna Immediate Reaction Division"

    JSA = "JSA"
    SHINDENBUTAI = "Shindenbutai"
    OBAN = "Oban"

    ALEPH = "Aleph"
    STEEL_PHALANX = "Steel Phalanx"
    OPERATIONS_SUBSECTION_OF_THE_SSS = "Operations Subsection of the SSS"

    NOMADS = "Nomads"
    JURISDICTIONAL_COMMAND_OF_CORREGIDOR = "Jurisdictional Command of Corregidor"
    JURISDICTIONAL_COMMAND_OF_BAKUNIN = "Jurisdictional Command of Bakunin"
    JURISDICTIONAL_COMMAND_OF_TUNGUSKA = "Jurisdictional Command of Tunguska"

    HAQQISLAM = "Haqqislam"
    HASSASSHIN_BAHRAM = "Hassasshin Bahram"
    QAPU_KHALQI = "Qapu Khalqi"
    RAMAH_TASKFORCE = "Ramah Taskforce"

    TOHAA = "Tohaa"

    COMBINED_ARMY = "Combined Army"
    MORAT_AGRESSION_FORCE = "Morat Agression Force"
    ONYX_CONTACT_FORCE = "Onyx Contact Force"
    NEXT_WAVE = "Next Wave"
    SHASVASTII_EXPEDITIONARY_FORCE = "Shasvastii Expeditionary Force"

    ARIADNA = "Ariadna"
    FORCE_DE_REPONSE_RAPIDE_MEROVINGIENNE = "Force de Réponse Rapide Merovingienne"
    TARTARY_ARMY_CORPS = "Tartary Army Corps"
    KOSMOFLOT = "Kosmoflot"
    CALEDONIAN_HIGHLANDER_ARMY = "Caledonian Highlander Army"
    USARIADNA_RANGER_FORCE = "USAriadna Ranger Force"

    DRUZE_BAYRAM_SECURITY = "Druze Bayram Security"
    IKARI_COMPANY = "Ikari Company"
    STARCO_FREE_COMPANY_OF_THE_STAR = "Starco. Free Company of the Star"
    DASHAT_COMPANY = "Dashat Company"
    WHITE_COMPANY = "White Company"

    O_12 = "O-12"
    STARMADA = "Starmada"
    TORCHLIGHT_BRIGADE = "Torchlight Brigade"

    YU_JING = "Yu Jing"
    IMPERIAL_SERVICE = "Imperial Service"
    INVINCIBLE_ARMY = "Invincible Army"
    WHITE_BANNER = "White Banner"

SECTORIALS_BY_ARMY: OrderedDict[Army, tuple[Sectorial, ...]] = OrderedDict([
    (
        Army.PANO,
        (
            Sectorial.PANOCEANIA,
            Sectorial.MILITARY_ORDERS,
            Sectorial.NEOTERRAN_CAPITALINE_ARMY,
            Sectorial.SVALARHEIMAS_WINTER_FORCE,
            Sectorial.KESTREL_COLONIAL_FORCE,
            Sectorial.SHOCK_ARMY_OF_ACONTECIMENTO,
            Sectorial.VARUNA_IMMEDIATE_REACTION_DIVISION,
        ),
    ),
    (
        Army.JSA,
        (
            Sectorial.JSA,
            Sectorial.SHINDENBUTAI,
            Sectorial.OBAN,
        ),
    ),
    (
        Army.ALEPH,
        (
            Sectorial.ALEPH,
            Sectorial.STEEL_PHALANX,
            Sectorial.OPERATIONS_SUBSECTION_OF_THE_SSS,
        ),
    ),
    (
        Army.NOMADS,
        (
            Sectorial.NOMADS,
            Sectorial.JURISDICTIONAL_COMMAND_OF_CORREGIDOR,
            Sectorial.JURISDICTIONAL_COMMAND_OF_BAKUNIN,
            Sectorial.JURISDICTIONAL_COMMAND_OF_TUNGUSKA,
        ),
    ),
    (
        Army.HAQQISLAM,
        (
            Sectorial.HAQQISLAM,
            Sectorial.HASSASSHIN_BAHRAM,
            Sectorial.QAPU_KHALQI,
            Sectorial.RAMAH_TASKFORCE,
        ),
    ),
    (
        Army.TOHAA,
        (
            Sectorial.TOHAA,
        ),
    ),
    (
        Army.COMBINED_ARMY,
        (
            Sectorial.COMBINED_ARMY,
            Sectorial.MORAT_AGRESSION_FORCE,
            Sectorial.ONYX_CONTACT_FORCE,
            Sectorial.NEXT_WAVE,
            Sectorial.SHASVASTII_EXPEDITIONARY_FORCE,
        ),
    ),
    (
        Army.ARIADNA,
        (
            Sectorial.ARIADNA,
            Sectorial.FORCE_DE_REPONSE_RAPIDE_MEROVINGIENNE,
            Sectorial.TARTARY_ARMY_CORPS,
            Sectorial.KOSMOFLOT,
            Sectorial.CALEDONIAN_HIGHLANDER_ARMY,
            Sectorial.USARIADNA_RANGER_FORCE,
        ),
    ),
    (
        Army.NA2,
        (
            Sectorial.DRUZE_BAYRAM_SECURITY,
            Sectorial.IKARI_COMPANY,
            Sectorial.STARCO_FREE_COMPANY_OF_THE_STAR,
            Sectorial.DASHAT_COMPANY,
            Sectorial.WHITE_COMPANY,
        ),
    ),
    (
        Army.O12,
        (
            Sectorial.O_12,
            Sectorial.STARMADA,
            Sectorial.TORCHLIGHT_BRIGADE,
        ),
    ),
    (
        Army.YU_JING,
        (
            Sectorial.YU_JING,
            Sectorial.IMPERIAL_SERVICE,
            Sectorial.INVINCIBLE_ARMY,
            Sectorial.WHITE_BANNER,
        ),
    ),
])

COLOR_CODING: dict[ Army, str] = {
    Army.PANO: "#00b0f2",
    Army.JSA: "#a6112b",
    Army.ALEPH: "#afa7bc",
    Army.NOMADS: "#ce181f",
    Army.HAQQISLAM: "#e6da9b",
    Army.TOHAA: "#3b3b3b",
    Army.COMBINED_ARMY: "#400b5f",
    Army.ARIADNA: "#007d27",
    Army.NA2: "#728868",
    Army.O12: "#005470",
    Army.YU_JING: "#ff9000"
}

@dataclass
class FactionSpread:
    tournament_name: str
    output_folder: pathlib.Path
    played_sectorials: dict[Sectorial, int]
