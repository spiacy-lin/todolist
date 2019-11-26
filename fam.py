list_todo = []                  # deklaracja listy zadań
to_archive = []                 # deklaracja listy zadań zrealizowanych


def get_items():
    with open('mytodo.txt') as file:
        for line in file:
            line = line.strip()   
            list_todo.append(line)
        return list_todo


def print_items():
    i = 1
    rozmiar = len(list_todo)
    if rozmiar < 1:
        print("\nThere is no tasks to do. Have a break ... or\n")
    else:
        print('')
        for item in list_todo:
            print(str(i) + '.', item)
            i += 1
        print('')


def print_arch():
    i = 1
    print('')
    for item in to_archive:
        print(str(i) + '.', item)
        i += 1
    print('')


def write_todo():
    with open('mytodo.txt', 'w') as file1:
        file1.writelines("%s\n" % item for item in list_todo)


def write_arch():
    with open('mytodoarch.txt', 'a') as file2:
        file2.writelines("%s\n" % item for item in to_archive)


def add_item():
    end_while = 'Y'
    while end_while == 'Y':
        wsad = input("Add new task: ")
        wsad = '[ ] ' + wsad
        list_todo.append(wsad)
        print_items()
        end_while = input('Want introduce the next task? (Y/N): ')
        end_while = end_while.upper()
    write_todo()


def mark_item():
    end_while = 'Y'
    while end_while == 'Y':
        try:
            wsad = int(input("Input number of task to be archived: "))
        except ValueError:
            print('Ups, it is not a number')
        maks = len(list_todo)
        if wsad > maks:
            print('There is no such task!!!. TRy again')
        else:
            current = list_todo[wsad - 1]
            current = current.replace('[ ]', '[x]')
            list_todo[wsad - 1] = current
        print_items()
        end_while = input('Want mark the next task? (Y/N): ')
        end_while = end_while.upper()
    write_todo()


def archive_items():
    wsad = input("Do you want to archive complited tasks? (Y/N): ")
    wsad = wsad.upper()
    if wsad == 'Y':
        for item in list_todo:
            if item[1] == 'x':
                to_archive.append(item)
                iterator = list_todo.index(item)
                list_todo.pop(iterator)
    print("\nComplited tasks in archive: ")
    print_arch()
    write_arch()
    print("\nTasks to do: ")
    print_items()
    write_todo()


def clearence():
    to_archive.clear()
    list_todo.clear()