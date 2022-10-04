import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { # slot symbols
    "A": 3,
    "B": 4,
    "C": 5,
    "D": 6
}

symbol_value = { # winning values
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): # checks if the symbol is the same in the same row for all columns
        symbol = columns[0][line]
        for column in columns: # loops through all columns checking symbol
            symbol_to_check = column[line]
            if symbol != symbol_to_check: # if symbols aren't the same, check next line
                break
        else:
            winnings += values[symbol] * bet # user wins multipler of symbol * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .items gives key and value of dictionary values
        for _ in range(symbol_count): # _ is an anonymous variable used when you just need to loop through something
            all_symbols.append(symbol) # create a list of all symbols within symbol_count

    columns = []
    for _ in range(cols): # create individual columns of symbols for value in cols
        column = []
        current_symbols = all_symbols[:] # copies a list [:] is the slice operator
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) # finds the value added and removes it from the list
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): # loop through every row transposing columns from horizontal to vertical columns
        for i, column in enumerate(columns): # enumerate gives you the index as well as the item
            if i != len(columns) - 1:
                print(column[row], end=" | ") # prints symbols of the row on single line
            else:
                print(column[row], end="") # prints symbols of the row on single line

        print() # this is used to start a new line for each row

def deposit():
    while True: # keeps checking until player deposits a correct amount
        amount = input("How much would you like to deposit? $") 
        if amount.isdigit(): # checks if input is a positive number
            amount = int(amount) # changes amount to an int
            if amount > 0:
                break # breaks the loop if the amount is positive and higher than 0
            else: # tells the player to enter higher than 0
                print("Amount must be greater than $0.")
        else: # tells the player to enter a positive number if they tried to input anything else
            print("Please enter a positive number.")

    return amount

def get_number_of_lines():
    while True: # keeps checking until player chooses a correct amount
        lines = input("Enter the number of lines to bet on (1-" +str(MAX_LINES) + ")? ") 
        if lines.isdigit(): # checks if input is a positive number
            lines = int(lines) # changes lines to an int
            if 1 <= lines <= MAX_LINES: # checks if lines is more than one and less than MAX_LINES
                break
            else: # tells the player to enter higher than 0
                print("Lines must be greater than 0.")
        else: # tells the player to enter a positive number if they tried to input anything else
            print("Please enter a positive number.")

    return lines

def get_bet():
    while True: # keeps checking until player deposits a correct amount
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit(): # checks if input is a positive number
            amount = int(amount) # changes amount to an int
            if MIN_BET <= amount <= MAX_BET: # checks if bet amount is more than MIN_BET and less than MAX_BET
                break
            else: # tells the player to enter higher than 0
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else: # tells the player to enter a positive number if they tried to input anything else
            print("Please enter a positive number.")

    return amount

def spin(balance): # starts the game
    lines = get_number_of_lines()
    
    while True: # checks if the players bet is within the amount of their balance
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines", *winning_lines) # * passes all lines from winning_lines
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play or press q to quit.")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()