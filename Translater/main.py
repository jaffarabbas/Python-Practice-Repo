from translate import Translator

try:
    translater = Translator(to_lang="Greek")
    translation = translater.translate("Hii")
    print(translation)
except Exception as e:
    print(e)