import fam  # importuje prywatny moduł fam (tam zapisane funkcje i listy)
print("\nWelcome to \"Task To Do Management Program\"\n")
kontynuacja = "Y"
while kontynuacja == "Y":    
    menu_items = ["list", "add", "mark", "archive"]         # implementacja wyboru - element menu
    answer = input("\nPlease specify a command [list, add, mark, archive]: ")  # wprowadzanie wyboru z klawiatury

    if(answer == menu_items[0]):    # list
        fam.get_items()                 # zapisuje rekordy z pliku do listy
        fam.print_items()               # wyświetla rekordy na ekranie
        fam.clearence()                 # zeruje listy operacujne przed kolejnym menu            

    elif(answer == menu_items[1]):  # add
        fam.get_items()                 # zapisuje rekordy z pliku do listy
        fam.print_items()               # wyświetla rekordy na ekranie
        fam.add_item()                  # dadaje rekordy do listy w pętli i zapisuje do pliku
        fam.clearence()                  

    elif(answer == menu_items[2]):  # mark
        fam.get_items()                 # zapisuje rekordy z pliku do listy
        fam.print_items()               # wyświetla rekordy na ekranie
        fam.mark_item()                 # zaznacza x zadania zrealizowane w liście i zapisuje do pliku
        fam.clearence()                 

    elif(answer == menu_items[3]):  # archive
        fam.get_items()                 # zapisuje rekordy z pliku do listy
        fam.print_items()               # delete rekordy oznaczone "x"-em z listy i zapisuje do listy to_archive
        fam.archive_items()
        fam.clearence()             
                                        
    kontynuacja = input('Do you want to continue? (Y/N):')
    kontynuacja = kontynuacja.upper()
print("To the next time")