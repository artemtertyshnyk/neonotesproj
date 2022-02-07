import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector


def ner(text):
    nlp = spacy.load('en_core_web_md')

    def set_language(language):
        if language == 'en':
            return spacy.load(language + '_core_web_md')
        else:
            return spacy.load(language + '_core_news_md')

    def get_lang_detector(nlp, name):
        return LanguageDetector()

    Language.factory("language_detector", func=get_lang_detector)
    nlp.add_pipe('language_detector', last=True)
    doc = nlp(text)

    nlp = set_language(doc._.language['language'])
    doc = nlp(text)

    result = {}

    if doc.ents:
        for t in doc.ents:
            result[t.text] = t.label_
    else:
        print('Your text has no entities')

    return result
