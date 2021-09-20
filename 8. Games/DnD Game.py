    #import 
    import random
    
    #Init variables
    PlayerName = " "
    Home = " "
    Profession = " "
    Strength =[]
    Agility = []
    Intelligence = []

    #Defs
    def first_choice():
        
        print(" ")
        print("** You choose to go with Simon, he seems happy about your decision** ")
        print(" ")
        print("Good choice lad, come with me.\n I don't know if you notice on your way in the village, but there aren't many people around. Many have left the town.")
        print("Many who left were the strong young lads, promising boys that, in normal circumstances would be stayed and helped in town but now, with the plague well. ")
        print("You know {} ".format(PlayerName))
        print("We had a son, he left with the others to look for better working and living conditions. We are not allowed to leave so you might understand my concern for my boy")
        print(" ")
        Start = input(" ")
        print("**You arrived at Simon's home without any constrain, you enter the old house with broken windows, patched with wooden planks, you sense Simon is being truthfully about\n the whole town situation.   **")
        print("**As you enter the old house decorated you smell a wonderful aroma. There is a metal pot brewing possibly a stew of meat, next to it is a woman in her 40's mixing the content of the pot. **")
        print("**The house is decorated with a rug of a bear, a wooden table with many knife holes on it, and 3 hay beds, one seems not being used for a while so Simon's story checks out**")
        print(" ")
        print("**Simon explains the circumstances of your arrival to the woman.**")
        print("**The woman approaches you, and greets you. Inviting you to **")
        Start = input(" ")
        print("welcome {}, you must be tired from the journey from {}. Join us near the pot, im making chicken stew with what we have left, its not much but its honest food ".format(PlayerName,Home))
        print(" ")
        print("**Its been a while since you had a meal indoors. During your journey u mostly ate near roads where was safe to be **")
        print("**You were always told about to beware of whats layins inside the forests, nothing good has ever come from going alone anyway, you thought**")
        print(" ")
    
    def second_choice():
        print("DOPE")

    #Intro
    print(F" **Hello, You don't know me ... but I know you**")
    print(F" **Think of me as the Narrator of your tail, the wave in your ocean, the dark in your night** ")
    print(F"  ")
    print(F" **You dictate your path, you make your own decision, I just observe **")
    print(F" **Be wary that people might not be what they seem, never underestimate the power of a foe and most importantly..** ")
    print(F"  ")
    print(F" **Be truth to yourself** ")
    Start = input("You understand?")
    print(F"  ")
    #define attributes
    print(F" **Before i let you go, How good are you?**")
    Start = input(" Start trials")
    Strength.append(random.randrange(1,10))
    Agility.append(random.randrange(1,10))
    Intelligence.append(random.randrange(1,10))
    print(F" You start picking up heavy weights, your Strength is {Strength} ")
    print(F" You start Dodging rocks coming your way, your Agility is {Agility} ")
    print(F" You start decifer old riddles, your Intelligence is {Intelligence} ")
    print(F" ")
    print(F" **Hmm, was expecting better honestly**")
    print(F" **Alright, I think we are good now**")
    print(F" ")
    Start = input(" CLICK")
    print(F" **with a flick of his fingers, the narrator puts you on a long slumber**  ..see? i can do that ")
    print(F" **You woke up in outskirts of a city maybe, a village stand before you and behind it, a large enormous castle **")
    print(F" **Planty of empty farms, almost no living souls to be seen, you don't remember what you were doing before of all of this... strange you think but think not much of it**")

    #START
    print(" ")
    Start = input(" Do you remember ?")
    print(F" Welcome Stranger, I'm Simon ");
    print(F" ")
    print(F"**You are entering the realm of Umbria, We are a small village in the outskirts of our main castle.**") 
    print(F" ")
    print(F" Currently we are being ordered by the king to refuge in our homes... there is a plague you see.")
    PlayerName = input("Wait, i don't you your name Stranger. Tell me Who you are?\n")
    print(F" ")
   #Get input from the user   
    print(F"Ah... {PlayerName} , nice to meet you")
    Home = input("And, are you from around here? where are you from if I might ask")
    print(F"Interesting, hopefully {Home} is a good place to be born ")
    print(F" ")
    Profession = input(F" And what did you do in {Home}, your profession?")
    print(F"Let's hope you are as good with a sword as you are as a {Profession}")
    print(F"Well {PlayerName}, it been good to know but we might need to Run")
    print(F" ")
    print(F" Like I said, a plague is upon us and we need to run")
    print(F" beside that, the troops from Umbria are ordering everyone to stay in.")
    print(F" ")
    print(F"i can offer your shelter for today if u want")
    action_taken = input("*Do you want to take the offer of [S]helter or take your chances on your [O]wn \n*" )
    if action_taken == "S" or action_taken == "s":
        first_choice()
    else:
        second_choice()

    

