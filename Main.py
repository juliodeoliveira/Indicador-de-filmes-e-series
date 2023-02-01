# Code by: Júlio de Oliveira
# Created in: 2022
# Github: https://github.com/juliodeoliveira
# If you have any problems, please contact me!

import search
import os

file_name = "Save.txt"

def createFile(name):
   '''
      This function creates a files, with any name you want, with any extension.

      Arguments: 
         1 ~ name - stands for the file name, you can put an extension too like '.html' or '.txt'.

      Returns: 
         None.
   '''
   try: 
      t = open(name, "wt+")
      t.close()

      #  ONLY FOR DEBUG!
      #print(f"File {name} created!")

   except:
      print("Error: Tried to create a file")



def fileExists(name):
   '''
      This function analysis if the file already exists.

      Arguments: 
         1 ~ name - stands for file name.
   '''
   try:
      f = open(name, "rt")
      return True
   
   except FileNotFoundError:
      return False


def writeFile(name, text):
   '''
      This function can write any text in any file.

      Arguments: 
         1 ~ name - is the name of the file you want to write in.
         
         2 ~ text - is the text you want to write in your file.
   '''

   try:
      f = open(name, "a")

   except:
      print("Something went wrong!")

   else: 
      try:
         f.write(text)
      except:
         print("Error: Tried do write archive!")


def readFile(name, ret=False):
   '''
      This function can read text in a file.

      Arguments:
         1 ~ name - In this argument you will put the name of the file you want to read.
         2 ~ ret - If you want the function returns what is in the text, use 'True'.

      Returns:
         - ret ~ By default if False, but if want you can use 'True' to return the text of the file.
   '''

   try:
      f = open(name, "r")
      
      for line in f:
         print(f"{line}".capitalize())
         if ret == True:
            return line

      f.close()

   except:
      print("Ocorreu um erro, tente novamente mais tarde!")


if fileExists(file_name) == False:
   createFile(file_name)

while True:
   os.system("clear")
   print("[1] Ver filmes cadastrados")
   print("[2] Pesquisar filmes (Não programado ainda!)")
   print("[3] Cadastrar filme")
   print("[0] Sair")

   Choose = int(input("Digite o número da sua escolha: "))

   if Choose == 0:
      print("Até mais!")
      break

   if Choose == 1:
      print()
      print("Nome  \t  Ano \t  Gênero")
      readFile(file_name)
      print()
      input("Aperte ENTER para retornar")
      os.system("clear")

   if Choose == 2:
      print("Pesquisar por:")
      print("[1] Nome")
      print("[2] Gênero")
      print("[3] Ano de lançamento")

      option = int(input("Sua escolha: "))

      if option == 1:
         look = str(input("Nome do filme: ")).upper()
         search.searchName(look)
         
         input("Pressione ENTER para continuar...")
      
      elif option == 2:
         look = str(input("Gênero do filme: "))
         #search.searchName(look)

         input("Pressione ENTER para continuar...")

      elif option == 3: 
         look = int(input("Ano de lançamento do filme: "))
         #search.search(look)

         input("Pressione ENTER para continuar...")

   if Choose == 3:
      os.system("clear")
      movie = input("Digite o nome do filme: ").strip()
      year = input("Digite o ano do filme: ").strip()
      gen = input("Digite o gênero do filme: ").strip()

      infos = [movie, year, gen]

      #print(infos)
      #print(infos[0])

      a = 0
      while a < 3:
         #Escreve tudo em maiúsculo para facilitar a busca
         writeFile(file_name, f'{infos[a].upper()}, ')
         a += 1

      #switch to writeFile(file_name, " ") this way is better for the program show the results with [0], for example.
      writeFile(file_name, "\n")

      print("Filme cadastrado com sucesso!")
      input("Aperte ENTER para continuar")
      os.system("clear")
   
