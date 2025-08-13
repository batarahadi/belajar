import pandas as pd

dataMenu = {"listMenu" : ["Nasi Goreng", "Mie Goreng", "Ayam Penyet", "Sate Ayam", "Gado-Gado"],
            "price" : [15000, 12000, 20000, 18000, 10000]}

# membuat DataFrame
dfMenu = pd.DataFrame(dataMenu)

# Format harga satuan dengan titik dan menambahkan "Rp"
dfMenu["price"] = dfMenu["price"].apply(lambda x: f"Rp {x:,}".replace(",", "."))

# Menampilkan DataFrame
print(dfMenu)