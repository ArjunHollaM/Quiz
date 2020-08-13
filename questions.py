import random
import answers
import lifelines
import time
#Questions
dic={'Chandrayaan-2 Mission was launched by which vehicle?':'A. GSLV MkIII B. PSLV C11 C. GSLV F11 D. PSLV C45',
     'Which among the following country first reached the ‘Dark Side’ of the Moon?':'A. India B. USA C. China D. Russia',
     'Which country has developed the world-first floating nuclear plant?':'A. India B. China C. USA D. Russia',
     'Which is the first country, where WhatsApp is launching its ‘WhatsApp Pay’?':'[A] India [B] Brazil [C] Japan [D] South Korea',
     'Which Indian institution developed an intensive care unit (ICU) grade ventilator under the name of ‘Project Praana’?':'[A] Indian Institute of Science (IISc) [B] AIIMS [C] IIT- Delhi [D] IIT- Guwahati',
     'Which Technology company has announced a new global skills initiative, to train 25 million people worldwide?':'[A] Google [B] Microsoft [C] Amazon [D] Facebook',
     'Which Indian institution has partnered with NVIDIA, to establish India’s first ‘NVIDIA AI Technology Centre’?':'[A] IIT- Madras [B] IISc, Bangalore [C] IIT- Hyderabad [D] IIT- Kharagpur',
     'Which state has recently declared 2020 as the year of Artificial Intelligence (AI) and has signed MoUs with tech firms for AI research?':'[A] Andhra Pradesh [B] Telengana [C] Odisha [D] Assam',
     'The first e-waste clinic of India was recently opened in which city?':'[A] Lucknow [B] Mumbai [C] Bhopal [D] Cuttack',
     'Which global firm has developed a new Artificial Intelligence (AI) model to protect an endangered whale species?':'[A] Amazon [B] Microsoft [C] Google [D] Facebook',
     'Which consists of two plates separated by a dielectric and can store a charge?':'(A) Inductor (B) Capacitor (C) Transistor (D) Relay',
     ' "FET" is a type of transistor; Its full name is ________ Effect Transistor.':'(A) Field (B) Factor (C) Flash (D) Force',
     'What are three types of lasers?':'(A) Gas, metal vapor, rock (B) Pointer, diode, CD (C) Diode, inverted, pointer (D) Gas, solid state, diode',
     'What will a UPS be used for in a building?':'(A) To provide power to essential equipment (B) To monitor building electricity use (C) To carry messages between departments (D) To control lighting and power systems',
     'What does AC and DC stand for in the electrical field?':'(A) Alternating Current and Direct Current (B) A Rock Band from Australia (C) Average Current and Discharged Capacitor (D) Atlantic City and District of Columbia',
     "A given signal's second harmonic is twice the given signal's __________ frequency?":'(A) Fourier (B) Foundation (C) Fundamental (D) Field',
     'What does the term PLC stand for?':'(A) Programmable Lift Computer (B) Program List Control (C) Programmable Logic Controller (D) Piezo Lamp Connector',
     'When measuring the characteristics of a small-signal amplifier, say for a radio receiver, one might be concerned with its "Noise"?':'(A) Fundamental (B) Fall (C) Force (D) Figure',
     'Who created Pretty Good Privacy (PGP)?':'(A) Phil Zimmermann (B) Tim Berners-Lee (C) Marc Andreessen (D) Ken Thompson',
     'After the first photons of light are produced, which process is responsible for amplification of the light?':"(A) Blackbody radiation (B) Stimulated emission (C) Planck's radiation (D) Einstein oscillation",
     ' What is “Hot Line”?':'(A) An Electric wire (B) Line of control in the battle field (C) Imaginary line indicating atmospheric pressure (D) A telecommunication link',
     ' Blue is what number on the resistor color code?':'(A) 1 (B) 4 (C) 2 (D) 6',
     "A coating of dust on a computer's main circuit boards has this probable consequence":'(A) Overheating (B) Short circuits (C) Slower hard disk (D) None',
     'What are the three main search expressions, or operators, recognized by Boolean logic?':'(A) FROM, TO, WHOM (B) AND, OR, NOT (C) SEARCH, KEYWORD, TEXT (D) AND, OR, BUT',
     'What is a GPU?':'(A) Grouped Processing Unit (B) Graphics Processing Unit (C) Graphical Performance Utility (D) Graphical Portable Unit',
     'What is VCM?':'(A) Virtual Connection Manager (B) Virtual Channel Memory (C) Voice Controlled Modem (D) Voice Communications Module',
     ' What was the clock speed of the original IBM PC?':'(A) Less than 5 MHz (B) 10 MHz (C) 8 MHz (D) Just over 16 MHz',
     ' What is NAT?':'(A) Network Address Translation (B) Network Administration Tool (C) Novell Address Transfer (D) Newly Added Technology',
     ' What does ICMP stand for?':'(A) Internet Connection Modem Protocol (B) Intranet Control Message Program (C) Internal Conflict Management Program (D) Internet Control Message Protocol',
     " 'DTP' computer abbreviation usually means?":'(A) Digital Transmission Protocol (B) Desk-Top Publishing (C) Data Type Programming (D) Document Type Processing'}

def ask():
     score=0
     for i in range(1,11,1):
          print("Question "+str(i)+":")
          ch=random.choice(list(dic.keys()))
          print(ch)
          print(dic.get(ch,0))
          s=input("Your Response: ")
          del dic[ch]
          if s.isalpha():
               if answers.ans[ch]==s.lower():
                    print("Correct!!")
                    score+=10
                    print("Current score "+str(score))
               elif "life" == s.lower():
                    condition=False
                    while (condition==False):
                         print("Which lifeline will it be?Enter number corresponding to the lifelines.")
                         print(lifelines.l)
                         k=input()
                         if k=='1':
                              condition=True
                              h=lifelines.half(ch)
                              if h=="Wrong":
                                   print("Sorry..The right option was " + answers.ans[ch])
                                   score -= 5
                                   print("current score " + str(score))
                              else:
                                   print("Correct!!")
                                   score += 5
                                   print("Current score " + str(score))
                              continue
                         elif k=='2':
                              condition=True
                              lifelines.pass_question(ch)
                              score+=3
                              print("Current score "+str(score))
                              continue
                         elif k=='3':
                              condition=True
                              if lifelines.eliminate(ch)=="Wrong":
                                   print("Sorry..The right option was "+answers.ans[ch])
                                   score-=5
                                   print("Current score "+str(score))
                              else:
                                   print("Correct!!")
                                   score+=7
                                   print("Current score "+str(score))
                         else:
                              print("Invalid input")
                              condition=False
               else:
                    print("Sorry.. The right option was " + answers.ans[ch])
                    score-=5
                    print("Current score "+str(score))
          else:
               print("Sorry.. The right option was "+answers.ans[ch])
               score-=5
               print("Current score "+str(score))
          time.sleep(2)
     return score

