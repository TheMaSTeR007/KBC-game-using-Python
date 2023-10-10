# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

#qlist is list containing questions.
qlist = ["\n        Your 1st Quesion for Rs. 10,000 /- is\n\n[1] Current Railway Minister of India is _______.\n    A. Mamta Banarjee                B. Ram Vilash \n    C. Ashwini Vaishnaw              D. Piyush Goyal\n",
"\n        Your 2nd Quesion for Rs. 20,000 /- is\n\n[2] What is height of Qutub Minar ?\n    A. 71m                B. 73m\n    C. 82m                D. 76m\n",
"\n        Your 3rd Quesion for Rs. 30,000 /- is\n\n[3] Which god is also known as 'Gauri Nandan' ?\n    A. Agni                B. Indra\n    C. Hanuman             D. Ganesha\n",
"\n        Your 4th Quesion for Rs. 40,000 /- is\n\n[4] Which city is known as Pink City in India ?\n    A. Banglore                B. Maysore\n    C. Jaipur                  D. Kochi\n",
"\n        Your 5th Quesion for Rs. 50,000 /- is\n\n[5] Who wrote Vande Mataram ?\n    A. Sarat Chandra Chattopadhyay                B. Rabindranath Tagore\n    C. Bankim Chandra Chatterjee                  D. Ishwar Chandra Vidyasagar\n",
"\n        Your 6th Quesion for Rs. 60,000 /- is\n\n[6] Where in India Gate located?\n    A. Agra                B. Punja\n    C. Mumbai              D. New Delhi\n",
"\n        Your 7th Quesion for Rs. 70,000 /- is\n\n[7] Which of the following musical instruments is NOT of foreign origin?\n    A. Tabla                B. Flute\n    C. Sitar                D. Violin\n",
"\n        Your 8th Quesion for Rs. 80,000 /- is\n\n[8] Who was the first Indian woman to win a medal in the Olympics?\n    A. P.T.Usha                B. Kunjarani Dev\n    C. Bachendri Pal           D. Karnam Maleshwariv\n",
"\n        Your 9th Quesion for Rs. 90,000 /- is\n\n[9] Which of the following is not a state of India?\n    A. Vrindachal                B. Goa\n    C. Jharkhan                  D. Chattisgarh\n",
"\n        Your 10th Quesion for Rs. 1,00,000 /- is\n\n[10] Which Indian city hosts Indian movie industry?\n    A. Goa                B. Mumbai\n    C. Chennai            D. Calcutta\n"]

#alist is list containing answers to qlist respectively.
alist = [('C','c'),('B','b'),('D','d'),('C','c'),('C','c'),('D','d'),('D','d'),('D','d'),('A','a'),('B','b')]

#rs is the list of rupees.
rs =["10,000.","20,000.","30,000.","40,000.","50,000.","60,000.","70,000.","80,000.","90,000.","1,00,000."]

#ra is the list of message to be shown when player is asked question and told how much prize he/she will win if he/she gives the Right answer.
ra=("\nIf you give the Right answer you will get Rs.")

#cyw is the list of Congratulations message shown to player when the Right answer is given.
cyw=("\n               Congratulations! You have won Rs.")

#rw is the message to be shown when player wins 40,000 and will surely get minimun 40k even if he gives a wrong answer afterwards.
rw=("Now, you will get guarenteed Rs.")

#message to be shown when invalid input is given.
ii=("Invalid Input, Please Restart the Game.")

#ent is the function which can be called with a message to take ENTER as input to proceed further in the game.
def ent():
    input("\nPress ENTER to continue...")

#ea is the message to be shown to ask player answer as input.
eya=("\nEnter Option of Your Answer : ")
# input(eya)

# u is user answer input.

#ol is the list of case-sensitive options.
ol = ['A','a','B','b','C','c','D','d']

#wa is the text to be printed when player gives a Wrong Answer.
wa=("\nSorry, That's a Wrong Answer.\nThe Right Answer is ")

#ao is list of optins with answer to print to player to show him/her the Right Answer.
ao =["[C] Ashwini Vaishnav","[B] 70m","[D] Ganesha","[C]Jaipur","[C]Bankim Chandra Chatterjee","[D]New Delhi","[D]Violin","[D]Karnam Maleshwariv","[A]Vrindachal","[B]Mumbai"]

print("                         Welcome to Kaun Banega Crorepati !!!\n")
name = input("What is your good name ?\n")
print("\n" + name + ", You are most Welcome to Kaun Banega Crorepati.\n\n               Let's start the game...\n")
ent()


for i in range(0,len(qlist)):
    print(qlist[i] + ra +rs[i])
    u = str(input(eya))
    if u in ('q','Q'):
     print("You have choose to quit this game now, so you will win " + rs[i-1])
     break
    if u in alist[i]:
     print(cyw ,rs[i])
     ent()
    elif u in ol:
     print(wa , ao[i])
    else:
     break


#THE BELOW CODE WAS WRITTEN USING IF ELSE ONLY ! BUT THE ABOVE CODE IS WRITTEN USING FOR LOOP INTEGRATING WITH IF ELSE...

# print(qlist[0] + ra +rs[0])
# u = str(input(eya))
# if u in alist[0]:
#      print(cyw ,rs[0])
#      ent()
    
#      print(qlist[1] + ra +rs[1])
#      u = str(input(eya))
#      if u in alist[1]:
#           print(cyw ,rs[1])
#           ent()
          
     
#           print(qlist[2] + ra +rs[2])
#           u = str(input(eya))
#           if u in alist[2]:
#                print(cyw ,rs[2])
#                ent()
     
#                print(qlist[3] + ra +rs[3])
#                u = str(input(eya))
#                if u in alist[3]:
#                     print(cyw ,rs[3])
#                     ent()
    
#                     print(qlist[4] + ra +rs[4])
#                     u = str(input(eya))
#                     if u in alist[4]:
#                          print(cyw ,rs[4])
#                          ent()
    
#                          print(qlist[5] + ra +rs[5])
#                          u = str(input(eya))
#                          if u in alist[5]:
#                               print(cyw ,rs[5])
#                               ent()
    
#                               print(qlist[6] + ra +rs[6])
#                               u = str(input(eya))
#                               if u in alist[5]:
#                                   print(cyw ,rs[6])
#                                   ent()
    
#                                   print(qlist[7] + ra +rs[7])
#                                   u = str(input(eya))
#                                   if u in alist[7]:
#                                        print(cyw ,rs[7])
#                                        ent()
    
#                                        print(qlist[8] + ra +rs[8])
#                                        u = str(input(eya))
#                                        if u in alist[8]:
#                                             print(cyw ,rs[8])
#                                             ent()
    
#                                             print(qlist[9] + ra +rs[9])
#                                             u = str(input(eya))
#                                             if u in alist[9]:
#                                                  print(cyw ,rs[9])#1

#                                             elif u in ol:
#                                                 print(wa , ao[0])#9
#                                             else:
#                                                 print(ii)
#                                        elif u in ol:
#                                            print(wa , ao[8])#8
#                                        else:
#                                            print(ii)
#                                   elif u in ol:
#                                       print(wa , ao[7])#7
#                                   else:
#                                       print(ii)
#                               elif u in ol:
#                                   print(wa , ao[6])#6
#                               else:
#                                   print(ii)
#                          elif u in ol:
#                             print(wa , ao[5])#5
#                          else:
#                             print(ii)
#                     elif u in ol:
#                         print(wa , ao[4])#4
#                     else:
#                         print(ii)
#                elif u in ol:
#                    print(wa , ao[3])#4
#                else:
#                    print(ii)
#           elif u in ol:
#               print(wa , ao[2])#3
#           else:
#              print(ii)
#      elif u in ol:
#          print(wa , ao[1])#2
#      else:
#          print(ii)
        
# elif u in ol:
#     print(wa , ao[0])#1
# else:
    print(ii)