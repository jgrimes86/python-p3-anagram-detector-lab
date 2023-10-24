# your code goes here!
import ipdb

class Anagram:
    def __init__(self, word):
        self.word = word

    def map_maker(self, string):
        string_map = {}
        i = 0
        while i < len(string):
            if string_map.get(string[i], False):
                string_map[string[i]] += 1
            else:
                string_map[string[i]] = 1
            i += 1
        return string_map

    def anagram_checker(self, possible_anagram):
        if len(self.word) != len(possible_anagram):
            return False
        word_map = self.map_maker(self.word)
        possible_map = self.map_maker(possible_anagram)
        for key in word_map:
            if not possible_map.get(key, False):
                return False
        return True

    def match(self, possible_anagram_list):
        anagram_list = [option for option in possible_anagram_list if self.anagram_checker(option)]
        return anagram_list


listen = Anagram("listen")
options = ['enlists', 'google', 'inlets', 'banana']

# ipdb.set_trace()

print(listen.match(options))