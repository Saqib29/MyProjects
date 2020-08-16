from googletrans import Translator, constants
from pprint import pprint

# initializing google api translator

translator = Translator()  # creating instance

# here two optional parameter can be "src" and "dest"
translation = translator.translate("Wie gehts ?", src="de")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

pprint(translation.extra_data)

sentence = [
    "Hello everyone",
    "How are you",
    "Do you speak english?",
    "Good bye!"
]

translations = translator.translate(sentence, dest='bn')
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# for language detection
detection = translator.detect("ওহে")
print("klanguage code: ", detection.lang)
print("Confidence: ", detection.confidence)
print()
print("Language: ", constants.LANGUAGES[detection.lang])

# all list of languages of language code
pprint(constants.LANGUAGES)
print()
print("Total supported languages:", len(constants.LANGUAGES))
