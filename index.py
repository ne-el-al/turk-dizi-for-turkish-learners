import string

# installing and setting up turkicnlp
import turkicnlp

# set up the NLP pipeline for Turkish language with specified processors
nlp = turkicnlp.Pipeline("tur", processors=["tokenize", "pos", "lemma"], backend="stanza")

# empty list for lines without minutes and seconds
transcript_clear = []


#processing the transcript file to remove time stamps and clean the text

# open file
with open("transcript.txt", "r") as transcript:
    transcript = list(transcript)

    #loop to remove beginning timeline count 
    for line in transcript:
        minute_index = line.find("minute")
        second_index = line.find("second")
        hour_index = line.find("hour")

        # hour > minute > second, which gets the biggest index, gets to be final number to remove the front-trailing time 
        if second_index > minute_index:
            line = line[second_index+len("second")+1:]
        elif minute_index > second_index:
            line = line[minute_index+len("minute")+1:]
        else:
            line = line[hour_index+len("hour")+1:]

        # clean line from punctuaton and extra spaces + lowercasing words
        line = ''.join([char for char in line if char not in string.punctuation]).lower().strip("\n")

        # add clean line to the transcript
        transcript_clear.append(line)

transcript_lemma_list = []

# loop through each sentence in the transcript and get the lemma of each word
for sentence in transcript_clear:
    # get lemma of each word
    doc = nlp(sentence)
    for word in doc.words:
        lemma = word.lemma
        transcript_lemma_list.append(lemma)
 
# counting occurences of each word
trasncript_dict = dict((word, transcript_lemma_list.count(word)) for word in set(transcript_lemma_list))

# sort transcript from biggest to smallest
trasncript_dict = dict(sorted(trasncript_dict.items(), key=lambda item: item[1], reverse=True))

print(trasncript_dict.items())

"""
TO DO:
- load dictionary in file
✔️ find way to get clean verb form
- get 2, 3, 4...-word phrases 
"""