"""
Analizzatore di Spese JSON 
Questo è un commento nuovo. Cosa succede sul fork?
Requisiti da completare:
1. Verificare che il file JSON esiste usando pathlib.
2. Caricare i dati dal file JSON.
3. Calcolare il totale delle spese e raggrupparle per categoria usando un dizionario.

BUG ALERT: Ci sono 2 bug nascosti nel codice... Trovali e correggili!
"""
import json
import sys
from pathlib import Path

def carica_spese(percorso_file: Path) -> list:
    """
    Legge il file JSON e restituisce la lista delle spese.
    """
    # TO-DO: Usare il metodo .exists() di pathlib per verificare se il file esiste.
    # Se il file NON esiste, stampare un errore e terminare il programma con sys.exit(1).
    if not percorso_file.exists():
        print("Percorso inserito non valido.... terminando programma...")
        sys.exit()


    # BUG 1: C'è un errore nella modalità di apertura del file per la lettura di un JSON
    with open(percorso_file, 'r', encoding='utf-8') as f:
        dati = json.load(f)
    
    return dati

def analizza_spese(lista_spese: list):
    """
    Riceve la lista delle spese, calcola il totale generale 
    e raggruppa i costi per categoria.
    """
    totale_generale = 0.0
    spese_per_categoria = {}  # Dizionario che conterrà: { "Categoria": Somma_Importi }

    for spesa in lista_spese:
        # Ogni 'spesa' è un dizionario, es: {"categoria": "Cibo", "importo": 45.50}
        categoria = spesa["categoria"]
        importo = spesa["importo"]
        
        # Calcoliamo il totale generale
        totale_generale += importo
        
        # Raggruppamento nel dizionario
        if categoria in spese_per_categoria:
            spese_per_categoria[categoria] += importo
        else:
            spese_per_categoria[categoria] = importo


    print(spese_per_categoria)
    # Stampa dei risultati
    print(f"\n--- RISULTATI ANALISI ---")
    print(f"Spesa Totale Generale: €{totale_generale:.2f}")
    print("Spese per Categoria:")
    
    # BUG 2: C'è un errore di sintassi/metodo nell'iterazione del dizionario per stampare chiave e valore.
    for cat, tot in spese_per_categoria.items():
        print(f" - {cat}: €{tot:.2f}")

def main():
    """
    Funzione principale.
    Uso previsto da terminale: python analizzatore.py spese.json
    """
    # Controllo che sia stato passato l'argomento del file
    if len(sys.argv) < 2:
        print("Errore: Specifica il file JSON delle spese!")
        print("Uso: python python_progetto_1.py <nome_file.json>")
        sys.exit(1)
        
    # Prendiamo il nome del file dagli argomenti di sys
    nome_file = sys.argv[1]
    percorso_json = Path(nome_file)
    
    print(f"Lettura del file: {percorso_json.name}...")
    
    # Esecuzione del programma
    dati_spese = carica_spese(percorso_json)
    analizza_spese(dati_spese)

if __name__ == "__main__":
    main()
