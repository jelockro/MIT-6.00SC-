# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1
class NewsStory(object):

    # instance variables
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    # class variables
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link


 




# TODO: NewsStory

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5
### pretend that any character in string.punctuation is a word separator
# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
        
    def is_word_in(self, text):
        import string
        word = self.word.lower()
        text = text.lower()

        # Remove punctuation & split
        punctuation = "!@#$%^&*()-_+={}[]|\:;<>?,./\""
        text = text.replace("'"," ")
        cleanText =''
        for char in text:
            if char not in punctuation:
                cleanText += char
        cleanText = cleanText.split(' ')

        # Check if the word is in the text
        if word in cleanText:
            return True
        else:
            return False

##class WordTrigger(Trigger):
##    def __init__(self, word):
##        self.word = word
##
##    def is_word_in(self, text):
##        word = self.word.lower()
##        text = text.lower()
##
##        # Remove punctation and split the text
##        for punc in string.punctuation:
##            text = text.replace(punc, " ")
##        splittext = text.split(" ")
##
##        # Check if the word is in the text
##        return word in splittext

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def __init__(self,word):
        self.word = word
    
    def evaluate(self, story):
        return self.is_word_in(story.get_title())

# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        self.word = word

    def evaluate(self, story):
        return self.is_word_in(story.get_subject())

# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        self.word = word

    def evaluate(self, story):
        return self.is_word_in(story.get_summary())

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, Trigger):
        self.Trigger = Trigger
    
    def evaluate(self, story):
        return not self.Trigger.evaluate(story)
 
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, Trigger1, Trigger2):
        self.t1 = Trigger1
        self.t2 = Trigger2

    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, Trigger1, Trigger2):
        self.t1 = Trigger1
        self.t2 = Trigger2

    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)

# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    # var are instance variables of NewsStory i.e (subject, title...) 
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        storyAttr = story.guid + story.title + story.subject + story.summary + story.link
        return self.phrase in storyAttr
    
#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel free to change this line!
    filtStories =[]
    for story in stories:
        #print 'triggerlist form filter_stories:', triggerlist
        for trigger in triggerlist:       
            #print trigger
            if trigger.evaluate(story):
                filtStories.append(story)
                #break




    return filtStories

#======================
# Part 4
# User-Specified Triggers
#======================
def makeTrigger(tmap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and returns a new
    trigger instance.

    trigger_map: dictionary with names as keys (strings) and triggers as values
    trigger_type: string indicating the type of trigger to make (ex: "TITLE", "AND")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"], ["t2", "t3"])
    name: a string representing the name of the new trigger (ex: "t1", "t2")

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).

    Modifies trigger_map, adding a new key-value pair for this trigger.
    """
    if triggerType == 'TITLE':
        trigger = TitleTrigger(params[0])   

    elif triggerType == 'SUBJECT':
        trigger = SubjectTrigger(params[0])
    elif triggerType == 'SUMMARY':
        trigger = SummaryTrigger(params[0])
    elif triggerType == 'NOT':
        trigger = NotTrigger(params[0])
    elif triggerType == 'AND':
        trigger = AndTrigger(tmap[params[0]], tmap[params[1]])
    elif triggerType == 'OR':
        trigger = OrTrigger(tmap[params[0]], tmap[params[1]])
    elif triggerType == "PHRASE":
        trigger = PhraseTrigger(" ".join(params))                                     

    else:
        return None
  
    #populate tmap
    tmap[name] = trigger
     
def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    #print all
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)
    
    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones

    #dict1={'TITLE':TitleTrigger(), SUBJECT():SubjectTrigger(), 'SUMMARY':'SummaryTrigger', 'NOT':'NotTrigger', 'PHRASE': 'PhraseTrigger', 'AND': 'AndTrigger', 'OR': 'OrTrigger'}
    tmap = {}
    triggerlist=[]
    for line in lines:
        
        var = line.split(' ')
       
    # Make a new trigger
        if  var[0] !='ADD':
            trigger = makeTrigger(tmap, var[1], var[2:], var[0])

    # Add the triggers to the list
        else:
            for name in var[1:]:
                 triggerlist.append(tmap[name])
                 #print tmap
    #print 'triggers from reattrigger:', triggerlist
    return triggerlist
            

    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
##    t1 = SubjectTrigger("Obama")
##    t2 = SummaryTrigger("MIT")
##    t3 = PhraseTrigger("Supreme Court")
##    t4 = OrTrigger(t2, t3)
##    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")
    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        print 'triggerlist form main_thread:', triggerlist
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

