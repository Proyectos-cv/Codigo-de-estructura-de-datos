#version 1
def machinerec():
    idnumero=int(input("idnumero"))
    descripcion=raw_input("descripcion")
    promediofallos=float(input("promediofallos"))
    ultimoserviciodia=int(input ("ultimoserviciodia"))
    ultimoserviciomes=int(input("ultimoserviciomes"))
    ultimoservicioyear=int(input("ultimoservicioyear"))
    diascaidos=int(input ("diascaidos"))
    compradia=int (input("compradia"))
    comprames=int(input("comprames"))
    comprayear=int(input("comprayear"))
    costo=float(input ("costo"))

class version2():
    def date(self):
        dia=int(input ("dia"))
        mes=int(input("mes"))
        year=int(input("year"))
    def statistics(self):
        promediofallos=float(input ("promediofallos"))
        ultimoservicio=int(input("ultimoservicio"))
        diascaidos=int (input("diascaidos"))
    def machinerec(self):
        idnumero=int(input ("idnumero"))
        descripcion=raw_input("descripcion")
        historia=int(input("historia"))
        fechacompra=int(input("fechacompra"))
        costo=float(input("costo"))
machinerec()
v=version2()
v.date()
v.statistics()
v.machinerec()