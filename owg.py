def main():

    UserInput = input ("Type your key word: ")
    print('Your word is...\n --- ' + UserInput + ' ---')

    regularInput = UserInput
    lowerCase = UserInput.lower()
    capitalLetter = UserInput.capitalize()

    symbols = '0','!','@','#','$','%','^','&','*'
    
    updatE = regularInput
    update = lowerCase
    Update = capitalLetter

    print(regularInput)
    print(lowerCase)
    print(capitalLetter)

    for k in range(1, 9): # symbols + word / word + symbol

        for numberCount in range(1, 1001): # word + number up t0 1000 / number up to 1000 + word

            print(capitalLetter + str(numberCount))

            print(lowerCase + str(numberCount))

            print(regularInput + str(numberCount))

            print(str(numberCount) + capitalLetter)

            print(str(numberCount) + lowerCase)

            print(str(numberCount) + regularInput)

            print(symbols[k] + lowerCase + str(numberCount)) # symbol + word + number / word + number + symbol / symbol + word + number + symbol / symbol + number +word

            print(symbols[k] + capitalLetter + str(numberCount))

            print(symbols[k] + regularInput + str(numberCount))

            print(lowerCase + str(numberCount) + symbols[k])

            print(capitalLetter + str(numberCount) +  symbols[k])

            print(regularInput + str(numberCount) +  symbols[k])

            print(symbols[k] + lowerCase + str(numberCount) + symbols[k])

            print(symbols[k] + capitalLetter + str(numberCount) +  symbols[k])

            print(symbols[k] + regularInput + str(numberCount) +  symbols[k])

            print(symbols[k] + str(numberCount) + capitalLetter)

            print(symbols[k] + str(numberCount) + lowerCase)

            print(symbols[k] + str(numberCount) + regularInput)



    for yearCount in range(1920, 2031): # word + year / year + word

        print(capitalLetter + str(yearCount))

        print(lowerCase + str(yearCount))

        print(regularInput + str(yearCount))

        print(str(yearCount) + capitalLetter)

        print(str(yearCount) + lowerCase)

        print(str(yearCount) + regularInput)

   

    for k in range(1, 9): # symbols + word / word + symbol

        print(symbols[k] + lowerCase)

        print(symbols[k] + capitalLetter)

        print(symbols[k] + regularInput)

        print(lowerCase + symbols[k])

        print(capitalLetter + symbols[k])

        print(regularInput + symbols[k])



        for yearCount in range(1920, 2031): # symbols + word + year / word + year + symbol / symbol + word + year + symbol

            print(symbols[k] + lowerCase + str(yearCount))

            print(symbols[k] + capitalLetter + str(yearCount))

            print(symbols[k] + regularInput + str(yearCount))

            print(lowerCase + str(yearCount) + symbols[k])

            print(capitalLetter + str(yearCount) +  symbols[k])

            print(regularInput + str(yearCount) +  symbols[k])

            print(symbols[k] + lowerCase + str(yearCount) + symbols[k])

            print(symbols[k] + capitalLetter + str(yearCount) +  symbols[k])

            print(symbols[k] + regularInput + str(yearCount) +  symbols[k])



    i = 1

    while i < 9:

        print(updatE) # regularInput udpate

        print(update) # Lower case update

        print(Update) # Capital update

        i += 1

    

        newString =  updatE + str(i)  # word + number1-12-123-1234( same for next two lines )

        newStrings =  update + str(i)

        newStringS =  Update + str(i)

        updatE = newString

        update = newStrings

        Update = newStringS

        

        j = 1

        while j < 10:

            print(symbols[j-1] + updatE) #symbol +  word + number1-12-123-1234( same for next two lines )

            print(symbols[j-1] + update)

            print(symbols[j-1] + Update)

            j += 1



main()

