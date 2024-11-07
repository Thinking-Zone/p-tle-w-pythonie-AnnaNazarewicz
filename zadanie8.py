nie_odpowiedzi = 0  

while True:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").lower()  
    
    if odpowiedz == "nie":
        nie_odpowiedzi += 1 
    elif odpowiedz == "tak":
        print(f"Liczba odpowiedzi 'nie': {nie_odpowiedzi}")
        break 
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.") 
    else:
        print("Proszę wpisać 'tak', 'nie' lub 'nie wiem'.")  
