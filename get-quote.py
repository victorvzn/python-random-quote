import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines() 
  f.close()
  
  last = len(quotes) - 1

  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last) 

  print("RANDOM QUOTE: ", quotes[rnd1], end="")
  print("RANDOM QUOTE: ", quotes[rnd2], end="")

  new_quote = input("Enter a new quote: ") 

  f = open("quotes.txt", "a")
  f.write("\n")
  f.write(new_quote)
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close

  last = len(quotes) - 1

  print()
  print("NEW QUOTE:", quotes[last], end="")

if __name__== "__main__":
  primary()
