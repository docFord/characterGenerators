#!/usr/bin/python
# Top Secret Character Generator v1.0

import random
from termcolor import colored


# Dictionaries & Lists

maleFirst = ['Noah',
			 'William',
			 'James',
			 'Benjamin',
			 'Mason',
			 'Elijah',
			 'Oliver',
			 'Jacob',
			 'Lucas',
			 'Michael',
			 'Alexander',
			 'Ethan',
			 'Daniel',
			 'Matthew',
			 'Henry',
			 'Joseph',
			 'Jackson',
			 'Samuel',
			 'David',
			 'Wyatt',
			 'John',
			 'Owen',
			 'Dylan',
			 'Luke',
			 'Gabriel',
			 'Anthony',
			 'Isaac',
			 'Grayson',
			 'Jack',
			 'Julian',
			 'Christopher',
			 'Joshua',
			 'Andrew',
			 'Ryan',
			 'Nathan',
			 'Aaron',
			 'Thomas',
			 'Charles',
			 'Caleb',
			 'Christian',
			 'Hunter',
			 'Eli',
			 'Jonathan',
			 'Connor',
			 'Adrian',
			 'Cameron',
			 'Theodore',
			 'Robert',
			 'Nolan',
			 'Nicholas',
			 'Brayden',
			 'Jordan',
			 'Austin',
			 'Ian',
			 'Adam',
			 'Elias',
			 'Carson',
			 'Evan',
			 'Cooper',
			 'Jason',
			 'Chase',
			 'Gavin',
			 'Kevin',
			 'Zachary',
			 'Tyler',
			 'Micah',
			 'Vincent',
			 'Miles',
			 'Wesley',
			 'Nathaniel',
			 'Brandon',
			 'Cole',
			 'Declan',
			 'Bennett',
			 'George',
			 'Justin',
			 'Max',
			 'Luca',
			 'Ivan',
			 'Giovanni',
			 'Eric',
			 'Blake',
			 'Alex',
			 'Alan',
			 'Elliott',
			 'Timothy',
			 'Victor',
			 'Bryce',
			 'Finn',
			 'Edward',
			 'Patrick',
			 'Grant',
			 'Richard',
			 'Joel',
			 'Gael',
			 'Tucker',
			 'Rhett',
			 'Steven',
			 'Graham',
			 'Jesse',
			 'Dean',
			 'Preston',
			 'August',
			 'Oscar',
			 'Jeremy',
			 'Alejandro',
			 'Marcus',
			 'Mark',
			 'Bryan',
			 'Kyle',
			 'Peter',
			 'Charlie',
			 'Paul',
			 'Colin',
			 'Bradley',
			 'Derek',
			 'Arthur',
			 'Leon',
			 'Felix',
			 'Jake',
			 'Sterling',
			 'Randy',
			 'Gordon',
			 'Sean',
			 'Riley',
			 'Archer',
			 'Corbin',
			 'Simon',
			 'Barry',
			 'Walter',
			 'Damien',
			 'Colt',
			 'Stephen',
			 'Louis',
			 'Cody',
			 'Spencer',
			 'Raymond',
			 'Cristian',
			 'Travis',
			 'Dante',
			 'Garrett',
			 'Donovan',
			 'Seth',
			 'Jeffrey',
			 'Edwin',
			 'Angelo',
			 'Conner',
			 'Marco',
			 'Jensen',
			 'Dakota',
			 'Johnny',
			 'Troy',
			 'Kash',
			 'Shane',
			 'Trevor',
			 'Odin',
			 'Quinn',
			 'Clark',
			 'Harvey',
			 'Jay',
			 'Jared',
			 'Shawn',
			 'Stuart', 
]

femFirst = ['Marisha',
			'Emma',
			'Olivia',
			'Ava',
			'Isabella',
			'Sophia',
			'Mia',
			'Charlotte',
			'Amelia',
			'Evelyn',
			'Abigail',
			'Harper',
			'Emily',
			'Elizabeth',
			'Avery',
			'Sofia',
			'Ella',
			'Madison',
			'Scarlett',
			'Victoria',
			'Aria',
			'Grace',
			'Chloe',
			'Camila',
			'Penelope',
			'Riley',
			'Layla',
			'Lillian',
			'Nora',
			'Zoey',
			'Mila',
			'Aubrey',
			'Hannah',
			'Lily',
			'Addison',
			'Eleanor',
			'Natalie',
			'Luna',
			'Savannah',
			'Brooklyn',
			'Leah',
			'Zoe',
			'Stella',
			'Hazel',
			'Ellie',
			'Paisley',
			'Audrey',
			'Skylar',
			'Violet',
			'Claire',
			'Bella',
			'Aurora',
			'Lucy',
			'Anna',
			'Samantha',
			'Caroline',
			'Aaliyah',
			'Kinsley',
			'Allison',
			'Maya',
			'Sarah',
			'Madelyn',
			'Adeline',
			'Alexa',
			'Ariana',
			'Elena',
			'Gabriella',
			'Naomi',
			'Alice',
			'Sadie',
			'Hailey',
			'Eva',
			'Emilia',
			'Autumn',
			'Quinn',
			'Piper',
			'Ruby',
			'Serenity',
			'Willow',
			'Everly',
			'Cora',
			'Kaylee',
			'Lydia',
			'Aubree',
			'Arianna',
			'Eliana',
			'Melanie',
			'Gianna',
			'Isabelle',
			'Julia',
			'Valentina',
			'Nova',
			'Clara',
			'Vivian',
			'Reagan',
			'Mackenzie',
			'Madeline',
			'Isla',
			'Katherine',
			'Sophie',
			'Josephine',
			'Ivy',
			'Liliana',
			'Jade',
			'Maria',
			'Taylor',
			'Hadley',
			'Kylie',
			'Emery',
			'Adalynn',
			'Natalia',
			'Annabelle',
			'Faith',
			'Alexandra',
			'Ashley',
			'Brianna',
			'Raelynn',
			'Bailey',
			'Mary',
			'Athena',
			'Andrea',
			'Leilani',
			'Jasmine',
			'Lyla',
			'Margaret',
			'Alyssa',
			'Adalyn',
			'Khloe',
			'Kayla',
			'Eden',
			'Eliza',
			'Rose',
			'Ariel',
			'Melody',
			'Alexis',
			'Isabel',
			'Sydney',
			'Juliana',
			'Lauren',
			'Iris',
			'Morgan',
			'Lilly',
			'Charlie',
			'Aliyah',
			'Valeria',
			'Arabella',
			'Sara',
			'Finley',
			'Trinity',
			'Jordyn',
			'Jocelyn',
			'Kimberly',
			'Molly',
			'Valerie',
			'Cecilia',
			'Anastasia',
			'Daisy',
			'Reese',
			'Laila',
			'Amy',
			'Elise',
			'Harmony',
			'Paige',
			'Laura',
			'Lana',
]

surnames = ['Winchester',
			'Reddington',
			'Reigal',
			'Woll',
			'Jaffe',
			'Bailey',
			'Wright',
			'Riggs',
			'Calkin',
			'Mercer',
			'Rose',
			'Smith',
			'Johnson',
			'Williams',
			'Jones',
			'Brown',
			'Davis',
			'Miller',
			'Wilson',
			'Moore',
			'Taylor',
			'Anderson',
			'Thomas',
			'Jackson',
			'White',
			'Harris',
			'Martin',
			'Thompson',
			'Garcia',
			'Martinez',
			'Robinson',
			'Clark',
			'Rodriguez',
			'Lewis',
			'Lee',
			'Walker',
			'Hall',
			'Allen',
			'Young',
			'Hernandez',
			'King',
			'Wright',
			'Lopez',
			'Hill',
			'Scott',
			'Green',
			'Adams',
			'Baker',
			'Gonzalez',
			'Nelson',
			'Carter',
			'Mitchell',
			'Perez',
			'Roberts',
			'Turner',
			'Phillips',
			'Campbell',
			'Parker',
			'Evans',
			'Edwards',
			'Collins',
			'Stewart',
			'Sanchez',
			'Morris',
			'Rogers',
			'Reed',
			'Cook',
			'Morgan',
			'Bell',
			'Murphy',
			'Bailey',
			'Rivera',
			'Cooper',
			'Richardson',
			'Cox',
			'Howard',
			'Ward',
			'Torres',
			'Peterson',
			'Gray',
			'Ramirez',
			'James',
			'Watson',
			'Brooks',
			'Kelly',
			'Sanders',
			'Price',
			'Bennett',
			'Wood',
			'Barnes',
			'Ross',
			'Henderson',
			'Coleman',
			'Jenkins',
			'Perry',
			'Powell',
			'Long',
			'Patterson',
			'Hughes',
			'Flores',
			'Washington',
			'Butler',
			'Simmons',
			'Foster',
			'Gonzales',
			'Bryant ',
			'Alexander',
			'Russell',
			'Griffin ',
			'Diaz',
			'Hayes',
			'Kennedy',
			'Connery',
			'Ford',
			'Reynolds',
			'Pratt',
			'Russo',
			'Reilly',
			'Rothfuss',
			'Weinstein',
			'Weissman',
			'Palmer',
			'Kirkland',
			'Scott',
			'Myers',
			'Greene',
			'Parish',
			'Kelley',
			'Pierce',
			'Thomas',
			'McClane',
			'Davis',
			'O\'Neil',
			'Figgis',
			'Kane',
			'O\'Hara',
			'Simpson',
			'Keene',
			'Camillo'
]

gender = ['male','female']

background = ['Actor',
			  'Architect',
			  'Art & Antiquities Dealer',
			  'Athlete',
			  'Computer Specialist',
			  'Criminal',
			  'Detective',
			  'Doctor',
			  'Driver / Mechanic',
			  'Engineer',
			  'Historian / Archaeologist',
			  'Hunter / Ranger',
			  'Lawyer',
			  'Magician',
			  'Military',
			  'Pilot',
			  'Police',
			  'Sailor / Ship Captain',
			  'Scientist',
			  'Clergy',
			  'The Child of A Famous Person',
			  'Journalist',
			  'Travel Blogger',
]

impairment = ['yes', 'no']

impairments = {1: 'Albinism \n\t\tYour skin and hair are abnormally white and your eyes have a pink or blue iris and a deep-red pupil. \n\t\tYour eyes are extremely sensitive to light, and your skin burns easily.',
			   2: 'Albinism \n\t\tYour skin and hair are abnormally white and your eyes have a pink or blue iris and a deep-red pupil. \n\t\tYour eyes are extremely sensitive to light, and your skin burns easily.',
			   3: 'Anosmia \n\t\tYou can not smell anything, and have a hard time tasting food or drink.',
			   4: 'Anosmia \n\t\tYou can not smell anything, and have a hard time tasting food or drink.',
			   5: 'Clumsy / Accident Prone \n\t\tAlthough your reflex score is not affected, you must roll twice and take \n\t\tthe lower reflex die every time.',
			   6: 'Clumsy / Accident Prone \n\t\tAlthough your reflex score is not affected, you must roll twice and take \n\t\tthe lower reflex die every time.',
			   7: 'Bromhidrosis \n\t\tYou have uncontrollable body odor and excessive sweating. You must shower several times a day \n\t\tand use perscription deodorants to maintain even a low level of body odor.',
			   8: 'Bromhidrosis \n\t\tYou have uncontrollable body odor and excessive sweating. You must shower several times a day \n\t\tand use perscription deodorants to maintain even a low level of body odor.',
			   9: 'Cataplexy \n\t\tStrong emotions such as laughter, anger, surprise, and embarrassment cause you to lose muscle control, \n\t\thave slurred speech and blurred vision, similar to being falldown drunk for about two minutes.',
			   10: 'Cataplexy \n\t\tStrong emotions such as laughter, anger, surprise, and embarrassment cause you to lose muscle control, \n\t\thave slurred speech and blurred vision, similar to being falldown drunk for about two minutes.',
			   11: 'Color Blind - Dichromacy \n\t\tYou are unable to see any shade of red or green or mixture thereof.',
			   12: 'Color Blind - Dichromacy \n\t\tYou are unable to see any shade of red or green or mixture thereof.',
			   13: 'Color Blind - Monochromacy \n\t\tYou cannot see color at all.',
			   14: 'Color Blind - Monochromacy \n\t\tYou cannot see color at all.',
			   15: 'Compulsive Liar \n\t\tYou have a pathologic need to lie, and do so often, from the smallest to the biggest things. \n\t\tYour lies are plausible and convincing, so long as they\'re not investigated too closely.',
			   16: 'Compulsive Liar \n\t\tYou have a pathologic need to lie, and do so often, from the smallest to the biggest things. \n\t\tYour lies are plausible and convincing, so long as they\'re not investigated too closely.',
			   17: 'Congestive Heart Failure \n\t\tYou have a condition marked by weakness, edema, and shortness of breath. You must rest after climbing \n\t\ta flight of stairs. You become weak over 5,000 feet above sea level. Forget about distance running!',
			   18: 'Congestive Heart Failure \n\t\tYou have a condition marked by weakness, edema, and shortness of breath. You must rest after climbing \n\t\ta flight of stairs. You become weak over 5,000 feet above sea level. Forget about distance running!',
			   19: 'Delusion \n\t\tYou have a false belief that you keep, in spite of its being proved false (choose one) e.g.- Flat Earth',
			   20: 'Delusion \n\t\tYou have a false belief that you keep, in spite of its being proved false (choose one) e.g.- Flat Earth',
			   21: 'Diplegia \n\t\tParalysis of both arms or both legs. If legs chosen, you are wheelchair bound. Wheelchair \n\t\tmay be motorized and modified with special devices (missiles!?)',
			   22: 'Diplegia \n\t\tParalysis of both arms or both legs. If legs chosen, you are wheelchair bound. Wheelchair \n\t\tmay be motorized and modified with special devices (missiles!?)',
			   23: 'Dyscalculia \n\t\tYou have difficulty understanding numbers, counting, reading a clock, or doing basic math',
			   24: 'Dyscalculia \n\t\tYou have difficulty understanding numbers, counting, reading a clock, or doing basic math',
			   25: 'Dyslexia \n\t\tYou have a learning disorder marked by impairment of the ability to recognize \n\t\tand comprehend written words.',
			   26: 'Dyslexia \n\t\tYou have a learning disorder marked by impairment of the ability to recognize \n\t\tand comprehend written words.',
			   27: 'Dysphonia \n\t\tYou have a weak, hoarse voice, causing you to sound raspy and strained. You cannot raise your \n\t\tvoice to be heard in loud environments or at a distance.',
			   28: 'Dysphonia \n\t\tYou have a weak, hoarse voice, causing you to sound raspy and strained. You cannot raise your \n\t\tvoice to be heard in loud environments or at a distance.',
			   29: 'Face Blindness (Prosopagnosia) \n\t\tYou cannot distinguish faces, and must rely on other cues to identify people. You often make \n\t\tsocial faux pas if you\'re not concentrating very carefully.',
			   30: 'Face Blindness (Prosopagnosia) \n\t\tYou cannot distinguish faces, and must rely on other cues to identify people. You often make \n\t\tsocial faux pas if you\'re not concentrating very carefully.',
			   31: 'Hoarding \n\t\tYou gather or accumulate a hidden supply of seemingly worthless junk stored for future use.',
			   32: 'Hoarding \n\t\tYou gather or accumulate a hidden supply of seemingly worthless junk stored for future use.',
			   33: 'Hubris \n\t\tYou have overbearing pride or presumption; arrogance. All reaction rolls \n\t\tare made at 1 down for your suave die.',
			   34: 'Hubris \n\t\tYou have overbearing pride or presumption; arrogance. All reaction rolls \n\t\tare made at 1 down for your suave die.',
			   35: 'Hyperacusis \n\t\tYou have a hypersensitivity to sound. What would be considered normal to most people is loud \n\t\tand slightly uncomfortable to you. What would be merely a bit loud to others causes you extreme \n\t\tdiscomfort and even pain. Very loud sounds leave you unable to function from the pain.',
			   36: 'Hyperacusis \n\t\tYou have a hypersensitivity to sound. What would be considered normal to most people is loud \n\t\tand slightly uncomfortable to you. What would be merely a bit loud to others causes you extreme \n\t\tdiscomfort and even pain. Very loud sounds leave you unable to function from the pain.',
			   37: 'Hyperalgesia \n\t\tYou have hypersensitivity to somatosensory stimuli, such as heat, cold, touch, and pain in \n\t\tyour fingers and toes. Somtimes a light finger tap feels like someone punched you.',
			   38: 'Hyperalgesia \n\t\tYou have hypersensitivity to somatosensory stimuli, such as heat, cold, touch, and pain in \n\t\tyour fingers and toes. Somtimes a light finger tap feels like someone punched you.',
			   39: 'Kleptomania \n\t\tYou steal compulsively, not out of any need or desire for the objects, but obsessively \n\t\tand without reason. You are often filled with guilt and remorse afterward.',
			   40: 'Kleptomania \n\t\tYou steal compulsively, not out of any need or desire for the objects, but obsessively \n\t\tand without reason. You are often filled with guilt and remorse afterward.',
			   41: 'Megalomania \n\t\tYou have a psychopathological condition in which delusional fantasies of \n\t\twealth, power, and omnipotence predominate.',
			   42: 'Megalomania \n\t\tYou have a psychopathological condition in which delusional fantasies of \n\t\twealth, power, and omnipotence predominate.',
			   43: 'Migraines \n\t\tYou have severe recurring headaches, usually affecting only one side of the head, characterized by \n\t\tsharp pain and often accompanied by nausea and visual disturbances.',
			   44: 'Migraines \n\t\tYou have severe recurring headaches, usually affecting only one side of the head, characterized by \n\t\tsharp pain and often accompanied by nausea and visual disturbances.',
			   45: 'Misophonia \n\t\tYou have an involuntary physical aversion to a particular type of sound, usually sounds of eating. \n\t\tYou are unable to be around people who are eating without twitching, visibly shuddering, or even \n\t\tstriking out physically.',
			   46: 'Misophonia \n\t\tYou have an involuntary physical aversion to a particular type of sound, usually sounds of eating. \n\t\tYou are unable to be around people who are eating without twitching, visibly shuddering, or even \n\t\tstriking out physically.',
			   47: 'Missing Arm, from the Elbow Down \n\t\tChoose left or right. Reflex score is not affected, but you must adjust for activities that \n\t\tcannot be performed or would be impaired with a prosthetic.',
			   48: 'Missing Arm, from the Elbow Down \n\t\tChoose left or right. Reflex score is not affected, but you must adjust for activities that \n\t\tcannot be performed or would be impaired with a prosthetic.',
			   49: 'Missing Foot (choose one) \n\t\tReflex score is not affected, but you must adjust for activities that cannot \n\t\tbe performed or would be impaired.',
			   50: 'Missing Foot (choose one) \n\t\tReflex score is not affected, but you must adjust for activities that cannot \n\t\tbe performed or would be impaired.',
			   51: 'Missing Hand (choose one) \n\t\tReflex score is not affected, but you must adjust for activities that cannot \n\t\tbe performed or would be impaired.',
			   52: 'Missing Hand (choose one) \n\t\tReflex score is not affected, but you must adjust for activities that cannot \n\t\tbe performed or would be impaired.',
			   53: 'Missing Leg, from the knee down \n\t\t Choose left or right.',
			   54: 'Missing Leg, from the knee down \n\t\t Choose left or right.',
			   55: 'Motion Sickness \n\t\tYou have nausea and dizziness induced by motion when traveling in any vehicle \n\t\tincluding cars, watercraft, and aircraft.',
			   56: 'Motion Sickness \n\t\tYou have nausea and dizziness induced by motion when traveling in any vehicle \n\t\tincluding cars, watercraft, and aircraft.',
			   57: 'Narcissistic Personality Disorder \n\t\tYou have a pathological need for admiration and fame, have grandiose fantasies, lack empathy, \n\t\tand have unreasonable expectations of special treatment.',
			   58: 'Narcissistic Personality Disorder \n\t\tYou have a pathological need for admiration and fame, have grandiose fantasies, lack empathy, \n\t\tand have unreasonable expectations of special treatment.',
			   59: 'Narcolepsy \n\t\tYou have sudden and uncontrollable, though often brief attacks of deep sleep, \n\t\tsometimes accompanied by paralysis and hallucinations.',
			   60: 'Narcolepsy \n\t\tYou have sudden and uncontrollable, though often brief attacks of deep sleep, \n\t\tsometimes accompanied by paralysis and hallucinations.',
			   61: 'Non-Swimmer \n\t\tYou cannot swim, have a fear of water, and are afraid to learn',
			   62: 'Non-Swimmer \n\t\tYou cannot swim, have a fear of water, and are afraid to learn',
			   63: 'Obsessive-Compulsive \n\t\tYou have a tendency to dwell on unwanted thoughts or ideas or perform certain repetitious rituals, \n\t\tespecially as a defense against anxiety from unconscious conflicts.',
			   64: 'Obsessive-Compulsive \n\t\tYou have a tendency to dwell on unwanted thoughts or ideas or perform certain repetitious rituals, \n\t\tespecially as a defense against anxiety from unconscious conflicts.',
			   65: 'Orthorexia \n\t\tYou are obsessed with a "pure" diet, in which you avoid unhealthy foods \n\t\tto the point where it interferes with your life.',
			   66: 'Orthorexia \n\t\tYou are obsessed with a "pure" diet, in which you avoid unhealthy foods \n\t\tto the point where it interferes with your life.',
			   67: 'Overconfidence / Hero Syndrome \n\t\tYou believe yourself capable of almost anything, and leap into action without thinking, \n\t\toften landing you in trouble or danger.',
			   68: 'Overconfidence / Hero Syndrome \n\t\tYou believe yourself capable of almost anything, and leap into action without thinking, \n\t\toften landing you in trouble or danger.',
			   69: 'Panic Disorder \n\t\tYou are excessively fearful, panicking in any stressful situation, and likely to flee danger \n\t\tor perceived danger, even when fleeing could actually be worse.',
			   70: 'Panic Disorder \n\t\tYou are excessively fearful, panicking in any stressful situation, and likely to flee danger \n\t\tor perceived danger, even when fleeing could actually be worse.',
			   71: 'Paranoia \n\t\tYou are convinced that there is a person or organization persecuting and following you, \n\t\tand suspect everyone of being "in on it".',
			   72: 'Paranoia \n\t\tYou are convinced that there is a person or organization persecuting and following you, \n\t\tand suspect everyone of being "in on it".',
			   73: 'Persona Non-grata \n\t\tYou were an embassy employee with diplomatic immunity. When you were associated with espionage \n\t\tyou were kicked out of a country (choose one). You are not allowed to return.',
			   74: 'Persona Non-grata \n\t\tYou were an embassy employee with diplomatic immunity. When you were associated with espionage \n\t\tyou were kicked out of a country (choose one). You are not allowed to return.',
			   75: 'Phobia \n\t\tYou have a strong unreasonable fear.',
			   76: 'Phobia \n\t\tYou have a strong unreasonable fear.',
			   77: 'Sadism \n\t\tYou receive pleasure from causing pain and suffering to others.',
			   78: 'Sadism \n\t\tYou receive pleasure from causing pain and suffering to others.',
			   79: 'Selective Eating Disorder \n\t\tYou have only a few things you can eat (choose two from each food group). \n\t\tAll others make you retch, gag, or vomit.',
			   80: 'Selective Eating Disorder \n\t\tYou have only a few things you can eat (choose two from each food group). \n\t\tAll others make you retch, gag, or vomit.',
			   81: 'Social Anxiety \n\t\tUnfamiliar social situations cause a physical panic in you, causing sweating, \n\t\ttrembling, palpitations, and nausea.',
			   82: 'Social Anxiety \n\t\tUnfamiliar social situations cause a physical panic in you, causing sweating, \n\t\ttrembling, palpitations, and nausea.',
			   83: 'Luddite \n\t\tYou mistrust any technology invented after you were born, have trouble mastering it, \n\t\tand avoid it as much as possible.',
			   84: 'Luddite \n\t\tYou mistrust any technology invented after you were born, have trouble mastering it, \n\t\tand avoid it as much as possible.',
			   85: 'Trigeminal Neuritis \n\t\tIf you do not take a daily anti-seizure pill, a slight breeze on your face feels like \n\t\tan "ice cream headache" or "brain freeze" at the outside corner of your nose.',
			   86: 'Trigeminal Neuritis \n\t\tIf you do not take a daily anti-seizure pill, a slight breeze on your face feels like \n\t\tan "ice cream headache" or "brain freeze" at the outside corner of your nose.',
			   87: 'Pacifist \n\t\tYou refuse to carry a weapon, or to fight except to save your life.',
			   88: 'Pacifist \n\t\tYou refuse to carry a weapon, or to fight except to save your life.',
			   89: 'Unilateral Hearing Loss \n\t\tYou are deaf in one ear. It is difficult to locate where sounds are coming from, \n\t\tand may take several repetitions to pinpoint the source.',
			   90: 'Unilateral Hearing Loss \n\t\tYou are deaf in one ear. It is difficult to locate where sounds are coming from, \n\t\tand may take several repetitions to pinpoint the source.',
			   91: 'Impulse Control Disorder \n\t\tYou act without thinking of the consequences, causing social embarrassment, \n\t\tmoney problems from compulsive shopping, and danger from "leaping before you look".',
			   92: 'Impulse Control Disorder \n\t\tYou act without thinking of the consequences, causing social embarrassment, \n\t\tmoney problems from compulsive shopping, and danger from "leaping before you look".',
			   93: 'Unilateral Vision Loss \n\t\tYou are blind in one eye. You have a loss of depth perception. \n\t\tYou may wear a glass eye if you choose.',
			   94: 'Unilateral Vision Loss \n\t\tYou are blind in one eye. You have a loss of depth perception. \n\t\tYou may wear a glass eye if you choose.',
			   95: 'Vertigo \n\t\tYou have a sensation of dizziness and nausea, as if everything is spinning around you. \n\t\tAttacks may come randomly, and last about 20 minutes.',
			   96: 'Vertigo \n\t\tYou have a sensation of dizziness and nausea, as if everything is spinning around you. \n\t\tAttacks may come randomly, and last about 20 minutes.',
			   97: 'Congenital Analgesia \n\t\tYou have an insensitivity to somatosensory stimuli, such as heat, cold, touch, and pain \n\t\tin your fingers and toes. Sometimes you cannot feel touch at all.',
			   98: 'Congenital Analgesia \n\t\tYou have an insensitivity to somatosensory stimuli, such as heat, cold, touch, and pain \n\t\tin your fingers and toes. Sometimes you cannot feel touch at all.',
			   99: 'Lame \n\t\tYou walk with a cane. You are unable to run, and have difficulty climbing stairs or rough slopes.',
			   100: 'Lame \n\t\tYou walk with a cane. You are unable to run, and have difficulty climbing stairs or rough slopes.',
}


phobias = ['Arachnaphobia - The fear of spiders. This includes cobwebs and trapdoors.',
		   'Ophidiophobia - The fear of snakes.',
		   'Acrophobia - The fear of heights.',
		   'Agoraphobia - The fear of open or crowded spaces.',
		   'Cynophobia - The fear of dogs.',
		   'Astraphobia - The fear of thunder / lightning.',
		   'Claustrophobia - The fear of small spaces. This includes elevators, trams, small rooms, and other enclosed spaces.',
		   'Mysophobia - The fear of germs.',
		   'Aerophobia - The fear of flying.',
		   'Carcinophobia - The fear of cancer.',
		   'Trypophobia - The fear of holes.',
		   'Thanatophobia - The fear of death.',
		   'Glossophobia - The fear of public speaking.',
		   'Monophobia - The fear of being alone.',
		   'Atychiphobia - The fear of failure.',
		   'Ornithophobia - The fear of birds.',
		   'Alektorophobia - The fear of chickens.',
		   'Enochlophobia - The fear of crowds.',
		   'Aphenphosmphobia - The fear of intimacy. This involves the fear of ebing touched and the fear of love.',
		   'Trypanophobia - The fear of needles.',
		   'Aquaphobia - The fear of water. This includes being in water and even near water.',
		   'Anthrophobia - The fear of people.',
		   'Autophobia - The fear of abandonment.',
		   'Haemophobia - The fear of blood. The sight of blood can cause fainting or panic attacks.',
		   'Gamophobia - The fear of commitment.',
		   'Anatidaephobia - The fear of ducks.',
		   'Pyrophobia - The fear of fire.',
		   'Ranidaphobia - The fear of frogs.',
		   'Galeophobia - The fear of sharks.',
		   'Athazagoraphobia - The fear of being forgotten or forgetting.',
		   'Katsaridaphobia - The fear of cockroaches. This can lead to an excessive cleaning disorder.',
		   'Iatrophobia - The fear of doctors.',
		   'Pediophobia - The fear of dolls.',
		   'Ichthyophobia - The fear of fish. This phobia concerns any, from small to large, dead or live fish.',
		   'Achondroplasiaphobia - The fear of little people.',
		   'Mottephobia - The fear of moths.',
		   'Zoophobia - The fear of animals.',
		   'Bananaphobia - The fear of bananas.',
		   'Sidonglobophobia - The fear of cotton balls or plastic foams, even their sound.',
		   'Scelerophobia - The fear of crime involves being afraid of burglars, attackers, or crime in general.',
		   'Cibophobia - The fear of food.',
		   'Phasmophobia - The fear of ghosts.',
		   'Equinophobia - The fear of horses.',
		   'Musophobia - The fear of mice.',
		   'Catoptrophobia - The fear of mirrors. Being afraid of seeing something you do not like in the mirror.',
		   'Agliophobia - The fear of pain. Being afraid or anxious that something painful will happen to you.',
		   'Tokophobia - The fear of pregnancy and childbirth.',
		   'Telephonophobia - The fear of talking on the phone. Most of these phobics prefer texting or emailing.',
		   'Pogonophobia - The fear of beards.',
		   'Omphalophobia - The fear of belly buttons.',
		   'Hippopotomonstrosesquippedaliophobia - The fear of long words.',
		   'Xenophobia - The fear of the unknown.',
		   'Vehophobia - The fear of driving.',
		   'Achievemephobia - The fear of success.',
		   'Basiphobia - The fear of falling. In extreme cases, people refuse to walk, use stairs, or even stand up.',
		   'Theophobia - The fear of God. It causes an irrational fear of religion in general.',
		   'Ailuorphobia - The fear of cats.',
		   'Metathesiophobia - The fear of change.',
		   'Globophobia - The fear of balloons.',
		   'Nyctophobia - The fear of darkness.',
		   'Androphobia - The fear of men.',
		   'Phobophobia - The fear of fear. The though of being afraid of objects or situations is scary.',
		   'Philophobia - The fear of love. Being scare of falling in love or becoming emotionally attached.',
		   'Triskaidekaphobia - The fear of the number 13. It is often associated with bad luck and evilness.',
		   'Emotophobia - The fear of vomiting. Loss of one\'s self control is often the biggest fear here.',
		   'Gephyrophobia - The fear of bridges.',
		   'Entomophobia - The fear of bugs and insects OR Acarophobia - The fear of biting insects.',
		   'Lepidopterophobia - The fear of butterflies. This phobia usually means the fear of most winged insects.',
		   'Panophobia - The fear of everything. A constant state of fear that something terrible will happen.',
		   'Podophobia - The fear of feet. Some people fear touching or even looking at feet, even their own.',
		   'Paraskevidekatriaphobia - The fear of Friday the 13th.',
		   'Somniphobia - The fear of sleep. Being terrified of what might happen if one falls asleep.',
		   'Gynophobia - The fear of women.',
		   'Apiphobia - The fear of bees. Many people fear bees because they are afraid of being stung.',
		   'Koumpounophobia - The fear of buttons. Clothes with buttons are usually avoided by these phobics.',
		   'Pseudodysphagia - The fear of choking.',
		   'Bathophobia - The fear of depths including lakes, tunnels, caves, etc.',
		   'Cacomorphobia - The fear of fat people.',
		   'Gerascophobia - The fear of getting old.',
		   'Chaetophobia - The fear of hair; other peoples\' hair and animal hair.',
		   'Nosocomephobia - The fear of hospitals.',
		   'Ligyrophobia - The fear of loud noises.',
		   'Didaskaleinophobia - The fear of school.',
		   'Technophobia - The fear of technology.',
		   'Chronophobia - The fear of the future. Chronophobia is a persistent fear of what is to come and the passing of time.',
		   'Spheksophobia - The fear of wasps.',
		   'Ergophobia - The fear of work.',
		   'Coulrophobia - The fear of clowns.',
		   'Allodoxaphobia - The fear of opinions. Being afraid of hearing what others are thinking of you.',
		   'Samhainophobia - The fear of Halloween.',
		   'Photophobia - The fear of light.',
		   'Disposophobia - The fear of getting rid of stuff. This triggers extreme collecting or hoarding of things.',
		   'Numerophobia - The fear of numbers.',
		   'Ombrophobia - The fear of rain. Many fear the rain because of accompanying stormlike conditions.',
		   'Coasterphobia - The fear of roller coasters.',
		   'Thalassophobia - The fear of the ocean.',
		   'Scoleciphobia - The fear of worms.',
		   'Kinemortophobia - The fear of zombies.',
		   'Myrmecophobia - The fear of ants.',
		   'Taphophobia - The fear of being buried alive by mistake and wake up in a coffin deep underground.',
]

languages = {10: 'Afrikaans',	#go to 68
			 11: 'Amharic (Ethiopia)',
			 12: 'Arabic',
			 13: 'Armenian',
			 14: 'Basque (Northern Spain)',
			 15: 'Bengali',
			 16: 'Berber',
			 17: 'Bulgarian',
			 18: 'Burmese',
			 19: 'Chinese (Cantonese)',
			 20: 'Chinese (Mandarin)',
			 21: 'Czech',
			 22: 'Danish',
			 23: 'Dutch',
			 24: 'Filipino (Tagalog)',
			 25: 'Finnish',
			 26: 'French',
			 27: 'German',
			 28: 'Greek',
			 29: 'Gujarati (India Gujarat Region)',
			 30: 'Hebrew',
			 31: 'Hindi',
			 32: 'Hungarian',
			 33: 'Indonesian',
			 34: 'Italian',
			 35: 'Japanese',
			 36: 'Khmer (Cambodian)',
			 37: 'Korean',
			 38: 'Kurdish',
			 39: 'Lao (Laotian)',
			 40: 'Latvian',
			 41: 'Lithuanian',
			 42: 'Malay',
			 43: 'Mongolian',
			 44: 'Nepal',
			 45: 'Norwegian',
			 46: 'Pashto',
			 47: 'Persian Farsi',
			 48: 'Polish',
			 49: 'Portuguese',
			 50: 'Punjabi',
			 51: 'Quechua (Bolivia / Peru)',
			 52: 'Russian',
			 53: 'Serbo-Croatian',
			 54: 'Somali',
			 55: 'Spanish',
			 56: 'Swahili',
			 57: 'Swedish',
			 58: 'Tamil',
			 59: 'Thai',
			 60: 'Tibetan',
			 61: 'Turkish',
			 62: 'Ukranian',
			 63: 'Urdu',
			 64: 'Uyghur',
			 65: 'Uzbek',
			 66: 'Vietnamese',
			 67: 'Yoruba',
			 68: 'Zulu',
}

profLang = ['Elementary (d4)', 'Basic (d6)', 'Advanced (d8)', 'Fluent (d10)', 'Native Speaker (d12)']

tradecraft = ['SIGINT', 'HUMINT', 'TECH', 'COMBAT']
tradeCraftAtts = {'SIGINT': 'Intellect', 'HUMINT': 'Suave or Nerve (Whichever is higher)', 'TECH': 'Intellect', 'COMBAT': 'Reflex'}
abilScore = {'Nerve': '', 'Suave': '', 'Pulse': '', 'Intellect': '', 'Reflex': ''}

specialSkills = ['Asset Handling',
				 'Analysis',
				 'Black Bag Ops',
				 'Climbing',
				 'Cryptography',
				 'Deception',
				 'Driving',
				 'Electronic Communications',
				 'Electronic Surveillance',
				 'Exfiltration / Infiltration',
				 'Explosives',
				 'First Aid',
				 'Forensics',
				 'Forgery',
				 'Guerrilla Tactics',
				 'Hacking',
				 'Hand to Hand Combat',
				 'Illusion / Sleight of Hand',
				 'Interrogation',
				 'Marksmanship / Weaponry',
				 'Paramilitary',
				 'Physical Surveillance',
				 'Pilot Aircraft',
				 'Pilot Watercraft',
				 'Psyops',
				 'Parachuting',
				 'Soft Skills',
				 'Street Delivery',
				 'Survival',
]



language = ""
impair = ""
# Function Definitions

#################
def statGen():
	global abilScore
	count = 0
	scoreTypee = ""
	scores = ""
	print("Ability Scores:")
	for i in range(5):
		roll = random.randrange(1,101)

		if roll >= 81:
			scoreTypee = 'cyan'
			attDie = "d12 (Elite)"
		elif roll < 81 and roll >= 61:
			scoreTypee = 'green'
			attDie = "d10 (Hardened)"
		elif roll < 61 and roll >= 41:
			scoreTypee = 'yellow'
			attDie = "d8 (Healthy)"
		elif roll < 41 and roll >= 21:
			scoreTypee = 'magenta'
			attDie = "d6 (Average)"
		elif roll <21:
			scoreTypee = 'red'
			attDie = "d4 (Weak)"

		if count == 0:
			print("\tNerve: " + colored(attDie, scoreTypee))
			scores += "Nerve: " + colored(attDie, scoreTypee) + " "
			abilScore['Nerve'] = attDie
		elif count == 1:
			print("\tSuave: " + colored(attDie, scoreTypee))
			scores += "Suave: " + colored(attDie, scoreTypee) + " "
			abilScore['Suave'] = attDie
		elif count == 2:
			print("\tPulse: " + colored(attDie, scoreTypee))
			scores += "Pulse: " + colored(attDie, scoreTypee) + " "
			abilScore['Pulse'] = attDie
		elif count == 3:
			print("\tIntellect: " + colored(attDie, scoreTypee))
			scores += "Intellect: " + colored(attDie, scoreTypee) + " "
			abilScore['Intellect'] = attDie
		elif count == 4:
			print("\tReflex: " + colored(attDie, scoreTypee))
			scores += "Reflex: " + colored(attDie, scoreTypee) + " "
			abilScore['Reflex'] = attDie

		count = count + 1

	count = 0
	#print("Ability Scores: " + scores)

#################
def genName():
	d2 = random.randrange(0,2)

	gend = gender[d2]
	if gend == 'male':
		name = random.choice(maleFirst) + " " + random.choice(surnames)
		nameColor = 'yellow'
	else:
		name = random.choice(femFirst) + " " + random.choice(surnames)
		nameColor = 'magenta'

	print("Name: " + colored(name, nameColor))
	print("Gender: " + colored(gend.title(), nameColor))

#################
def shuffler():
	for i in range(20):
		random.shuffle(maleFirst)
		random.shuffle(femFirst)
		random.shuffle(surnames)
		random.shuffle(background)

#################
def genBackground():
	global impair
	d23 = random.randrange(0,23)
	print("Background: " + colored(background[d23], 'yellow'))
	impair = random.choice(impairment)

	if impair == 'yes':
		impairmentSel()
	else:
		pass

#################
def impairmentSel():
	d100 = random.randrange(1,101)
	genImpair = impairments[d100]
	print("Impairments: " + colored(genImpair, 'red'))

	if genImpair[:6] == 'Phobia':
		xx = random.choice(phobias)
		print("Phobia: " + colored(xx, 'red' ))

#################
def languageSel():
	global language
	#language = "English"
	d4 = random.randrange(1,5) 	#choose a number of languages

	y = d4
	for i in range(y):
		langDie = random.randrange(10,69) #skip 24, because it's the default language for all agents

		count = i
		if count == 0:
			language = "English " + "- " + profLang[4]

		elif count == 1:
			language += "\n\t   " + languages[langDie] + " - " + random.choice(profLang)

		elif count == 2:
			if languages[langDie] in language:
				langDie = random.randrange(10,69)
				language += "\n\t   " + languages[langDie] + " - " + random.choice(profLang)
			else:
				language += "\n\t   " + languages[langDie] + " - " + random.choice(profLang)

		elif count == 3:
			if languages[langDie] in language:
				langDie = random.randrange(10,69)
				language += "\n\t   " + languages[langDie] + " - " + random.choice(profLang)
			else:
				language += "\n\t   " + languages[langDie] + " - " + random.choice(profLang)
		#count = count - 1

	print("Languages: " + language)

#################
def profSel():
	global language

	xx = random.choice(profLang)
	language += " - " + xx

#################
def specSkills():
	moop = tradecraft
	print("Strong Tradecrafts:")

	for i in range(3):
		tradeC = random.choice(moop)
		dieVal = tradeCraftAtts[tradeC]

		if dieVal == 'Suave or Nerve (Whichever is higher)':
			s = abilScore['Suave']
			s = s[0:3].strip('d ')
			n = abilScore['Nerve']
			n = n[0:3].strip('d ')

			if int(s) > int(n):
				#print("s: " + str(s) + " n: " + str(n))
				dieVal1 = abilScore['Suave']
			elif int(s) < int(n):
				#print("s: " + str(s) + " n: " + str(n))
				dieVal1 = abilScore['Nerve']
			elif int(s) <= int(n):
				#print("s: " + str(s) + " n: " + str(n))
				s_or_n = ['Suave', 'Nerve']
				dieVal1 = abilScore[random.choice(s_or_n)]
		else:
			dieVal1 = abilScore[tradeCraftAtts[tradeC]]


		if tradeC == 'HUMINT':
			print("\t" + tradeC + " - " + tradeCraftAtts[tradeC] + " - " + dieVal1)

		elif tradeC == 'SIGINT':
			print("\t" + tradeC + " - " + tradeCraftAtts[tradeC] + " - " + dieVal1)

		elif tradeC == 'COMBAT':
			print("\t" + tradeC + " - " + tradeCraftAtts[tradeC] + " - " + dieVal1)

		elif tradeC == 'TECH':
			print("\t" + tradeC + " - " + tradeCraftAtts[tradeC] + " - " + dieVal1)

		moop.remove(tradeC)

	print("Weak Tradecrafts:")
	#print(weakDie[0:2])
	#print("DEBUG LINE: tradeCraftAtts = " + tradeCraftAtts[moop[0]])

	if tradeCraftAtts[moop[0]] == 'Suave or Nerve (Whichever is higher)':
		s = abilScore['Suave']
		s = s[0:3].strip('d ')
		n = abilScore['Nerve']
		n = n[0:3].strip('d ')

		if int(s) > int(n):
			#print("s: " + str(s) + " n: " + str(n))
			weakDie = abilScore['Suave']
		elif int(s) < int(n):
			#print("s: " + str(s) + " n: " + str(n))
			weakDie = abilScore['Nerve']
		elif int(s) <= int(n):
			#print("s: " + str(s) + " n: " + str(n))
			s_or_n = ['Suave', 'Nerve']
			weakDie = abilScore[random.choice(s_or_n)]


		if 'd4' in weakDie:
			print("\t" + moop[0] + " - d4 (Weak)")

		elif 'd6' in weakDie:
			print("\t" + moop[0] + " - d4 (Weak)")

		elif 'd8' in weakDie:
			print("\t" + moop[0] + " - d4 (Weak)")

		elif 'd10' in weakDie:
			print("\t" + moop[0] + " - d6 (Average)")

		elif 'd12' in weakDie:
			print("\t" + moop[0] + " - d6 (Average)")

	else:
		weakDie = abilScore[tradeCraftAtts[moop[0]]]

		if 'd4' in weakDie:
			print("\t" + moop[0] + " - d4 (Weak)")

		elif 'd6' in weakDie:
			print("\t" + moop[0] + " - d4 (Weak)")

		elif 'd8' in weakDie:
			print("\t" + moop[0] + " - d4 (Weak)")

		elif 'd10' in weakDie:
			print("\t" + moop[0] + " - d6 (Average)")

		elif 'd12' in weakDie:
			print("\t" + moop[0] + " - d6 (Average)")

	#print("\t" + moop[0] + " - " + tradeCraftAtts[moop[0]])
#From here and below go ahead and do the special skills (5 random choices, 6 if impaired)

	if impair == 'yes':
		specCopy = specialSkills
		print("Special Skills:")
		for i in range(6):
			x = random.choice(specCopy)
			print("\t" + colored(x, 'green'))
			specCopy.remove(x)

	else:
		specCopy = specialSkills
		print("Special Skills:")
		#5 skills
		for i in range(5):
			x = random.choice(specCopy)
			print("\t" + colored(x, 'green'))
			specCopy.remove(x)

#################
def mainRoutine():
	shuffler()
	genName()
	statGen()
	print("Reputation: 0 [Newly Minted Agent]")
	genBackground()
	languageSel()
	specSkills()
	print("")

#################

# Main Routine
mainRoutine()
