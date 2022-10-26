# Mitchell Martin
# 10/11/2022

from Chatbot import dataextraction
# Splitting the string
import re

""""
Input your responses here then add the specified 
index to the check_messages function.
"""

B_TELEMED = "Shannon On Demand makes it easy for you to talk to a healthcare provider for minor medical needs, immediately, without an appointment."
B_TELEMED += "\nI'm redirecting you to the page..."
B_HOME = 'Let\'s go to the home screen'
B_WEBSITE = "I'm redirecting you to the shannon webpage"
B_MYCHARTLINK = 'MyChart makes it easy to access your health records and schedule appointments.'
B_MYCHARTLINK += "\nI'm redirecting you to the page..."
B_BILL = "I'm redirecting you to the payment page"
B_WHOAMI = dataextraction.get_name()
B_WAITTIMES = dataextraction.get_wait_times()
B_WLOCATION = dataextraction.get_women_location()
B_THANKS = "You're welcome!"
B_PHARMACY = "I'm redirecting you to the pharmacy page..."
B_PPAGE = "I'm redirecting you to the available perscriptions"
B_NEWS = "Here is the latest news.\n" + dataextraction.return_news()
B_PRICEEST = "I'm redirecting you to the price estimate page..."
B_SLEEP = "I'm redirecting you to the sleep center..."
B_DATE = dataextraction.get_date()
B_CAREER = "The employment page allows you to check for career openings.\nI will redirect you to the page..."
B_READY = "Let's check by going to the available perscription screen."
B_STORIES = dataextraction.get_stories()
B_NUMBER = dataextraction.get_shannon_info()
B_MR = "You can access your medical records by filling a Record Authorization form\nI will redirect you to the page..."


possible_answers=['Hello', B_TELEMED, B_WEBSITE, B_MYCHARTLINK,
                  B_BILL, B_HOME, B_WHOAMI, B_WAITTIMES,
                  B_WLOCATION, B_THANKS, B_PHARMACY, B_PPAGE, B_NEWS, 
                  B_PRICEEST, B_SLEEP, B_DATE, B_CAREER, B_READY, B_STORIES, B_NUMBER,
                  B_MR]





# message_probability: checks the keywords for the most accurate response
# @ user_message - The user input
# @ 
def message_probability(user_message, recognised_words, single_response=False, req_words=[]):
   message_certainty = 0
   has_req_words = True
   
   # Calculates how many words are present in the each predifined message
   for word in user_message:
      if word in recognised_words:
         message_certainty += 1
   
   # Calculates the percent of recognized
   # words in "user_message"      
   perc = float(message_certainty) / float(len(recognised_words))
   
   # Assures the required words are within
   # the string
   for word in req_words:
      if word not in user_message:
         has_req_words = False
         break
   
   # Makes the percentage a whole number
   if has_req_words or single_response:
      return int(perc*100)
   else:
      return 0


# Used if an unknown message is sent.
def unknown_message():
   return 'I don\'t understand'

def check_messages(message):
   highest_prob_list = {}
   
   def response(bot_response, list_of_words, single_response=False, req_words=[]):
      nonlocal highest_prob_list
      highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, req_words)
   # Insert robot responses here
   # @ First Arg. - Robot Response
   # @ Second Arg. - List of matched words
   # @ Third Arg. - List of required words
   response('I don\'t understand', ['bla bla bla'], single_response=True)
   response('I\'m doing well! How may I help you?', ['how', 'are', 'you', 'doing', 'what\'s up', 'wassup'])
   response(possible_answers[0], ['hello', 'hey', 'heyy', 'hola'], single_response=True)
   response(possible_answers[1], ['telemedicene', 'help', 'emergency', 'immediate', 'immediately', 'doctor', 'phone', 'appointment'], single_response=False)
   response(possible_answers[2], ['desktop', 'web', 'webpage', 'website', 'online'])
   response(possible_answers[3], ['mychart', 'chart', 'my chart', 'checked'])
   response(possible_answers[4], ['bill', 'pay', 'bills', 'order', 'money'])
   response(possible_answers[5], ['back', 'home'])
   response(possible_answers[6], ['name', 'hospital'])
   response(possible_answers[7], ['time', 'wait', 'available', 'time', 'times'])
   response(possible_answers[8], ['women', 'children', 'hospital', 'child', 'kid', 'baby', 'girl'])
   response(possible_answers[9], ['thank', 'thanks', 'appreciate'])
   response(possible_answers[10], ['pharmacy', 'online'])
   response(possible_answers[11], ['perscription', 'perscriptions', 'medicene'])
   response(possible_answers[12], ['news', 'breaking'], req_words=['news'])
   response(possible_answers[13], ['estimates', 'price', 'charges', 'estimate', 'cost'], req_words=['estimate'])
   response(possible_answers[14], ['sleep', 'center', 'sleeping'], req_words=['sleep'])
   response(possible_answers[15], ['date', 'today', 'day'])
   response(possible_answers[16], ['job', 'career', 'careers', 'employment', 'employees', 'employee'])
   response(possible_answers[17], ['ready', 'perscription', 'available', 'here', 'medicene', 'meds'])
   response(possible_answers[18], ['class', 'classes', 'group', 'groups', 'survivor', 'sisters'])
   response(possible_answers[19], ['call', 'phone', 'open', 'opening', 'number', 'contact', 'information', 'info', 'hours', 'operation'])
   response(possible_answers[20], ['record', 'records', 'medical', 'image', 'images', 'radiology', 'form', 'authorization'])

   best_match = max(highest_prob_list, key=highest_prob_list.get)
   return best_match

   return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def matchedresponse(usr_input):
   # Makes sure all letters are lower-case and the punctuation is removed
   # converted to an array
   split_message = re.split(r'\s+|[,;?!.-]\s*', usr_input.lower())
   
   response = check_messages(split_message)
   return response

   


