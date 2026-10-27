import string

# empty list for lines without minutes and seconds
transcript_clear = []

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
            line = line[second_index+len("seconds")+1:]
        elif minute_index > second_index:
            line = line[minute_index+len("minute")+1:]
        else:
            line = line[hour_index+len("hour")+1:]

        # clean line from punctuaton and extra spaces + lowercasing words
        line = ''.join([char for char in line if char not in string.punctuation]).lower()

        # add clean line to the transcript
        transcript_clear.append(line)

# making sorted list of words
transcript_word_list = sorted(" ".join(transcript_clear).split())

# counting occurences of each word
trasncript_dict = dict((word, transcript_word_list.count(word)) for word in set(transcript_word_list))

# sort transcript from biggest to smallest
trasncript_dict = dict(sorted(trasncript_dict.items(), key=lambda item: item[1], reverse=True))

print(trasncript_dict)

# for word in trasncript_dict.items():
#     print(word)

"""
TO DO:
- load dictionary in file
- find way to get clean verb form
- get 2, 3, 4...-word phrases 
"""
