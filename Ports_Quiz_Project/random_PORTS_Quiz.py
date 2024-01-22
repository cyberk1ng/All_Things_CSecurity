import pyinputplus as pyip, random, time 

#this program tests your knowledge on ports and their services




#The 29 quiz data. keys are port numbers and values are usage.
ports_proto = {'20':'ftp-data','21':'ftp','22':'ssh','23':'telnet',
         '25':'smtp','49':'tacacs','53':'dns','69':'tftp',
         '80':'http','88':'kerberos','110':'pop3','119':'nntp',
         '123':'ntp','137':'netbios','143':'imap','161':'snmp',
         '162':'snmptrap','389':'ldap','443':'https','444':'snpp',
        '445':'smb','500':'isakmp','514':'syslog','636':'ldaps',
        '1433':'ms-sql-s', '1701':'l2tp', '1723':'PPTP', '1812':'radius',
        '3389':'rdp'}



port_list = list(ports_proto.keys()) #the ports rom the dictare transform into a list
services_list = list(ports_proto.values())# and the services running those ports too.

numberOfQuestions = 29 #this number matches the amount of question that would be asked.
correctAnswer = 0 #the corerct answer variable.
count = 0 #this variable tracks the number of failed tries

def ask_port_service(): #this function takes the user input and returns it value.
    return pyip.inputMenu(unique_port_choice, prompt, lettered=True, numbered=False, limit=3)  


#this is the loop for the questions
for questionNumber in range(1, numberOfQuestions):
    question_port = random.choice(port_list) # a random port is selected
    port_service_options = random.sample(services_list, k=3) # 3 random wrong ports are picked
    prompt = 'Q# %s: What service uses the port %s?' % (questionNumber, question_port) +'\n ' 

    correctService = ports_proto[question_port] #the correct answer is stored in this variable,
    port_service_options.append(correctService) #then it gets appended to the list of wrong ports,
    unique_port_choice = list(set(port_service_options)) # the list get preprocessed from duplicates and then back to a list,
    random.shuffle(unique_port_choice) #then the list gets shuffles so that the correct answer dont have to always be 'D'.
    


    # A try block to get the users input and check if it is right, else do something else.
    try:
        result = ask_port_service()
        if result == ports_proto[question_port]:
            print("Correct")
            correctAnswer += 1
            continue
        else:
            print('Wrong!')
            count += 1
            result = ask_port_service()
            if result == ports_proto[question_port]:
                print("Correct")
                correctAnswer += 1
                continue
            else:
                print('Wrong!')
                count += 1
                result = ask_port_service()
                if result == ports_proto[question_port]:
                    print("Correct")
                    correctAnswer += 1
                    continue
                else:
                    print('Wrong!')
                    count += 1
                    result = ask_port_service()
                if count == 3:
                    break
    #except pyip.TimeoutException:
    #    print("Out of tries!")
    except pyip.RetryLimitException:
        print("Out of tries!")
    except KeyboardInterrupt:
        print("Keyboard interruption!")
    else:
        correctAnswer += 1 #After the code inside the try block has run, this else block  which updates the correctAnswer variable is executed.
    
    time.sleep(1) #the program waits for a second before asking the next question.

print('\n Score: %s / %s' % (correctAnswer, numberOfQuestions)) #Finally the score is printed.