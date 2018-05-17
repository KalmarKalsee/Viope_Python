def main():

    luku = int(input("Anna lukuarvo: "))
    
    def potenssi(luku):
        luku2 = luku**2
        print("Toinen potenssi on",luku2)
    
    potenssi(luku)

if __name__ == "__main__":
    main()