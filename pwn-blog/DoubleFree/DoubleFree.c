#include <stdlib.h>

int main(void)
{
    /* 1. Erstes malloc – Chunk landet später in tcache[8] */
    char *a = malloc(8);

    /* 2. Erster free:  a  ➜  tcache[8]->next = NULL */
    free(a);

    /* 3. Zweiter free auf dieselbe Adresse:  a taucht ZWEI Mal in der Liste auf.
          Jetzt zeigt der 'next'‑Pointer von a auf sich selbst – frei kontrollierbar
          via Use‑After‑Free‑Write. */
    free(a);

    /* 4. Nächstes malloc(8) gibt den manipulierten Pointer zurück.
          Angreifer kann ihn vorher auf GOT‑Eintrag / beliebige Adresse umlenken,
          dann beliebige 8 Byte schreiben. */
    malloc(8);

    /* 5. Seit glibc 2.34 greifen per‑Thread‑Tcache‑Mitigations:
          Doppel‑Free wird detektiert und Programm terminiert.  */
}