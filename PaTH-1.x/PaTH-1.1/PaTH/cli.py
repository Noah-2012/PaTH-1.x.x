import os
from rich import print

def main():
    current_directory = os.getcwd()
    print(f"{current_directory}/")
    print_tree(current_directory)

def print_tree(directory, prefix=''):
    # Liste alle Dateien und Ordner im aktuellen Verzeichnis
    try:
        entries = os.listdir(directory)
    except PermissionError:
        print(f"{prefix}Zugriff verweigert: {directory}")
        return

    # Sortiere Einträge nach Ordnern und Dateien
    entries.sort()

    # Durchlaufe alle Einträge und gib die Struktur aus
    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        
        # Bestimme das aktuelle Symbol, je nachdem, ob es der letzte Eintrag ist
        if index == len(entries) - 1:
            connector = '└── '
            new_prefix = prefix + '    '
        else:
            connector = '├── '
            new_prefix = prefix + '│   '

        if os.path.isdir(path):  # Wenn es ein Ordner ist
            print(f"{prefix}{connector}{entry}/")
            # Rekursiv aufrufen, um den Inhalt des Ordners anzuzeigen
            print_tree(path, new_prefix)
        else:  # Wenn es eine Datei ist
            if os.path.splitext(entry)[1] in ('.py', '.cc', '.cpp', '.c', '.r', '.sh', '.txt'):
                print(f"{prefix}{connector}[yellow]{entry}[/yellow]")

# Das Skript im aktuellen Verzeichnis starten
if __name__ == "__main__":
    main()

