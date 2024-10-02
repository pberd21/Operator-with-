import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for ch in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(ch, ' ')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        word_positions = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                word_positions[file_name] = words.index(word) + 1
            else:
                word_positions[file_name] = None
        return word_positions

    def count(self, word):
        word = word.lower()
        word_counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))