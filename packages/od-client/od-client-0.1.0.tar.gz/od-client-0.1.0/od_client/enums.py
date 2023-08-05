from enum import Enum


class OdEndpoint(Enum):
    entries = "entries"
    inflections = "inflections"
    translations = "translations"


class LexiStatsSort(Enum):
    word_form_asc = "wordform"
    true_case_asc = "trueCase"
    lemma_asc = "lemma"
    lexical_category_asc = "lexicalCategory"
    frequency_asc = "frequency"
    normalized_frequency_asc = "normalizedFrequency"

    word_form_desc = "-wordform"
    true_case_desc = "-trueCase"
    lemma_desc = "-lemma"
    lexical_category_desc = "-lexicalCategory"
    frequency_desc = "-frequency"
    normalized_frequency_desc = "-normalizedFrequency"


class LexiStatsCollate(Enum):
    word_form = "wordform"
    true_case = "trueCase"
    lemma = "lemma"
    lexical_category = "lexicalCategory"


class LexiStatsTokenFormat(Enum):
    google = ("google",)
    oup = "oup"
