# open and read a text file
text = open('HarryPotter.txt','r')
text = text.read()

# print a text fle
print(text)

# perform basic operations on the content
sentences = text.split('.')
for sentence in sentences:
    if 'Harry' in sentence:
        print(sentence)
