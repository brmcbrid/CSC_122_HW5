# CSC 122
# Keno Lottery Game
# by <your name>
 
# Your solution code to implement the required functions goes here
 
def main():
    random.seed(0)  # this sets the random numbers to a default known set for testing
    print(f"Keno Lottery Game\n")
    picks = [0] * 10
    keno = [0] * 20
    getPicks(picks)
    generateKeno(keno)
    count,matches = checkMatches(picks,keno)
    if count == 5:
        prize = "You have won $1"
    elif count == 6:
        prize = "You have won $7"
    elif count == 7:
        prize = "You have won $25"
    elif count == 8:
        prize = "You have won $250"
    elif count == 9:
        prize = "You have won $2,500"
    elif count == 10:
        prize = "You have won $250,000"
    else:
        prize = "You did not win a prize."
        
    print(f"\nYour picks are:{picks}")
    print(f"\nThe winning numbers are:{keno}")
    print(f"\nYou matched:{matches}")
    print(f"\nYou matched {count} of 20 numbers. {prize}")


if __name__ == "__main__":
          main()