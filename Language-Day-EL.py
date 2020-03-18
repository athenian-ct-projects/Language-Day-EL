# DO NOT RUN THIS CELL WHILE PLAYING GAME (IT RESETS PROGRESS)
# This sets list to nothing at start of game
fs=[]

# Vowel function:
# Checks if the input (that is a noun) starts with a vowel and inserts a or an
# depending on what it starts with. It also adds the input to the end of the 
# list (fs).

def vowel():
  if x[0] in "aeiouAEIOU":
    va=("an " + x)
  else:
    va=("a "+ x)
  fs.append(va)
  
# Spanish el/la function
# Checks if the input (that is a noun) ends with a, and inserts la or el
# depending on what the noun ends with. It also adds the input to the end of the list (fs).

def span():
  if x.endswith("a"):
    vs=("la " + x)
  else:
    vs=("el " +x)
  fs.append(vs)

# Spanish los/las function
# Checks if the input (that is a plural noun) ends with as, and inserts las or 
# los depending on what the noun ends with. It also adds the input to the end of the list (fs).

def spanp():
  if x.endswith("as"):
    vs=("las " + x)
  else:
    vs=("los " +x)
  fs.append(vs)

# Spanish un/una function
# Checks if the input (that is a noun) ends with an a, and inserts una or un
# depending on what the noun ends with. It also adds the input to the end of the list (fs).

def span1():
  if x.endswith("a"):
    v1=("una " + x)
  else:
    v1=("un " +x)
  fs.append(v1)
  
# Intro/Instructions code:
# Code prints the instructions
# Input, start, checks if the player has run the first four cells.
start=input("STOP! Before you start, run the previous four cells before starting."
"If you have type ok to start instructions, type help if you haven't: ")
if start==("ok"):
  print("Instrucciones para Mad Libs: ")
  print("Escribe en el blanco con el parte del discurso: ")
  print("Ex. Escribe un sustantivo: 'banana'")
  print("En elf fín, va a imprimir tu cuenta: ")
  print("Ex. Snow White estaba envenenada de una banana")
  print("At the end your story will printed with your inputs. Also, do not run"
  " the very first cell while playing. ")
elif start==("help"):
  print("Run the past four cells (10-13). There will be no inputs of prints from "
  "running these cells. Once you have, restart this cell.")

# example: Try one!
# Prints an example: prints instructions, then prints an input asking for a noun
print("¡Ahora prueba uno!")
y=input("Escribe un sustantivo: ")


# SKIP THIS CELL FOR NOW
# Pick a language code: (only have one language done)
# Function:
  # Input that asks for a language, if the input is english then it will start
  # in English, if not it will start in Spanish. If the input is neither then
  # it will ask you to try again.
def langpick():
  lang=input("Pick a language: English or Spanish ")
  if (lang=="English" or lang=="english"):
    print("Ok let's start our story in English.")
  elif (lang=="Spanish" or lang=="spanish"):
    print("Ok let's start our story in Spanish.")
  else:
    print("Try again.")
    langpick()
  return(lang)

language=langpick()

# The following cells (8-19), asks for inputs for the game. Each one asks for
# a noun, plural noun, verb, adjective, or emotion. Some will be specific to 
# feminine or masculine.
# 0
x=input("Excribe un nombre: ")
fs.append(x)

#1
x=input("Excribe un sustantivo: ")
span1()

#2
x=input("Escribe un numero: ")
fs.append(x)

#3
x=input("Escribe una adjetiva femenina: ")
fs.append(x)

#4
x=input("Escribe dos adjectivas femeninas (ex. linda y bonita): ")
fs.append(x)

#5
x=input("Escribe un sunstantivo plural: ")
spanp()

#6
x=input("Escribe un numero: ")
fs.append(x)

#7
x=input("Escribe una adjetiva femenina: ")
fs.append(x)

#8
x=input("Escribe un sustantivo: ")
fs.append(x)

#9
x=input("Escribe un adjetivo masculino: ")
fs.append(x)

# This cell has two inputs on the end of the list, fs, because it is used twice
# in the story with different preceeding words. (The first one only adds the 
# input. The second one uses the spanish plural function so los or las will 
# preceed the word.)

#10
x=input("Escribe un sustantivo plural: ")
fs.append(x)
#11
spanp()

#12
x=input("Escribe un sustantivo: ")
span1()
#13
fs.append(x)

#14
x=input("Escribe un sustantivo: ")
fs.append(x)

#15
x=input("Escribe una adjetiva feminina: ")
fs.append(x)

# This cell checks if the input is a verb. It checks if the input ends with
# -ar, -er, or -ir. If it doesn't it will ask you to try it again.

#16
x=input("Escribe un infinitivo: ")
while not x.endswith("ir") and x.endswith("ar") and x.endswith("er"):
  x=input("Trata otra vez. Escribe un infinitivo: ")

fs.append(x)

#17
x=input("Escribe una emoción masculino: ")
fs.append(x)

#18
x=input("Escribe un sustantivo plural: ")
spanp()

#19
x=input("Escribe un sustantivo: ")
span1()

# Prints out your inputs from the previous cells.

print("Here are your inputs: ")
for y in fs:
  print(y)
  
# The next cells (30-39), print out the finished story using the inputs. It uses
# each input in the list, fs, by calling fs[number input is in the list].

print("Había una vez, había una chica se llama "+fs[0]+". Su madre se murió" 
      " cuando la chica era muy pequeña. Ella sólo tenía su padre y "+fs[1]+
      " para compañía. Ahora ella tenía "+fs[2]+" hermanastras. Ellas eran" 
      " maliciosas y eran las hijas de la nueva esposa de su padre."
      "La "+fs[3]+" madrastra de la chica no le gustaba a ella. "
      +fs[0]+" se convirtió una servidora para las hermanastras."
      " Ellas empezaban a llamarla Cenicienta porque ella sentaba en cenizas. "
      +fs[0]+" era "+fs[4]+" y simpática, entonces todos les gustaban a ella "
      "excepto su hermanastras.")

print("Cuando Cenicienta tenía 17 años, el rey tenía un baile donde " 
      +fs[5]+" y las chicas en la ciudad estaban invitadas. Cenicienta" 
      " empezaron a ella a vestirlas, pero ellas no pudieron permitir a ella si ir al"
      " baile. Cuando las hermanastras salieron, Cenicienta lloró por "
      +fs[6]+" horas.")

print("Pero una misteriosa y "+fs[7]+" voz llamó a Cenicienta. ¡Era su hada madrina! "
      "Ella dijo a Cenicienta, 'No llores no más " +fs[0]+ ". Vas a ir al baile "
      "porque eres " +fs[4]+ ". Trae una calabaza a mi.' Ella la trató y su "
      "hada madrina la tocó con su "+fs[8]+".")
      
print("La calabaza transformó en un "+fs[9]+" coche. La hada madrina pidió "
      +fs[10]+" y Cenicienta obedeció. También " 
      +fs[11]+" transformaron en lacayos. Ahora la hada madrina tocó la ropa "
      "de la chica y transformó en "+fs[12]+".")
      
print("Cenicienta tenía zapatos de "+fs[14]+" y se miró muy linda. “Ahora puedes "
      "ir al baile,' la hada madrina dijo, 'pero necesitas salir antes de "
      "medianoche. A la medianoche, tu "+fs[12]+" va a transformó en harapos."
      " Cenicienta dijo gracias y salió. Cuando llegó al castillo, todos"
      " miraban a ella y el príncipe le pedí que bailar consigo.")

print("Cuando sus hermanastras llegaron a la casa donde Cenicienta estaba, "
"ellas hablaban de una princesa elegante y "+fs[15]+". El príncipe quería hablar "
"con la princesa otra vez y tenía otro baile. Las hermanastras de Cenicienta "
"salieron para el baile y su hada madrina apareció otra vez con el coche, "
"lacayos, "+fs[13]+", y zapatos.")

print("Otra vez ella bailaba con el príncipe y salió antes de la medianoche. "
"Otra vez el príncipe quería bailar y "+fs[16]+" con la princesa, entonces tenía "
"otro baile.")

print("Este tiempo, el príncipe no la dejaría, pero al doce menos cinco, "
"ella corrió y dejó un zapato. El príncipe fue "+fs[17]+" y sorprendido.")

print("Él buscó ella todo el próximo día y quería casar ella. Todas "
+fs[18]+" y las mujeres trataban de llevar el zapato.")

print("Cuando Cenicienta llevó el zapato, sus hermanastras se rían a ella, "
"pero lo cupe Cenicienta. Ella sacó el otro zapato y "+fs[19]+". Ellos "
"casaron y vivieron felices para siempre.")

print("Thanks for playing!")

