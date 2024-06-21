from tabulate import tabulate
from googletrans import Translator


class TranslateClass(object):
    def __init__(self, word, lang):
        self.word = word
        self.lang = lang
        self.Trans = Translator(service_urls=["translate.google.com"])

    def __repr__(self):
        translated = self.Trans.translate(self.word, dest=self.lang).text
        data = [
            ['Language:', "Word/Sentence"],
            ['English', self.word],
            ['Hindi', str(translated)]]
        table = str(tabulate(data, headers="firstrow", tablefmt="grid"))
        return table


if __name__ == '__main__':
    translate = input('Enter Word/Sentence...')
    language = 'hi'  # Translates to hindi
    #language = 'mr' # Translates to marathi
    print(TranslateClass(translate, language))