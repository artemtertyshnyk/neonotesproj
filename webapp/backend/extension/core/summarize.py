from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

GIVEN_PERCENTAGE = .5

def summarize(text, percentage):
    summarized_text = []
    GIVEN_PERCENTAGE = percentage / 100
    LANGUAGE = 'english'

    sentences = list(Tokenizer(LANGUAGE).to_sentences(text))

    result_length = int(len(sentences) * GIVEN_PERCENTAGE) + 1

    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sent in summarizer(parser.document, result_length):
        str1 = str(sent).replace(u'\xa0', u' ')
        summarized_text.append(str1)

    return " ".join(summarized_text)
