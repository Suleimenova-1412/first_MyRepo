import tabula
myfile = 'pricee.pdf'
mytable =tabula.read_pdf(myfile)
print(mytable[0])
