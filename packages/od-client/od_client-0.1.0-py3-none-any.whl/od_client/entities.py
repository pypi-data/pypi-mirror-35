from collections import namedtuple

Language = namedtuple("Language", ["id", "name"])
LanguageResult = namedtuple(
    "Language", ["region", "source", "source_language", "target_language", "type"]
)
