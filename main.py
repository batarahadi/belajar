import pandas as pd

dataMenu = {"listMenu" : ["Nasi Goreng", "Mie Goreng", "Ayam Penyet", "Sate Ayam", "Gado-Gado"],
            "price" : [15000, 12000, 20000, 18000, 10000]}


df = pd.DataFrame(dataMenu)
print(df)