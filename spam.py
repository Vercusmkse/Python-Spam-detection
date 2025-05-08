spamchars = ["!","?","$","*","#","%","+","_"]
spamkeywords = ["limited offer","act now","exclusive","urgent","immediate","deadline","only a few left","hurry","last chance","today only","final hours","while supplies last","one time","expires","never again","don’t miss","rush","time-sensitive","offer expires","instant access","closing soon","final call","once in a lifetime","limited time","now or never","flash sale","countdown","last minute deal","rare opportunity","ends tonight","","private","confidential","winner","selected","guaranteed","personal","secret","exclusive access","membership","you have been chosen","claim","beneficiary","award","pre-approved","eligible","certified","not shared","sensitive","protection","verified","urgent","limited time","priority access","restricted information","top secret","special offer","confidential deal","privileged","exclusive rights","secure claim","","miracle","amazing","incredible","magic","once in a lifetime","revolutionary","sensational","unbelievable","phenomenal","fantastic","life-changing","unmatched","breakthrough","top-notch","stunning","spectacular","unparalleled","outstanding","extraordinary","supreme","astounding","remarkable","unprecedented","jaw-dropping","breathtaking","groundbreaking","mind-blowing","majestic","unrivaled","ultimate","","earn","discount","pure profit","credit","investment","loan","save","million dollars","financial freedom","get paid","bankruptcy","refinance","money back","debt","extra income","no fees","best rates","cash bonus","extra cash","easy money","penny stocks","wealth","no hidden charges","no hidden costs","be your own boss","unsecured credit","lower interest rates","accept credit cards","best mortgage rates","cashback","lottory","","date of birth","social security number","phone number","home address","credit card details","login details","password","bank details"]
major_flags = [ "doctor", "pill", "breast", "viagra", "windows xp", "regalis", "viagra", "rolex", "extremely cheap", "soffttwares", "sooftware", "easy download", "charity", "medication", "medicinal", "specially formulated", "onlly", "ciallis", "tabs", "meds", "death", "dvd", "prescription"]


def spamdetection():
    with open("email.txt", "r", errors="ignore") as f:
        message = f.read()
    # Making the message in the email to be lower case.
    message = message.lower()
    # the starting the count at 0
    spam = 0
    symbol = 0
    # i am check the length of the email
    if len(message) < 20 or len(message) > 8000:
        print("spam")
    else:
        # I am going count how time occurrences of spam keywords in the message.
        for char in spamkeywords:
            if char in message:
                spam += 1
        for sym in spamchars:
            if sym in message:
                symbol += 1
        for flag in major_flags:
            if flag.lower() in message:
                print("spam")
                return
        # I am going make if statem saying if count is greater then the spam thershold is 2 going return spam else it will return notspam.
        if spam >= 2 and symbol > 1:
            print("spam")
        else:
            print("notspam")


spamdetection()