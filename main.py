import random 
# create subject

subject=[
    "shahrukh khan",
    'virat kohli',
    'modi ji',
    'Rahul gandhi',
    'a group of Monkey',
    'Shrama Ji ka ldka'
]

action =[
    'Lauches',
    "Cancel sports",
    "dancing",
    "orders breakfast",
    "celebrate"
]
places_or_things =[
    "at Red Fort",
    "in Mumbai Local Train",
    "during Ipl",
    " in shahdol",
    "at Gandhi Chouk"
]

# start the head line generation loop

while True:
    subject = random.choice(subject)
    action= random.choice(action)
    places_or_things=random.choice(places_or_things)

    headline =f"Breaking News:{subject} {action} {places_or_things}"
    print("\n "+headline)
    # ask user 

    user_input =input("/n Do you want another headline ? (yes/no)").strip().lower()
    if user_input =="no":
     break
# print good by 
print("\n "+"Thanks for using Fake News Headline Gnerator have a fun day")