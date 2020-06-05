import random
import os.path
import datetime
import time

def Convert(end, start):
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    #return ('%d:%d:%d' %(hours, minutes, seconds))
    return ("{:0>2}:{:0>2}:{:0>2}".format(int(hours),int(minutes),int(seconds)))

def CurrentTime():
    now = datetime.datetime.now()
    return now.strftime('%I:%M:%S %p')


def MakeItLookOfficial(number):
    return ("$" + '{0:,.2f}'.format(number))


def Int(stuff):
    if type(stuff) == int:
        return stuff
    else:
        print(type(stuff))
        send = int(input("You have entered an invalid input. Please enter a number value"))
        return Int(send)


def intro():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")  # introduction
    print("Enter 'x' for bet to exit")
    print("Start time: ",CurrentTime(),"\n")


def starting():
    while True:
        starting = int(input("Starting player money: \t"))
        if Int(starting) == True:
            if starting < 0 or starting > 10000:
                print("Invalid amount. Must be from 0 to 10,000.")
            else:
                return starting


def betInput(total):
    while True:
        bet = input("Bet amount:\t")

        while True:
            if bet == 'x' or bet.isnumeric():
                break
            #print("type of bet:", type(bet))       #testing purpose
            bet = input("You have entered an invalid input. Please enter 'x' or a bet amount:\t")

        if bet == 'x':
            return -1
        elif int(bet) < 5:
            print("The minimum bet is 5.")
        elif int(bet) > 1000:
            print("The maximum bet is 1000.")
        elif int(bet) > total:
            print("You don't have enough money to make that bet.")
        else:
            return bet


def blackjack(bet, total):
    # print("Blackjack.")
    return int(total) + int(bet * 1.5)


def win(bet, total):
    # print("You won.")
    return int(total) + bet


def push(total):
    # print("Push.")
    return int(total)


def lose(bet, total):
    # print("You lost.")
    return bet - int(total)


def shuffle(list):
    random.shuffle(list)
    # print(list)
    # print(len(list))


def deal(list, times):
    a = []
    for i in range(times):
        a.append(list[len(list) - 1])
        list.pop(len(list) - 1)
    return a
    # print(a)


# def dealerStart(list, inputList):

def setupCards():
    cards = []
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    for i in range(4):  # assigns cards[] 52 unique cards
        for j in range(13):
            cards.append([suits[i], j + 1])
    shuffle(cards)
    return cards


def reset():
    pass


def value(list):
    totalValue = 0
    for i in range(len(list)):
        if list[i][1] >= 10:
            totalValue = totalValue + 10
        elif list[i][1] == 1:
            totalValue = totalValue + 11
        else:
            totalValue = totalValue + list[i][1]

    return totalValue


def show(list, times):
    for i in range(times):
        print(cardName(list[i][1]), "of", list[i][0])


def cardName(num):
    if num == 1:
        return 'Ace'
    elif num == 11:
        return 'Jack'
    elif num == 12:
        return 'Queen'
    elif num == 13:
        return 'King'
    else:
        return num


def bustWin(player, dealer, tot, bt):
    if player == dealer:
        print("\nYou tied!")
        return push(bt)
    elif player > 21:
        print("\nYou busted! You lose!")
        return lose(int(tot), bt)
    elif player == 21:
        print("\nBLACKJACK!")
        return int((tot) + (int(bt) * 1.5))
    elif player > dealer:
        print("\nYou are higher than Dealer! You win!")
        return win(int(tot), bt)
    elif player < dealer:
        if dealer > 21:
            print("\nDealer busted! You win!")
            return win(int(tot), bt)
        else:
            print("\nDealer is higher! You lose!")
            return lose(int(tot), bt)


#def calculations(betI, total):
#    betI = int(betI)
#    choice = random.randint(1, 100)  # chooses a random int from 1 - 100
#    if choice <= 5:  # Blackjack gets 5% chance of getting picked
#        total = blackjack(betI, total)  # ratio of 3:2 (payout)
#    elif choice <= 37 + 5:  # Win gets 37% chance of getting picked
#        total = win(betI, total)
#    elif choice <= 9 + 37 + 5:  # choice gets 9% chance of getting picked
#        total = push(betI)
#    else:  # lose gets 49% chance of getting picked
#        total = lose(betI, total)  # calculations for statistics
#
#    print("MONEY:", total)
#    # print("Total:", total)
#    print()
#    return total

def file():
    if os.path.isfile("f:\\hello.txt") == False:
        return 'd'
    with open("f:\\hello.txt", "r+") as file:
        reading = file.read()
        if reading == '':
            file.close()
            return 'x'
        elif int(reading) < 5:
            file.close()
            return int(reading)
        else:
            file.close()
            return int(reading)

def rewrite(replace):
    with open("f:\\hello.txt", "r+") as file:
        number = replace
        file.truncate(0)
        file.write(str(number))
        file.close()

def check(number):
    if number =='x':
        print("You were out of money.\nWe gave you 100 so you could play.")
        number = 100
        return number
    elif int(number) < 5:
        print("You did not have enough money.\nWe gave you 100 so you could play")
        number = int(number) + 100
        return number

def main():
    begin = time.time()
    intro()
    total = file()
    if total == 'd':
        print("Data file missing, resetting starting amount to 1000.")
        total = 1000
    elif total == 'x':
        print("You were out of money.\nWe gave you 100 so you could play.")
        total = 100
    elif int(total) < 5:
        print("You did not have enough money.\nWe gave you 100 so you could play")
        total = int(total) + 100
    #total = check(total)
    total = int(total)
    start = total

    while True:
        print("Player's money: ", MakeItLookOfficial(total))
        bet = betInput(total)
        if bet == -1:
            break
        deck = setupCards()
        player = deal(deck, 2)
        dealer = deal(deck, 2)

        print("\nDEALER'S SHOW CARD:")
        show(dealer, 1)

        print("\nYOUR CARDS:")
        show(player, 2)

        while True:

            if value(player) >= 21:  # checking for blackjack or bust
                break

            hs = input("\nHit or Stand? (h/s):\t")
            while True:
                if hs == 'h' or hs == 's':
                    break
                hs = input("You have entered an incorrect input. Please enter 'h' or 's':\t")
            if hs == 'h':
                player = player + deal(deck, 1)
                print("\nYOUR CARDS:")
                show(player, len(player))

            if hs == 's':
                print("\nDEALER'S CARDS:")
                while True:
                    if value(dealer) >= 17:  # Checking to see if dealer should draw or not
                        break
                    else:
                        dealer = dealer + deal(deck, 1)
                show(dealer, len(dealer))
                print()
                break

        print("\nYOUR POINTS:\t\t", value(player))
        print("\nDEALER'S POINTS:\t", value(dealer))

        #print(total - 1)

        total = bustWin(value(player), value(dealer), total, bet)
        test = 21
        print("\nPlayer money:", MakeItLookOfficial(total))

        playAgain = input("\nPlay again? (y/n):\t")
        while True:
            if playAgain == 'y' or playAgain == 'n':
                break
            playAgain = input("You have entered an invalid input. Please enter 'y' or 'n':\t")
        if playAgain == 'n':
            total = int(total)
            rewrite(total)
            break
        else:
            checkpoint = False
            print()
            dealer = reset()
            player = reset()
            if int(total) < 5:
                asking = input("You are out of money.\nWould you like to buy more chips? (y/n): ")
                if asking == 'n':
                    total = int(total)
                    rewrite(total)
                    break
                else:
                    total = int(total) + 100        #109940062  mdlwl67@lc

                    rewrite(total)
                    #print("Player's money", total)

            # total = check(total)

    print("\nYou gained:", total - start, "dollars!")
    print("\nCome again soon!")
    print("Stop time:\t\t",CurrentTime())
    end = time.time()
    Convert(end, begin)
    print("Elapsed time:\t",Convert(end, begin))
    print("What happens in Vegas stays in Vegas!")  # Conclusion


if __name__ == "__main__":
    main()
