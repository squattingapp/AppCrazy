import string
import os

import itertools

vowel = ['a', 'e', 'o', 'i', 'u']
punctuation = [' ', '-', '_']
r_punctuation = ['.', ' ', '_']
common_letter_replace_dic = {'b':'p','i':'1,l',"l":'i,1',"o":'0','c':'k','k':'c','p':'b','m':'n','n':'m','s':'5'}

prefix_list = []
file_name = os.getcwd() + os.path.sep + "prefix.txt"
file_obj = open(file_name,"rU")
try:
    for line in file_obj:
        prefix_list.append(line.rstrip("\n"))
finally:
    file_obj.close()

class DeformationMethod:
    """generate appname or packagename variants"""

    def __init__(self, ori_name):
        self.ori_name = ori_name
        self.variant_dic = {}
        self.length = len(self.ori_name)

    def appname_deformation(self):
        self.vowel_character_deletion()
        self.vowel_character_insertion()
        self.vowel_character_substitution()
        self.double_character_deletion()
        self.double_character_insertion()
        self.common_misspelling_mistakes_substition()
        self.puncatuation_deletion()
        self.puncatuation_substitution()
        if (self.ori_name in self.variant_dic.keys()) or (self.ori_name.lower() in self.variant_dic.keys()):
            self.variant_dic.pop(self.ori_name)

    def packagename_deformation(self):
        self.vowel_character_deletion()
        self.vowel_character_insertion()
        self.vowel_character_substitution()
        self.double_character_deletion()
        self.double_character_insertion()
        self.common_misspelling_mistakes_substition()
        self.puncatuation_deletion()
        self.puncatuation_substitution()
        self.string_rearrangement()
        if (self.ori_name in self.variant_dic.keys()) or (self.ori_name.lower() in self.variant_dic.keys()):
            self.variant_dic.pop(self.ori_name)

    def vowel_character_insertion(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in vowel:
                for r_letter in vowel:
                    word = self.ori_name.lower()
                    word = word[0:i] + r_letter + word[i:]
                    self.variant_dic[word] = 'vowel_character_insertion'

    def vowel_character_deletion(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in vowel:
                word = word[0:i] + word[i+1:]
                self.variant_dic[word] = 'vowel_character_deletion'

    def vowel_character_substitution(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in vowel:
                for r_letter in vowel:
                    word = self.ori_name.lower()
                    if r_letter != word[i]:
                        word = word[0:i] + r_letter + word[i+1:]
                        self.variant_dic[word] = 'vowel_character_substitution'

    def double_character_insertion(self):
        for i in range(0,self.length-1):
            word = self.ori_name.lower()
            if word[i] == word[i + 1]:
                word = word[0:i] + word[i] + word[i:]
                self.variant_dic[word] = 'double_character_insertion'

    def double_character_deletion(self):
        for i in range(0,self.length-1):
            word = self.ori_name.lower()
            if word[i] == word[i + 1]:
                word = word[0:i] + word[i+1:]
                self.variant_dic[word] = 'double_character_deletion'
                word = word[0:i] + word[i + 1:]
                self.variant_dic[word] = 'double_character_deletion'

    def puncatuation_substitution(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in punctuation:
                for r_letter in punctuation:
                    word = self.ori_name.lower()
                    if r_letter != word[i]:
                        word = word[0:i] + r_letter +word[i+1:]
                        self.variant_dic[word] = 'puncatuation_substitution'
                        word = self.ori_name.lower()
                        word = word.replace(" ", r_letter)
                        word = word.replace("_", r_letter)
                        word = word.replace(".", r_letter)
                        self.variant_dic[word] = 'puncatuation_substitution'

    def puncatuation_deletion(self):
        for i in range(0,self.length):
            word = self.ori_name.lower()
            if word[i] in punctuation:
                word = word[0:i] + word[i + 1:]
                self.variant_dic[word] = 'puncatuation_deletion'
        word = self.ori_name.lower()
        word = word.replace(" ", "")
        word = word.replace("_", "")
        word = word.replace(".", "")
        self.variant_dic[word] = 'puncatuation_deletion'

    def common_misspelling_mistakes_substition(self):
        for i in range(0, self.length):
            for key in common_letter_replace_dic.keys():
                word = self.ori_name.lower()
                if word[i] == key:
                    letter = word[i]
                    values = common_letter_replace_dic.get(key)
                    if ',' in values:
                        value = values.split(',')
                        for val in value:
                            word = self.ori_name.lower()
                            word = word[0:i] + val + word[i + 1:]
                            self.variant_dic[word] = 'misspelling_mistakes_substition'
                            word = word.replace(letter,val)
                            self.variant_dic[word] = 'misspelling_mistakes_substition'
                    else:
                        word = word[0:i] + values + word[i + 1:]
                        self.variant_dic[word] = 'misspelling_mistakes_substition'
                        word = word.replace(letter, values)
                        self.variant_dic[word] = 'misspelling_mistakes_substition'

    def string_rearrangement(self):
        word_list = self.ori_name.split(".")
        length = len(word_list)
        number = []
        for i in range(0, length):
            number.append(i)
        if length - 2 > 1:
            start = length - 2
        else:
            start = 1
        for le in range(start, length):
            numberlist = list(itertools.permutations(number, le + 1))
            for numberls in numberlist:
                newword = ''
                for num in numberls:
                    newword = newword + word_list[num] + '.'
                self.variant_dic[newword.rstrip('.')] = 'string_rearrangement'

        for dele in ['com.android', 'com.google', 'android.com', 'google.com', 'com.game', 'game.com',
                     'com.google.android', 'com.music', 'music.com', 'google.android', 'android.google']:
            flag = True
            while flag == True:
                if dele in self.variant_dic.keys():
                    flag = True
                    self.variant_dic.pop(dele)
                else:
                    flag = False