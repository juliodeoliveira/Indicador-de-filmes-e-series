def readFile(name):

   try:
      f = open(name, "r")
      l = []

      for line in f:
         #print(f"{line}")
         l.append(line)
      return l
        

      f.close()


   except:
      print("Ocorreu um erro, tente novamente mais tarde!")


var = readFile("Indicador-de-filmes-e-series/Save.txt")

def searchName(item):
   '''
      The parameter 'item' need to be in uppercase!
   '''
   
   i = 0
   while i < len(var):
      if item in var[i]:
         print("ACHADO - ",var[i])
      i += 1

def searchGender(item):
   '''
      The parameter 'item' need to be in uppercase!
   '''

   i = 0
   while i < len(var):
      if item in var[i]:
         print("Encontrado por genero: ", var[i])
      i += 1
   
def searchYear(item):
   '''
      The parameter 'item' need to be in uppercase!
   '''

   i = 0
   while i < len(var):
      if item in var[i]:
         print("Encontrado por ano: ", var[i])
      i += 1