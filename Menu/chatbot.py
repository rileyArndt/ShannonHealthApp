# Mitchell Martin
# 10/11/2022

""""
Input your responses here then add the specified 
index to the check_messages function.
"""

B_TELEMED = 'Redirecting you to the telemedicene page...'
B_HOME = 'Taking you home'
B_WEBSITE = "I'm redirecting you to the shannon webpage"
B_MYCHARTLINK = "I'm redirecting you to the mychart page"
B_BILL = "I'm redirecting you to the payment page"


possible_answers=['Hello', B_TELEMED, B_WEBSITE, B_MYCHARTLINK, B_BILL, B_HOME]


# Splitting the string
import re

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
   response(possible_answers[0], ['hello', 'hey', 'heyy', 'hola'], single_response=True)
   response(possible_answers[1], ['telemedicene', 'help', 'emergency', 'immediate', 'immediately', 'phone'], single_response=False)
   response(possible_answers[2], ['desktop', 'web', 'webpage', 'website', 'online'])
   response(possible_answers[3], ['mychart', 'chart', 'my chart'])
   response(possible_answers[4], ['bill', 'pay', 'bills', 'order'])
   response(possible_answers[5], ['back', 'home'])

   best_match = max(highest_prob_list, key=highest_prob_list.get)
   return best_match

   return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def matchedresponse(usr_input):
   # Makes sure all letters are lower-case and the punctuation is removed
   # converted to an array
   split_message = re.split(r'\s+|[,;?!.-]\s*', usr_input.lower())
   
   response = check_messages(split_message)
   return response

   