# -*- coding: utf-8 -*-
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "english"


class Elements:
    def __init__(self, links, sentences_number):
        self.links = links
        self.sent_num = sentences_number

    def parsing(self):
            result = []
            for link in self.links:
                url = link
                parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
                stemmer = Stemmer(LANGUAGE)
                summarizer = Summarizer(stemmer)
                summarizer.stop_words = get_stop_words(LANGUAGE)

                for sentence in summarizer(parser.document, self.sent_num):
                    print(sentence)
                    result.append(sentence)
            return result