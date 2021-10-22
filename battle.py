#Alfredo Izak Figueroa
#%%
import random

# -------------Acomodando la tabla, jugadores y escondiendo los barcos-------------

board = []

for x in range(0,10):
  board.append(["o"] * 10)

def print_board(board):
  for row in board:
    print (" ".join(row))

print("Juguemos Battleship!")
print("Este es un juego de 2 jugadores")

player_1 = input("Escribe el nombre del primer jugador: ")
player_2 = input("Escribe el nombre del segundo jugador: ")
players = [player_1, player_2]

def random_player(players):
    return random.choice(players)

def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
  return random.randint(0,len(board[0])-1)

if random_player(players) == player_1:
  print(player_1, "Comenzar el juego.")
else:
  print(player_2, "Comenzar el juego.")
  
ship_row_1 = random_row(board)
ship_col_1 = random_col(board)
# print (ship_row_1)
# print (ship_col_1)

ship_row_2 = random_row(board)
ship_col_2 = random_col(board)
# print (ship_row_2)
# print (ship_col_2)

print_board(board)

player_start = random_player(players)

# ----------------------------Jugando el juego----------------------------



hit_count = 0

for turn in range(9):
     guess_row = int(input("Adivina fila: (Valores aceptados: 0-9) "))
     guess_col = int(input("Adivina columna: (Valores aceptados: 0-9) "))

     if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
            hit_count = hit_count + 1
            board[guess_row][guess_col] = "*"
            print ("Felicidades! ")
            if hit_count == 1:
                   print("Hundiste el primer barco de guerra!") 
            elif hit_count == 2:
                   print("Hundiste el segundo barco de guerra! Ganaste!")
                   print_board(board)
                   break
     else:
            if (guess_row < 0 or guess_row > 9)  or (guess_col < 0 or guess_col > 9):
                   print ("Oops, eso ni siquiera esta en el oceano.")
            elif(board[guess_row][guess_col] == "X"):
                   print ("Ya habias disparado ahi.")
            else:
                 print ("Fallaste tu tiro!")
                 board[guess_row][guess_col] = "X"
            print (turn + 1, "turno")
     print_board(board)
print ("Barco 1 esta escondido:")    
print (ship_row_1)
print (ship_col_1)

print ("Barco 2 esta escondido:")    
print (ship_row_2)
print (ship_col_2)
# %%
