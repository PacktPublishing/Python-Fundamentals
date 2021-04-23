text = open('blankText.txt', 'r+')


# create a file that we car write text to
for i in range(0,11):
    text.write(str(i)+30*' ')
    text.write('\n')

text.write('The End')
text.seek(0)
text.write('The Start')
# write a sequence of numbers each on a new line

# write a note at the start and the end of sequence
