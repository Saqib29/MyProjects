project_file = open("files/project_twitter_data.csv", "r") # file will be open as read only
result_file = open("files/resulted_file.csv", "w")  # file will be created as resulted_file.csv as write only

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@'] 
def removePunctuations(text):
    for p in punctuation_chars:
        text = text.replace(p, "") # checking every punctuations, if present to the text, replacing it by empty string
    
    return text

# reads positive words from positive_words.txt file
positive_words = []
with open("files/positive_words.txt", "r") as pos_words:
    for lines in pos_words:
        if lines[0] != ";" and lines[0] != '\n':   # checking if every line not starts with ";" of "\n"(new line)
            positive_words.append(lines.strip())  # here strip used to save words from unnecessary spaces and added to the list only words
            

# getting negative words to a list from negative_words.txt file placed in files folder
negative_words = []
with open("files/negative_words.txt", "r") as neg_words:
    for lines in neg_words:
        if lines[0] != ";" and lines[0] != "\n":
            negative_words.append(lines.strip()) # same thing did here, described above 

def count_positives(text):
    texts = removePunctuations(text)
    words = texts.strip().split()
    cnt = 0
    for word in words:
        if word in positive_words:
            cnt += 1                    # counting if positive words presents to the tweet or not, if present count increses
    
    return cnt                          # returning for the positive words in the tweet


def count_negatives(text):
    texts = removePunctuations(text)
    words = texts.strip().split()
    cnt = 0

    for word in words:
        if word in negative_words:
            cnt += 1                   # same thing did for negative counts
    
    return cnt                         # returning negative counts




def create_file():
    lines = project_file.readlines()
    lines.pop(0)
    result_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n") # adding heading
    for line in lines:
        line = line.strip().split(",")                  # each column separated by "," hence splitted where comma presents
        positive_counts = count_positives(line[0])      # tweets are sent to the functions to --
        negative_counts = count_negatives(line[0])      # -- count positive & negative words 
        result_file.write("{},  {}, {}, {}, {}\n".format(line[1],line[2], positive_counts, negative_counts, positive_counts-negative_counts))



create_file()          
project_file.close()
result_file.close()