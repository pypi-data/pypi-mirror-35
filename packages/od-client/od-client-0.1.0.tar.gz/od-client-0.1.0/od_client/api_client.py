import logging

import requests

from typing import List
from urllib.parse import urljoin

from .utils import OdFilter
from .enums import OdEndpoint, LexiStatsSort, LexiStatsCollate, LexiStatsTokenFormat

logger = logging.getLogger(__name__)

DEFAULT_PAGINATION_LIMIT = 5000
OXFORD_DICTIONARIES_API_ROOT = "https://od-api.oxforddictionaries.com/api/v1"


class OxfordDictionariesApiClient(object):
    def __init__(self, app_id, app_key, api_root=OXFORD_DICTIONARIES_API_ROOT):
        self.__app_id = app_id
        self.__app_key = app_key
        self._api_root = api_root
        self.session = requests.Session()
        self.session.headers.update(
            {"app_id": self.__app_id, "app_key": self.__app_key}
        )

    def get(self, url: str, **kwargs) -> requests.Response:
        return self.session.get(urljoin(self._api_root, url), **kwargs)

    # region Lemmatron
    def get_inflections(self, source_language: str, word: str) -> requests.Response:
        return self.get(f"/inflections/{source_language}/{word}")

    def get_inflections_filtered(
        self, source_language: str, word: str, filters: OdFilter
    ) -> requests.Response:
        return self.get(
            f"/inflections/{source_language}/{word}/{filters.representation}"
        )

    # endregion

    # region Dictionary entries
    def get_dictionary_entry(
        self, source_language: str, word: str
    ) -> requests.Response:
        return self.get(f"/entries/{source_language}/{word}")

    def get_dictionary_entry_by_regions(
        self, source_language: str, word: str, region: str
    ) -> requests.Response:
        return self.get(f"/entries/{source_language}/{word}/regions={region}")

    def get_dictionary_entry_filtered(
        self, source_language: str, word: str, filters: OdFilter
    ) -> requests.Response:
        return self.get(f"/entries/{source_language}/{word}/{filters.representation}")

    # endregion

    # region Thesaurus
    def get_synonyms(self, source_language: str, word: str) -> requests.Response:
        return self.get(f"/entries/{source_language}/{word}/synonyms")

    def get_antonyms(self, source_language: str, word: str) -> requests.Response:
        return self.get(f"/entries/{source_language}/{word}/antonyms")

    def get_synonyms_and_antonyms(
        self, source_language: str, word: str
    ) -> requests.Response:
        return self.get(f"/entries/{source_language}/{word}/synonyms;antonyms")

    # endregion

    # region Search
    def get_monolingual_matches(
        self,
        source_language: str,
        query_string: str,
        prefix: bool = False,
        regions: str = None,
        limit: int = DEFAULT_PAGINATION_LIMIT,
        offset: int = 0,
    ) -> requests.Response:
        params = {"q": query_string, "prefix": prefix, "limit": limit, "offset": offset}
        if regions:
            params["regions"] = regions
        return self.get(f"/search/{source_language}", params=params)

    def get_bilingual_matches(
        self,
        source_search_language: str,
        target_search_language: str,
        query_string: str,
        prefix: bool = False,
        limit: int = DEFAULT_PAGINATION_LIMIT,
        offset: int = 0,
    ) -> requests.Response:
        return self.get(
            f"/search/{source_search_language}/translations={target_search_language}",
            params={
                "q": query_string,
                "prefix": prefix,
                "limit": limit,
                "offset": offset,
            },
        )

    # endregion

    # region Translation
    def get_translation(
        self,
        source_translation_language: str,
        target_translation_language: str,
        word: str,
    ) -> requests.Response:
        return self.get(
            f"/entries/{source_translation_language}/{word}/{target_translation_language}"
        )

    # endregion

    # region Wordlist
    def get_word_list(
        self, source_language: str, filters_basic: OdFilter, limit=5000, offset=0
    ) -> requests.Response:
        return self.get(
            f"/wordlist/{source_language}/{filters_basic.representation}",
            params={"limit": limit, "offset": offset},
        )

    def get_word_list_advanced(
        self,
        source_language: str,
        filters_advanced: OdFilter,
        exclude_filter: OdFilter = None,
        exclude_senses_filter: OdFilter = None,
        exclude_prime_senses_filter: OdFilter = None,
        word_length: str = None,
        prefix: str = None,
        exact: bool = False,
        limit=5000,
        offset=0,
    ) -> requests.Response:
        params = {"limit": limit, "offset": offset, "exact": exact}
        for key, value in {
            "word_length": word_length,
            "prefix": prefix,
            "exclude": exclude_filter.representation,
            "exclude_senses": exclude_senses_filter.representation,
            "exclude_prime_senses": exclude_prime_senses_filter.representation,
        }.items():
            if value is not None:
                params["key"] = value
        return self.get(
            f"/wordlist/{source_language}/{filters_advanced.representation}",
            params=params,
        )

    # endregion

    # region The Sentence Dictionary
    def get_sentences(self, source_language: str, word: str) -> requests.Response:
        return self.get(f"/entries/{source_language}/{word}/sentences")

    # endregion

    # region LexiStats
    def get_word_frequency(
        self,
        source_language: str,
        corpus: str = "nmc",
        word_form: str = None,
        true_case: str = None,
        lemma: str = None,
        lexical_category: str = None,
    ) -> requests.Response:
        params = {"corpus": corpus}
        for key, value in {
            "wordform": word_form,
            "trueCase": true_case,
            "lemma": lemma,
            "lexicalCategory": lexical_category,
        }.items():
            if value is not None:
                params[key] = value
        return self.get(f"/stats/frequency/word/{source_language}/", params=params)

    def get_words_frequency(
        self,
        source_language: str,
        corpus: str = "nmc",
        word_form: str = None,
        true_case: str = None,
        lemma: str = None,
        lexical_category: str = None,
        grammatical_features: str = None,
        sort: List[LexiStatsSort] = None,
        collate: List[LexiStatsCollate] = None,
        min_frequency: int = None,
        max_frequency: int = None,
        min_normalized_frequency: float = None,
        max_normalized_frequency: float = None,
        offset: int = 0,
        limit: int = 100,
    ) -> requests.Response:
        """Todo: grammatical_features - add a class with representation for k:v list"""
        sort = ",".join((enm.value for enm in sort)) if sort else sort
        collate = ",".join((enm.value for enm in collate)) if collate else None
        params = {"corpus": corpus, "offset": offset, "limit": limit}
        for key, value in {
            "wordform": word_form,
            "trueCase": true_case,
            "lemma": lemma,
            "lexicalCategory": lexical_category,
            "grammaticalFeatures": grammatical_features,
            "sort": sort,
            "collate": collate,
            "minFrequency": min_frequency,
            "maxFrequency": max_frequency,
            "minNormalizedFrequency": min_normalized_frequency,
            "maxNormalizedFrequency": max_normalized_frequency,
        }.items():
            if value is not None:
                params[key] = value
        return self.get(f"/stats/frequency/words/{source_language}/", params=params)

    def get_ngrams_frequency(
        self,
        source_language: str,
        ngram_size: int,
        corpus: str = "nmc",
        tokens: List[str] = None,
        contains_tokens: List[str] = None,
        punctuation: bool = False,
        token_format: LexiStatsTokenFormat = None,
        sort: List[LexiStatsSort] = None,
        collate: List[LexiStatsCollate] = None,
        min_frequency: int = None,
        max_frequency: int = None,
        min_document_frequency: float = None,
        max_document_frequency: float = None,
        offset: int = 0,
        limit: int = 100,
    ) -> requests.Response:
        """Todo: grammatical_features - add a class with representation for k:v list"""
        sort = ",".join((enm.value for enm in sort)) if sort else sort
        collate = ",".join((enm.value for enm in collate)) if collate else None
        tokens = ",".join(tokens) if tokens else None
        contains_tokens = ",".join(contains_tokens) if contains_tokens else None
        params = {"offset": offset, "limit": limit}
        for key, value in {
            "tokens": tokens,
            "contains": contains_tokens,
            "punctuation": punctuation,
            "format": token_format.value,
            "sort": sort,
            "collate": collate,
            "minFrequency": min_frequency,
            "maxFrequency": max_frequency,
            "minDocumentFrequency": min_document_frequency,
            "maxDocumentFrequency": max_document_frequency,
        }.items():
            if value is not None:
                params[key] = value
        return self.get(
            f"/stats/frequency/ngrams/{source_language}/{corpus}/{ngram_size}/",
            params=params,
        )

    # endregion

    # region Utils
    def get_languages(self) -> requests.Response:
        return self.get("/languages")

    def get_filters(self) -> requests.Response:
        return self.get("/filters")

    def get_endpoint_filters(self, endpoint: OdEndpoint) -> requests.Response:
        return self.get(f"/filters/{endpoint.value}")

    def get_lexical_categories(self, language: str) -> requests.Response:
        return self.get(f"/lexicalcategories/{language}")

    def get_monolingual_registers(self, source_language: str) -> requests.Response:
        return self.get(f"/registers/{source_language}")

    def get_bilingual_registers(
        self, source_register_language: str, target_register_language: str
    ) -> requests.Response:
        return self.get(
            f"/registers/{source_register_language}/{target_register_language}"
        )

    def get_monolingual_domains(self, source_language: str) -> requests.Response:
        return self.get(f"/domains/{source_language}")

    def get_bilingual_domains(
        self, source_domains_language: str, target_domains_language: str
    ) -> requests.Response:
        return self.get(f"/domains/{source_domains_language}/{target_domains_language}")

    def get_regions(self, source_language: str) -> requests.Response:
        return self.get(f"/domains/{source_language}")

    def get_grammatical_features(self, source_language: str) -> requests.Response:
        return self.get(f"/grammaticalFeatures/{source_language}")

    # endregion
