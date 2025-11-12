# Inventory_system
Inventory Management System in Python using SQLite. A terminal-based application to manage clothing and footwear stock, track sizes, search products, and generate auto-replenishment lists. Designed for learning and practical inventory management experience.
Inventory Management System - Python

Acesta este un *sistem de inventar* dezvoltat în Python pentru gestionarea produselor de tip *haine și încălțăminte*.
Proiectul utilizează *SQLite* pentru stocarea datelor și oferă un meniu interactiv în terminal pentru a căuta produse, vizualiza stocurile pe dimensiuni și genera liste de auto-replenishment.

Funcționalități principale

- Crearea și configurarea bazei de date stockroom.db.
- Adăugarea de produse în baza de date (haine, încălțăminte femei și bărbați).
- Vizualizarea stocurilor pe dimensiuni pentru *backroom* și *salesfloor*.
- Căutarea produselor după cod.
- Generarea unei liste de auto-replenishment pentru stocuri scăzute.
- Meniu interactiv în terminal cu opțiuni pentru utilizator.

Cerințe

- Python 3.x
- Biblioteca standard sqlite3 (inclusă în Python)
- (Opțional) alte librării standard precum random

Cum se rulează

1. Clonează repository-ul sau descarcă fișierul app.py.
2. Deschide terminalul și rulează:
   ```bash
   python app.py

3. Vei vedea un meniu interactiv în terminal. Urmează instrucțiunile pentru a naviga printre opțiuni.



Structura bazei de date

products – Informații generale despre produs (cod, nume, preț, material, culoare, categorie, stoc backroom și salesfloor)

clothing_sizes_backroom / clothing_sizes_salesfloor – Stoc pe mărimi pentru haine

women_shoes_sizes_backroom / women_shoes_sizes_salesfloor – Stoc pe mărimi pentru încălțăminte femei

men_shoes_sizes_backroom / men_shoes_sizes_salesfloor – Stoc pe mărimi pentru încălțăminte bărbați
