class Product:
    product_Id = ""
    product_Name = ""
    product_Price = ""
    product_Quantity = ""
    def __init__(self):
        pass
        #self.id_SP = id_SP
        #self.ten_SP = ten_SP
        #self.gia_SP = gia_SP
        #self.sl_SP = sl_SP

    #def printProduct(self):
     #   print()

f = open('D:\\PYTHON CORE\\Bai hoc File Python\\Buoi11\\DATA_FILE.txt')
data = f.read()

new_data = data.split('{SAN_PHAM')
new_data1 = list(filter(None, new_data))

danhSachSanPham = []

# Add new comment

for i in range(len(new_data1)):
    listAttribute = new_data1[i].split('\n')
    listAttribute = list(filter(None, listAttribute))
    product = Product()
    for e in range(len(listAttribute)):
        new_listAttribute = listAttribute[e].split(': ')
        if new_listAttribute[0] == 'ID_SP':
           product.product_Id = new_listAttribute[1]
        if new_listAttribute[0] == 'TEN_SP':
           product.product_Name = new_listAttribute[1]
        if new_listAttribute[0] == 'GIA_SP':
           product.product_Price = new_listAttribute[1]
        if new_listAttribute[0] == 'SL_SP':
           product.product_Quantity = new_listAttribute[1]
    danhSachSanPham.append(product)

for ds in danhSachSanPham:
    print(ds.product_Id, '-',  ds.product_Name, '-', ds.product_Price, '-', ds.product_Quantity)
        #print(new_listAttribute)

import pyodbc
# Ket noi den CSDL SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TOMHOUSE-PC;'
                      'Database=QUAN_LY_NHAN_VIEN;'
                      'Trusted_Connection=Yes;')

#
cursor = conn.cursor()
cursor.execute("select*from dbo.PRODUCT")
for p in danhSachSanPham:
    s = ""
    id = p.product_Id
    name = p.product_Name
    price = p.product_Price
    quantity = p.product_Quantity

    s = "INSERT INTO PRODUCT VALUE('" + id + "','" + name + "','" + price + "','" + quantity + ")"
    cursor.execute(s)

    conn.commit(); # Chay lenh nay de thuc hien thay doi
"""
def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute("insert into product")
"""
