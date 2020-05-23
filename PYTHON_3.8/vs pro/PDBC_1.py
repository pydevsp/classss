import cx_Oracle as cxo
con = cxo.connect ('scott/tiger@localhost:1521')
cursorp = con.cursor()
DATA = cursorp.execute('select * from emp')
print(DATA.fetchall())


print("-=-=-=-=-=-")
for row in cursorp:
    print(row)

cursorp.close()
con.close()


# print(con.version)
# con.close()



# 


# cxo.connect ('scott/tiger@`192`.168.1.9:1521')``s`