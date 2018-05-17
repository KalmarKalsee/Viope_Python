def main():

   while True:

    userinput = input("Anna syöte (Lopeta lopettaa): ")
    if userinput == "Lopeta":
        break

    else:
        tester(userinput)

def tester(givenstring="Oletustulostus"):
    if(len(givenstring) < 5):
        print("Oletustulostus")
    else:
        print(givenstring)

if __name__ == "__main__":
	main()