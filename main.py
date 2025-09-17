# Case-study #3
# Developers: Sedelnikova P., Simonov A., Fedotova M.
#
from textblob import TextBlob
import ru_local as ru


def count_syllables(word, language):
    """Counting syllables for words"""
    syllables = 0
    vowels = 'aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    for i in range(len(text)):
        if text[i] in vowels:
            syllables += 1


def detect_language(text):
    """Text language detection"""
    text_str = str(text)
    en_chars = sum(1 for c in text_str
                   if 'a' <= c <= 'z' or 'A' <= c <= 'Z')
    ru_chars = sum(1 for c in text_str
                   if 'а' <= c <= 'я' or 'А' <= c <= 'Я' or c in 'ёЁ')

    return 'en' if en_chars > ru_chars else 'ru'


def flesch_interpretation(score, language):
    """Interpretation of the Flush index"""
    if language == 'en':
        if score >= 90:
            return ru.VERY_EASY
        elif score >= 80:
            return ru.EASY
        elif score >= 70:
            return ru.PRETTY_EASY
        elif score >= 60:
            return ru.ORDINARY
        elif score >= 50:
            return ru.QUITE_DIFFICULT
        elif score >= 30:
            return ru.DIFFICULT
        else:
            return ru.VERY_DIFFICULT
    else:
        if score >= 80:
            return ru.EASY
        elif score >= 70:
            return ru.PRETTY_EASY
        elif score >= 60:
            return ru.ORDINARY
        elif score >= 50:
            return ru.QUITE_DIFFICULT
        elif score >= 30:
            return ru.DIFFICULT
        else:
            return ru.VERY_DIFFICULT


def main():
    text = input(ru.TEXT)
    blob = TextBlob(text)

    language = detect_language(text)

    sentences = len(blob.sentences)
    words = len(blob.words)

    syllables = sum(count_syllables(word, language) for word in blob.words)

    average_sentence_length = words / sentences
    average_word_length = syllables / words

    if language == 'en':
        flash_index = (206.835 - (1.015 * average_sentence_length) -
                       (84.6 * average_word_length))
    else:
        flash_index = (206.835 - (1.52 * average_sentence_length) -
                       (65.14 * average_word_length))

    positive_words = [
        ru.GOOD, ru.EXCELLENT, ru.BEAUTIFUL,
        ru.WONDERFUL, ru.LOVE, ru.LIKE
    ]
    negative_words = [
        ru.BAD, ru.TERRIBLE, ru.DISGUSTING,
        ru.HATE, ru.NOT_LIKE
    ]

    text_words = [str(word).lower() for word in blob.words]

    positive_count = sum(1 for word in text_words if word in positive_words)
    negative_count = sum(1 for word in text_words if word in negative_words)

    if positive_count > negative_count:
        sentiment = ru.POSITIVE
    elif negative_count > positive_count:
        sentiment = ru.NEGATIVE
    else:
        sentiment = ru.NEUTRAL

    objectivity = (1 - blob.subjectivity) * 100

    print(f'{ru.OFFERS}\n{sentences}')
    print(f'{ru.WORDS} {words}')
    print(f'{ru.SYLLABLES} {syllables}')
    print(f'{ru.AVERAGE_LENGTH_OFFERS} {average_sentence_length:.2f}')
    print(f'{ru.AVERAGE_LENGTH_WORDS} {average_word_length:.2f}')
    print(f'{ru.INDEX} {flash_index:.2f}')
    print(flesch_interpretation(flash_index, language) + '.')
    print(f'{ru.TONALITY} {sentiment}')
    print(f'{ru.OBJECTIVITY} {objectivity:.1f}%')


if __name__ == '__main__':
    main()