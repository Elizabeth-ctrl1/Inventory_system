import random
import sqlite3

def item(code, name, price, material, color, maxshoestander, maxtype1, maxtype2, maxtype3):
    return {
        "code": code,
        "name": name,
        "price": price,
        "material": material,
        "color": color,
        "maxshoestander": maxshoestander,
        "maxtype1": maxtype1,
        "maxtype2": maxtype2,
        "maxtype3": maxtype3,
    }


def size_on_stock_backroom():
    return {
        "xs": random.randint(5, 15),
        "s": random.randint(8, 20),
        "m": random.randint(10, 25),
        "l": random.randint(8, 20),
        "xl": random.randint(5, 15),
    }


def size_on_stock_salesfloor():
    return {
        "xs": random.randint(1, 5),
        "s": random.randint(2, 8),
        "m": random.randint(3, 10),
        "l": random.randint(2, 8),
        "xl": random.randint(1, 5),
    }


def f_shoes_size_backroom():
    return {
        "s35": random.randint(5, 15),
        "s36": random.randint(8, 20),
        "s37": random.randint(10, 25),
        "s38": random.randint(8, 20),
        "s39": random.randint(5, 15),
        "s40": random.randint(5, 15),
        "s41": random.randint(3, 10),
    }


def f_shoes_size_salesfloor():
    return {
        "s35": random.randint(1, 5),
        "s36": random.randint(2, 8),
        "s37": random.randint(3, 10),
        "s38": random.randint(2, 8),
        "s39": random.randint(1, 5),
        "s40": random.randint(1, 5),
        "s41": random.randint(1, 3),
    }


def m_shoes_size_backroom():
    return {
        "s40": random.randint(5, 15),
        "s41": random.randint(8, 20),
        "s42": random.randint(10, 25),
        "s43": random.randint(8, 20),
        "s44": random.randint(5, 15),
        "s45": random.randint(5, 15),
        "s46": random.randint(8, 20),
        "s47": random.randint(3, 10),
        "s48": random.randint(3, 10),
        "s49": random.randint(2, 8),
    }


def m_shoes_size_salesfloor():
    return {
        "s40": random.randint(1, 5),
        "s41": random.randint(2, 8),
        "s42": random.randint(3, 10),
        "s43": random.randint(2, 8),
        "s44": random.randint(1, 5),
        "s45": random.randint(1, 5),
        "s46": random.randint(2, 8),
        "s47": random.randint(1, 3),
        "s48": random.randint(1, 3),
        "s49": random.randint(1, 2),
    }


def setup_database():
    conn = sqlite3.connect('stockroom.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS products
                   (
                       code
                       TEXT
                       PRIMARY
                       KEY,
                       name
                       TEXT
                       NOT
                       NULL,
                       price
                       REAL
                       NOT
                       NULL,
                       material
                       TEXT,
                       color
                       TEXT,
                       category
                       TEXT
                       NOT
                       NULL,
                       maxshoestander
                       INTEGER,
                       maxtype1
                       INTEGER,
                       maxtype2
                       INTEGER,
                       maxtype3
                       INTEGER,
                       stockroom
                       TEXT,
                       salesfloor
                       TEXT
                   )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS clothing_sizes_backroom
                   (
                       product_code
                       TEXT
                       PRIMARY
                       KEY,
                       xs
                       INTEGER,
                       s
                       INTEGER,
                       m
                       INTEGER,
                       l
                       INTEGER,
                       xl
                       INTEGER,
                       FOREIGN
                       KEY
                   (
                       product_code
                   ) REFERENCES products
                   (
                       code
                   )
                       )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS clothing_sizes_salesfloor
                   (
                       product_code
                       TEXT
                       PRIMARY
                       KEY,
                       xs
                       INTEGER,
                       s
                       INTEGER,
                       m
                       INTEGER,
                       l
                       INTEGER,
                       xl
                       INTEGER,
                       FOREIGN
                       KEY
                   (
                       product_code
                   ) REFERENCES products
                   (
                       code
                   )
                       )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS women_shoes_sizes_backroom
                   (
                       product_code
                       TEXT
                       PRIMARY
                       KEY,
                       size_35
                       INTEGER,
                       size_36
                       INTEGER,
                       size_37
                       INTEGER,
                       size_38
                       INTEGER,
                       size_39
                       INTEGER,
                       size_40
                       INTEGER,
                       size_41
                       INTEGER,
                       FOREIGN
                       KEY
                   (
                       product_code
                   ) REFERENCES products
                   (
                       code
                   )
                       )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS women_shoes_sizes_salesfloor
                   (
                       product_code
                       TEXT
                       PRIMARY
                       KEY,
                       size_35
                       INTEGER,
                       size_36
                       INTEGER,
                       size_37
                       INTEGER,
                       size_38
                       INTEGER,
                       size_39
                       INTEGER,
                       size_40
                       INTEGER,
                       size_41
                       INTEGER,
                       FOREIGN
                       KEY
                   (
                       product_code
                   ) REFERENCES products
                   (
                       code
                   )
                       )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS men_shoes_sizes_backroom
                   (
                       product_code
                       TEXT
                       PRIMARY
                       KEY,
                       size_40
                       INTEGER,
                       size_41
                       INTEGER,
                       size_42
                       INTEGER,
                       size_43
                       INTEGER,
                       size_44
                       INTEGER,
                       size_45
                       INTEGER,
                       size_46
                       INTEGER,
                       size_47
                       INTEGER,
                       size_48
                       INTEGER,
                       size_49
                       INTEGER,
                       FOREIGN
                       KEY
                   (
                       product_code
                   ) REFERENCES products
                   (
                       code
                   )
                       )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS men_shoes_sizes_salesfloor
                   (
                       product_code
                       TEXT
                       PRIMARY
                       KEY,
                       size_40
                       INTEGER,
                       size_41
                       INTEGER,
                       size_42
                       INTEGER,
                       size_43
                       INTEGER,
                       size_44
                       INTEGER,
                       size_45
                       INTEGER,
                       size_46
                       INTEGER,
                       size_47
                       INTEGER,
                       size_48
                       INTEGER,
                       size_49
                       INTEGER,
                       FOREIGN
                       KEY
                   (
                       product_code
                   ) REFERENCES products
                   (
                       code
                   )
                       )
                   ''')

    conn.commit()
    conn.close()
    print("Database created!")


def save_product(product, category, stockroom_location, salesfloor_location):
    conn = sqlite3.connect('stockroom.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT OR REPLACE INTO products 
    (code, name, price, material, color, category, maxshoestander, maxtype1, maxtype2, maxtype3, stockroom, salesfloor)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        product["code"],
        product["name"],
        product["price"],
        product["material"],
        product["color"],
        category,
        product["maxshoestander"],
        product["maxtype1"],
        product["maxtype2"],
        product["maxtype3"],
        stockroom_location,
        salesfloor_location
    ))

    if category == "clothing":
        sizes_back = product["sizes_backroom"]
        cursor.execute('''
        INSERT OR REPLACE INTO clothing_sizes_backroom 
        (product_code, xs, s, m, l, xl)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (product["code"], sizes_back["xs"], sizes_back["s"], sizes_back["m"], sizes_back["l"], sizes_back["xl"]))

        sizes_floor = product["sizes_salesfloor"]
        cursor.execute('''
        INSERT OR REPLACE INTO clothing_sizes_salesfloor 
        (product_code, xs, s, m, l, xl)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (product["code"], sizes_floor["xs"], sizes_floor["s"], sizes_floor["m"], sizes_floor["l"],
              sizes_floor["xl"]))

    elif category == "women_shoes":
        sizes_back = product["sizes_backroom"]
        cursor.execute('''
        INSERT OR REPLACE INTO women_shoes_sizes_backroom 
        (product_code, size_35, size_36, size_37, size_38, size_39, size_40, size_41)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (product["code"], sizes_back["s35"], sizes_back["s36"], sizes_back["s37"], sizes_back["s38"],
              sizes_back["s39"], sizes_back["s40"], sizes_back["s41"]))

        sizes_floor = product["sizes_salesfloor"]
        cursor.execute('''
        INSERT OR REPLACE INTO women_shoes_sizes_salesfloor 
        (product_code, size_35, size_36, size_37, size_38, size_39, size_40, size_41)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (product["code"], sizes_floor["s35"], sizes_floor["s36"], sizes_floor["s37"], sizes_floor["s38"],
              sizes_floor["s39"], sizes_floor["s40"], sizes_floor["s41"]))

    elif category == "men_shoes":
        sizes_back = product["sizes_backroom"]
        cursor.execute('''
        INSERT OR REPLACE INTO men_shoes_sizes_backroom 
        (product_code, size_40, size_41, size_42, size_43, size_44, size_45, size_46, size_47, size_48, size_49)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (product["code"], sizes_back["s40"], sizes_back["s41"], sizes_back["s42"], sizes_back["s43"],
              sizes_back["s44"], sizes_back["s45"], sizes_back["s46"], sizes_back["s47"], sizes_back["s48"],
              sizes_back["s49"]))

        sizes_floor = product["sizes_salesfloor"]
        cursor.execute('''
        INSERT OR REPLACE INTO men_shoes_sizes_salesfloor 
        (product_code, size_40, size_41, size_42, size_43, size_44, size_45, size_46, size_47, size_48, size_49)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (product["code"], sizes_floor["s40"], sizes_floor["s41"], sizes_floor["s42"], sizes_floor["s43"],
              sizes_floor["s44"], sizes_floor["s45"], sizes_floor["s46"], sizes_floor["s47"], sizes_floor["s48"],
              sizes_floor["s49"]))

    conn.commit()
    conn.close()


def search_product(product_code):
    conn = sqlite3.connect('stockroom.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE code = ?', (product_code,))
    product = cursor.fetchone()

    if not product:
        conn.close()
        return None

    result = {
        "code": product[0],
        "name": product[1],
        "price": product[2],
        "material": product[3],
        "color": product[4],
        "category": product[5],
        "stockroom": product[10],
        "salesfloor": product[11]
    }

    if product[5] == "clothing":
        cursor.execute('SELECT xs,s,m,l,xl FROM clothing_sizes_backroom WHERE product_code=?', (product_code,))
        back = cursor.fetchone()
        result["sizes_backroom"] = {"xs": back[0], "s": back[1], "m": back[2], "l": back[3], "xl": back[4]}

        cursor.execute('SELECT xs,s,m,l,xl FROM clothing_sizes_salesfloor WHERE product_code=?', (product_code,))
        floor = cursor.fetchone()
        result["sizes_salesfloor"] = {"xs": floor[0], "s": floor[1], "m": floor[2], "l": floor[3], "xl": floor[4]}

    elif product[5] == "women_shoes":
        cursor.execute(
            'SELECT size_35,size_36,size_37,size_38,size_39,size_40,size_41 FROM women_shoes_sizes_backroom WHERE product_code=?',
            (product_code,))
        back = cursor.fetchone()
        result["sizes_backroom"] = {"35": back[0], "36": back[1], "37": back[2], "38": back[3], "39": back[4],
                                    "40": back[5], "41": back[6]}

        cursor.execute(
            'SELECT size_35,size_36,size_37,size_38,size_39,size_40,size_41 FROM women_shoes_sizes_salesfloor WHERE product_code=?',
            (product_code,))
        floor = cursor.fetchone()
        result["sizes_salesfloor"] = {"35": floor[0], "36": floor[1], "37": floor[2], "38": floor[3], "39": floor[4],
                                      "40": floor[5], "41": floor[6]}

    elif product[5] == "men_shoes":
        cursor.execute(
            'SELECT size_40,size_41,size_42,size_43,size_44,size_45,size_46,size_47,size_48,size_49 FROM men_shoes_sizes_backroom WHERE product_code=?',
            (product_code,))
        back = cursor.fetchone()
        result["sizes_backroom"] = {"40": back[0], "41": back[1], "42": back[2], "43": back[3], "44": back[4],
                                    "45": back[5], "46": back[6], "47": back[7], "48": back[8], "49": back[9]}

        cursor.execute(
            'SELECT size_40,size_41,size_42,size_43,size_44,size_45,size_46,size_47,size_48,size_49 FROM men_shoes_sizes_salesfloor WHERE product_code=?',
            (product_code,))
        floor = cursor.fetchone()
        result["sizes_salesfloor"] = {"40": floor[0], "41": floor[1], "42": floor[2], "43": floor[3], "44": floor[4],
                                      "45": floor[5], "46": floor[6], "47": floor[7], "48": floor[8], "49": floor[9]}

    conn.close()
    return result


def return_to_menu():
    response = input("\nDo you wish to go back to the menu? (yes/no): ").strip().lower()
    return response in ['yes', 'y', 'da']


def main_menu():
    while True:
        print("\n" + "=" * 50)
        option_a = "A. Look up a product"
        option_b = "B. Backroom info"
        option_c = "C. Sales floor information"
        option_d = "D. Auto-replenishment list"
        option_e = "E. Exit"

        action = input(f"Hello. What can I help with today?\n"
                       f"{option_a}\n"
                       f"{option_b}\n"
                       f"{option_c}\n"
                       f"{option_d}\n"
                       f"{option_e}\n").strip().upper()

        if action == "A":
            product_code = input("Please specify the code of the product: \n").strip().upper()
            found = search_product(product_code)
            if found:
                print("\n    PRODUCT INFORMATION    ")
                print(f"Code: {found['code']}")
                print(f"Name: {found['name']}")
                print(f"Price: ${found['price']}")
                print(f"Material: {found['material']}")
                print(f"Color: {found['color']}")
                print(f"Backroom Location: {found['stockroom']}")
                print(f"Sales Floor Stander: {found['salesfloor']}")

                print("\n    BACKROOM STOCK    ")
                total_backroom = sum(found["sizes_backroom"].values())
                for size, qty in found["sizes_backroom"].items():
                    print(f"Size {size}: {qty}")
                print(f"Total Backroom: {total_backroom}")

                print("\n    SALES FLOOR STOCK    ")
                total_salesfloor = sum(found["sizes_salesfloor"].values())
                for size, qty in found["sizes_salesfloor"].items():
                    print(f"Size {size}: {qty}")
                print(f"Total Sales Floor: {total_salesfloor}")

                total_stock = total_backroom + total_salesfloor
                print(f"\nTOTAL STOCK (Backroom + Sales Floor): {total_stock}")
            else:
                print("Product not found. Check the code and try again.")

            if not return_to_menu():
                print("Thank you for using the inventory system. Goodbye!")
                break

        elif action == "B":
            bin_code = input("Please specify bin code: \n").strip().upper()
            conn = sqlite3.connect('stockroom.db')
            cursor = conn.cursor()
            cursor.execute('SELECT code, name, category FROM products WHERE stockroom = ?', (bin_code,))
            products_in_bin = cursor.fetchall()

            if products_in_bin:
                print(f"\n    BIN {bin_code} INFORMATION     ")
                print(
                    f"Total products in bin: {len(products_in_bin)}\nFor the full information about a product please use the look up option \n")
                for code, name, category in products_in_bin:
                    if category == "clothing":
                        cursor.execute('SELECT xs,s,m,l,xl FROM clothing_sizes_backroom WHERE product_code=?', (code,))
                        sizes = cursor.fetchone()
                        total_stock = sum(sizes)
                        print(
                            f"{code} | {name} | Total: {total_stock} units | XS({sizes[0]}) S({sizes[1]}) M({sizes[2]}) L({sizes[3]}) XL({sizes[4]})")
                    elif category == "women_shoes":
                        cursor.execute(
                            'SELECT size_35,size_36,size_37,size_38,size_39,size_40,size_41 FROM women_shoes_sizes_backroom WHERE product_code=?',
                            (code,))
                        sizes = cursor.fetchone()
                        total_stock = sum(sizes)
                        print(
                            f"{code} | {name} | Total: {total_stock} units | 35({sizes[0]}) 36({sizes[1]}) 37({sizes[2]}) 38({sizes[3]}) 39({sizes[4]}) 40({sizes[5]}) 41({sizes[6]})")
                    elif category == "men_shoes":
                        cursor.execute(
                            'SELECT size_40,size_41,size_42,size_43,size_44,size_45,size_46,size_47,size_48,size_49 FROM men_shoes_sizes_backroom WHERE product_code=?',
                            (code,))
                        sizes = cursor.fetchone()
                        total_stock = sum(sizes)
                        print(
                            f"{code} | {name} | Total: {total_stock} units | 40({sizes[0]}) 41({sizes[1]}) ... 49({sizes[9]})")
            else:
                print(f"No products found in bin {bin_code}.")
            conn.close()

            if not return_to_menu():
                print("Thank you for using the inventory system. Goodbye!")
                break

        elif action == "C":
            sf_code = input("Please specify sales floor stander code: \n").strip().upper()
            conn = sqlite3.connect('stockroom.db')
            cursor = conn.cursor()
            cursor.execute('SELECT code, name, category FROM products WHERE salesfloor = ?', (sf_code,))
            products_on_floor = cursor.fetchall()

            if products_on_floor:
                print(f"\n    SALES FLOOR {sf_code} INFORMATION    ")
                print(
                    f"Total products on stander: {len(products_on_floor)}\nFor the full information about a product please use the look up option \n")
                for code, name, category in products_on_floor:
                    if category == "clothing":
                        cursor.execute('SELECT xs,s,m,l,xl FROM clothing_sizes_salesfloor WHERE product_code=?',
                                       (code,))
                        sizes = cursor.fetchone()
                        total_stock = sum(sizes)
                        print(
                            f"{code} | {name} | Total: {total_stock} units | XS({sizes[0]}) S({sizes[1]}) M({sizes[2]}) L({sizes[3]}) XL({sizes[4]})")
                    elif category == "women_shoes":
                        cursor.execute(
                            'SELECT size_35,size_36,size_37,size_38,size_39,size_40,size_41 FROM women_shoes_sizes_salesfloor WHERE product_code=?',
                            (code,))
                        sizes = cursor.fetchone()
                        total_stock = sum(sizes)
                        print(f"{code} | {name} | Total: {total_stock} units | 35({sizes[0]}) ... 41({sizes[6]})")
                    elif category == "men_shoes":
                        cursor.execute(
                            'SELECT size_40,size_41,size_42,size_43,size_44,size_45,size_46,size_47,size_48,size_49 FROM men_shoes_sizes_salesfloor WHERE product_code=?',
                            (code,))
                        sizes = cursor.fetchone()
                        total_stock = sum(sizes)
                        print(f"{code} | {name} | Total: {total_stock} units | 40({sizes[0]}) ... 49({sizes[9]})")
            else:
                print(f"No products found on stander {sf_code}.")
            conn.close()

            if not return_to_menu():
                print("Thank you for using the inventory system. Goodbye!")
                break

        elif action == "D":
            print("\n    AUTO-REPLENISHMENT LIST    ")
            conn = sqlite3.connect('stockroom.db')
            cursor = conn.cursor()
            cursor.execute('SELECT code, name, category, stockroom, salesfloor, maxshoestander, maxtype1 FROM products')
            all_products = cursor.fetchall()
            replenishment_list = []

            for code, name, category, stockroom, salesfloor, maxs, maxtype1 in all_products:
                max_capacity = maxs if maxs else maxtype1
                if not max_capacity:
                    continue

                if category == "clothing":
                    cursor.execute('SELECT xs,s,m,l,xl FROM clothing_sizes_backroom WHERE product_code=?', (code,))
                    total_backroom = sum(cursor.fetchone())
                    cursor.execute('SELECT xs,s,m,l,xl FROM clothing_sizes_salesfloor WHERE product_code=?', (code,))
                    total_salesfloor = sum(cursor.fetchone())
                elif category == "women_shoes":
                    cursor.execute(
                        'SELECT size_35,size_36,size_37,size_38,size_39,size_40,size_41 FROM women_shoes_sizes_backroom WHERE product_code=?',
                        (code,))
                    total_backroom = sum(cursor.fetchone())
                    cursor.execute(
                        'SELECT size_35,size_36,size_37,size_38,size_39,size_40,size_41 FROM women_shoes_sizes_salesfloor WHERE product_code=?',
                        (code,))
                    total_salesfloor = sum(cursor.fetchone())
                elif category == "men_shoes":
                    cursor.execute(
                        'SELECT size_40,size_41,size_42,size_43,size_44,size_45,size_46,size_47,size_48,size_49 FROM men_shoes_sizes_backroom WHERE product_code=?',
                        (code,))

HBM39258 = item("HBM39258", "blu m h", 125, "cotton", "blue", None, 9, 10, 23)
TBF59374 = item("TBF59374", "blu f t-s", 95, "polyester", "blue", None, 26, 24, 35)
PBM10247 = item("PBM10247", "blk m p", 180, "denim", "black", None, None, 10, 17)
BWF29164 = item("BWF29164", "whi f b", 140, "silk", "white", None, 15, 10, 28)
HGF62173 = item("HGF62173", "grn f h", 155, "fleece", "green", None, 9, 10, 23)
PBF41859 = item("PBF41859", "blu f p", 175, "linen", "blue", None, None, 9, 13)
HBF83461 = item("HBF83461", "blu f h", 150, "cotton", "blue", None, 9, 10, 23)
TSM62415 = item("TSM62415", "sil m t-s", 120, "polyblend", "silver", None, 26, 24, 35)
BWM67139 = item("BWM67139", "whi m b", 190, "nylon", "white", None, 15, 10, 28)
PWF32857 = item("PWF32857", "whi f p", 160, "denim", "white", None, None, 8, 10)
TBF94283 = item("TBF94283", "blu f t-s", 110, "cotton", "blue", None, 26, 24, 35)
HSM51674 = item("HSM51674", "sil m h", 165, "polyester", "silver", None, 9, 10, 23)
PBM95437 = item("PBM95437", "blu m p", 185, "cotton", "blue", None, None, 10, 17)
BPF37526 = item("BPF37526", "pnk f b", 135, "silk", "pink", None, 15, 10, 28)
TSF69284 = item("TSF69284", "sil f t-s", 130, "polyblend", "silver", None, 26, 24, 35)
HBM57263 = item("HBM57263", "blu m h", 145, "cotton", "blue", None, 9, 10, 23)
BWF87425 = item("BWF87425", "whi f b", 155, "linen", "white", None, 15, 10, 28)
HGF98462 = item("HGF98462", "grn f h", 160, "polyester", "green", None, 9, 10, 23)
TBM73561 = item("TBM73561", "blu m t-s", 100, "cotton", "blue", None, 26, 24, 35)
TWM85937 = item("TWM85937", "whi m t-s", 150, "satin", "white", None, 26, 24, 35)
HWF96482 = item("HWF96482", "whi f h", 170, "fleece", "white", None, 9, 10, 23)
PBM41875 = item("PBM41875", "blu m p", 175, "denim", "blue", None, 0, 9, 13)
BPF94267 = item("BPF94267", "pnk f b", 145, "silk", "pink", None, 15, 10, 28)
HBM61294 = item("HBM61294", "blu m h", 155, "cotton", "blue", None, 9, 10, 23)
TWM19736 = item("TWM19736", "whi m t-s", 125, "cotton", "white", None, 26, 24, 35)
PGM48529 = item("PGM48529", "grn m p", 165, "linen", "green", None, None, 10, 17)
BWF62453 = item("BWF62453", "whi f b", 135, "silk", "white", None, 15, 10, 28)
TBF19268 = item("TBF19268", "blu f t-s", 115, "cotton", "blue", None, 26, 24, 35)
HBF47891 = item("HBF47891", "blu f h", 160, "polyester", "blue", None, 9, 10, 23)
PWF31974 = item("PWF31974", "whi f p", 170, "denim", "white", None, None, 8, 10)
TWM93725 = item("TWM93725", "whi m t-s", 140, "cotton", "white", None, 26, 24, 35)
HGF87439 = item("HGF87439", "grn f h", 175, "fleece", "green", None, 9, 10, 23)
TBF47813 = item("TBF47813", "blu f t-s", 120, "polyblend", "blue", None, 26, 24, 35)
PGM72591 = item("PGM72591", "grn m p", 160, "linen", "green", None, None, 9, 13)
BPF19487 = item("BPF19487", "pnk f b", 175, "canvas", "pink", None, 15, 10, 28)
SBM78102 = item("SBM78102", "blu m s", 260, "leather", "blue", 12, None, None, None)
SBM45826 = item("SBM45826", "blu m s", 250, "leather", "blue", 12, None, None, None)
SBM58341 = item("SBM58341", "blu m s", 260, "leather", "blue", 12, None, None, None)
SBM84719 = item("SBM84719", "blu m s", 255, "leather", "blue", 12, None, None, None)
SWM75264 = item("SWM75264", "whi m s", 245, "synthetic", "white", 12, None, None, None)
SBF42178 = item("SBF42178", "blu f s", 225, "leather", "blue", 12, None, None, None)
SBF39528 = item("SBF39528", "blu f s", 210, "canvas", "blue", 12, None, None, None)
SWF92157 = item("SWF92157", "whi f s", 220, "canvas", "white", 12, None, None, None)
SWF48391 = item("SWF48391", "whi f s", 230, "leather", "white", 12, None, None, None)

clothes = [HBM39258, TBF59374, PBM10247, BWF29164, HGF62173, PBF41859, HBF83461, TSM62415, BWM67139, PWF32857,
           TBF94283, HSM51674, PBM95437, BPF37526, TSF69284, HBM57263, BWF87425, HGF98462, TBM73561, TWM85937,
           HWF96482, PBM41875, BPF94267, HBM61294, TWM19736, PGM48529, BWF62453, TBF19268, HBF47891, PWF31974,
           TWM93725, HGF87439, TBF47813, PGM72591, BPF19487]
men_shoes = [SBM78102, SBM45826, SBM58341, SBM84719, SWM75264]
female_shoes = [SBF42178, SBF39528, SWF92157, SWF48391]

for cloth in clothes:
    cloth["sizes_backroom"] = size_on_stock_backroom()
    cloth["sizes_salesfloor"] = size_on_stock_salesfloor()

for shoe in female_shoes:
    shoe["sizes_backroom"] = f_shoes_size_backroom()
    shoe["sizes_salesfloor"] = f_shoes_size_salesfloor()

for shoe in men_shoes:
    shoe["sizes_backroom"] = m_shoes_size_backroom()
    shoe["sizes_salesfloor"] = m_shoes_size_salesfloor()

print("Setting up database...")
setup_database()

clothing_locations = ["A111", "A112", "A113", "A114", "A115",
                      "A121", "A122", "A123", "A124", "A125",
                      "A131", "A132", "A133", "A134", "A135",
                      "A141", "A142", "A143", "A144", "A145",
                      "A211", "A212", "A213", "A214", "A215",
                      "A221", "A222", "A223", "A224", "A225",
                      "A231", "A232", "A233", "A234", "A235"]
clothing_sf_locations = ["SFA1", "SFA2", "SFA3", "SFA4", "SFA5",
                         "SFA6", "SFA7", "SFA8", "SFA9", "SFA10",
                         "SFA11", "SFA12", "SFA13", "SFA14", "SFA15",
                         "SFA16", "SFA17", "SFA18", "SFA19", "SFA20",
                         "SFA21", "SFA22", "SFA23", "SFA24", "SFA25",
                         "SFA26", "SFA27", "SFA28", "SFA29", "SFA30",
                         "SFA31", "SFA32", "SFA33", "SFA34", "SFA35"]
women_shoes_locations = ["B111", "B112", "B113", "B114"]
women_shoes_sf_locations = ["SFB1", "SFB2", "SFB3", "SFB4"]
men_shoes_locations = ["C111", "C112", "C113", "C114", "C115"]
men_shoes_sf_locations = ["SFC1", "SFC2", "SFC3", "SFC4", "SFC5"]

print("Saving products to database...")
for i, cloth in enumerate(clothes):
    save_product(cloth, "clothing", clothing_locations[i], clothing_sf_locations[i])

for i, shoe in enumerate(female_shoes):
    save_product(shoe, "women_shoes", women_shoes_locations[i], women_shoes_sf_locations[i])

for i, shoe in enumerate(men_shoes):
    save_product(shoe, "men_shoes", men_shoes_locations[i], men_shoes_sf_locations[i])

print("All products saved to database!\n")

# START THE PROGRAM
if __name__ == "__main__":
    main_menu()
