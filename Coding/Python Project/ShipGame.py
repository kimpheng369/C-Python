class Ship:
    def __init__(self, x: int, y: int, name: str) -> None:
#_________________Initialize the ship with coordinates, name, and a sunk status (False means it's afloat)________
        self.x = x
        self.y = y
        self.name = name
        self.sunk = False    #(Indicates whether the ship has sunk)

    def got_hit(self):
#_________________Marks the ship as sunk when it gets hit_________________
        self.sunk = True

    def has_sunk(self) -> bool:
#_________________Returns whether the ship has sunk or not_________________
        return self.sunk

    def get_name(self) -> str:
#_________________Returns the name of the ship_________________
        return self.name

    def get_coord(self) -> tuple[int, int]:
#_________________Returns the coordinates of the ship as a tuple (x, y)_________________
        return self.x, self.y

    def __repr__(self) -> str:
#_________________Provides a string representation of the ship's current status_________________
        status = "sunk" if self.sunk else "Afloat"
        return f"{self.name}: {status}"

    @staticmethod
    def create_ships() -> list["Ship"]:
#_________________Creates ships by user input. Continues until 10 ships are created or "END SHIPS" is entered
        ships = []
        print("Creating ships...")
        while len(ships) < 10:
            user_input = input('> ')
            if user_input.strip().upper() == 'END SHIPS':
                break # Exit the loop if user inputs "END SHIPS"

            token = user_input.split()
            if len(token) != 3:
                print("Error: <symbol> <x> <y>")
#_________________Expected format is symbol followed by x and y coordinates_________________
                continue
#_________________Convert symbol to uppercase to handle case insensitivity_________________
            symbol = token[0].upper()
            try:
                x = int(token[1])
                y = int(token[2])
            except ValueError:
                print(f"Error: ({', '.join(token)}) is an invalid coordinate")
                continue

#_________________Validations for symbol and coordinates_________________
            if symbol < 'A' or symbol > 'J':
                print("Error: symbol must be between 'A' _ 'J'")
                continue
            if x < 0 or y < 0 or x >= 5 or y >= 5: # (Assuming a 5x5 board)
                print(f"Error: ({x}, {y}) is out of bounds on 5x5 board")
                continue
            if any(ship.x == x and ship.y == y for ship in ships):
                print(f"Error: ({x}, {y}) is already occupied by another ship.")
                continue
            if any(ship.name == f'Ship{symbol}' for ship in ships):
                print(f"Error: symbol '{symbol}' is already taken.")
                continue

            #(If all validations pass, create the ship)
            ships.append(Ship(x, y, f'Ship{symbol}'))
            print(f'Success! Ship{symbol} added at ({x}, {y})')

        print(f"{len(ships)} ships added.")
        return ships

def print_board(ships):
#_________________Prints the current game board_________________
    board = [[' ' for _ in range(5)] for _ in range(5)] # (Create a 5x5 empty board)
    for ship in ships:
        if ship.has_sunk():
            board[ship.y][ship.x] = 'X' # (Mark the ship as sunk with 'X')
        else:
            board[ship.y][ship.x] = ship.get_name()[-1] # (Mark the ship with its last character (e.g., 'ShipA' -> 'A'))

        print("_______")
        for row in board:
            print('|' + ''.join(row) + '|') # (Print each row of the board)
        print('_______')

def main():
#_________________Create ships based on user input_________________
    ships = Ship.create_ships()
    print("Game started. Fire at Will!")

    attempts = 10
    for attempt in range(attempts):
        hit = False
        while True:
            try:
                # (Take the user's input for coordinates and parse it)
                x, y = map(int, input(f'Enter X, Y coordinate [{attempt + 1}/{attempts}]: ').split(','))
                if x < 0 or y < 0 or x >= 5 or y >= 5:
                    print("Invalid coordinates. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input format.Please enter in format X,Y.")

#_________________Check if the entered coordinates hit any ship_________________
        for ship in ships:
            if ship.x == x and ship.y == y:
                if not ship.has_sunk():
                    ship.got_hit() # (Mark the ship as hit (sunk))
                    hit = True
                    print(f'You sunk {ship.get_name()}!')
                else:
                    print(f'{ship.get_name()} is already sunk!')
                break
        else:
            print("MISS!") # (If no ship is hit)

        print_board(ships) # (Print the board after each attempt)

#_________________Check if all ships are sunk_________________
        if all(ship.has_sunk() for ship in ships):
            print("Congratulations! All ships are sunk.")
            break
    else:
        print("Game over! Not all ships were sunk.")

if __name__ == '__main__':
    main()