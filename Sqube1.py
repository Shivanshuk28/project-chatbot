//what is being typed here is none of your businesss
import re                                         
import long_responses as long
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}
    

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses 
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('hmmmm!',['ok','ya','hmm','hm','yup'],required_words=['ok','ya','hmm','hm','yup'])
    response("Well!! Since you have selected python,it wil surely clear your basics.Write ""Python"" in chatbox to know its general information.",["i",'want','know','python'],required_words=['python'])
    
    
    
    
    
    # Longer responses
    #advice
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    #eating
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    #name
    response(long.R_NAME,['Whats','what','your','name'],required_words=['name'])
    #condn
    response(long.R_CONDN,['How','are','you'],required_words=['how','are','you'])
    #age
    response(long.R_AGE,["What's","What","is","your","age"],required_words=["your","age"])
    #do
    response(long.R_do, ['what', 'you', 'do','does'], required_words=['what','you', 'do'])
    #learn
    response(long.R_learn, ['how', 'you', 'learn'], required_words=['you', 'learn'])
    #language
    response(long.R_language, ['which','is','best','language'], required_words=['which','language'])
    #slearn
    response(long.R_slearn,['which','language','should','learn','study'],required_words=['language','learn'])
    #programminglanguage
    response(long.R_proglang,['tell','something','about','programming','languages'], required_words=['programming','languages'])
    #python
    response(long.R_python, ['python','Python','PYTHON'], required_words=['python'])
    #features
    response(long.R_pyfeatures, ['features','Features','python','features'], required_words=['features','python'])
    #variables
    response(long.R_pyvariables, ["python","variables"], required_words=["python","variables"])
    #operators
    response(long.R_pyoperators, ["python","operators"], required_words=["python","operators"])
    #datatypes
    response(long.R_pydatatypes, ["python","datatypes"], required_words=["python","datatypes"])
    #comments
    response(long.R_pycomments, ["python","comments"], required_words=["python","comments"])
    #strings
    response(long.R_pystrings, ["python","strings"], required_words=["python","strings"])
    #booleans
    response(long.R_pybooleans, ["python","booleans"], required_words=["python","booleans"])
    #numbers
    response(long.R_pynumbers, ["python","numbers"], required_words=["python","numbers"])
    #lists
    response(long.R_pylists,["python","lists"], required_words=["python","lists"])
    #tuples
    response(long.R_pytuples, ["python","tuples"], required_words=["python","tuples"])
    #sets
    response(long.R_pysets, ["python","sets"], required_words=["python","sets"])
    #dictionaries
    response(long.R_pydictionaries, ["python","dictionaries"], required_words=["python","dictionaries"])
    #ifelse
    response(long.R_pyifelse, ["python","ifelse"], required_words=["python","ifelse"])
    #whileloops
    response(long.R_pywhileloop, ["python","whileloops"], required_words=["python","whileloops"])
    #forloops
    response(long.R_pyforloop, ["python","forloops"], required_words=["python","forloops"])
    #functions
    response(long.R_pyfunctions, ["python","functions"], required_words=["python","functions"])
    #lamda
    response(long.R_pylamdafunctions, ["python","lamda","function"], required_words=["python","lamda","function"])
    #arrays
    response(long.R_pythonarrays, ["python","arrays"], required_words=["python","arrays"])
    #modules
    response(long.R_pymodules, ["python","modules"], required_words=["python","modules"])
    
    
    
    
    #response(long., [], required_words=[])
    
    
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
    
    









