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



def searchName(item):
   
   var = readFile("Indicador-de-filmes-e-series/Save.txt")

   #Now I need the code to run over the list an see wich index is the result of the search
   i = 0
   while i < len(var):
      if item in var[i]:
         print("ACHADO - ",var[i])
      i += 1

   # DEBUG ONLY!
   #print("\n")
   #print(30*"--")
   #print("1: tudo lá do Save.txt", end=" - ")
   #print(var)
   #print("2: O que vc pesquisou",user, "\n")
   #print("3: resultado da busca",result, "\n")
  # print("4: todos os nomes do Save.txt divididos",divide, "\n")


#Argument need to be in uppercase
#search("ERA DO GELO")




