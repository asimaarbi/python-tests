

def flip_word (sentence):

     return' '.join(word[::-1] for word in sentence.split(" "))
sentence = 'How are you ?'

print(flip_word(sentence))
