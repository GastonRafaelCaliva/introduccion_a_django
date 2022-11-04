from portfolio.models import Proyecto

class Generar():
    def generar(self,):
        p3 = Proyecto(titulo="SGI Toners y Reciclados",
                      descripcion="Aplicacion de escritorio para la gestion de reciclados de toner de ECIN",
                      tecnologias="VB SQL", link="https://www.ecinsoluciones.com", imagen="img/turismo.png")

        p3.save()
        p2 = Proyecto(titulo='Compra en tu barrio',
                      descripcion='Plataforma web de comercio electronico para comercios y emprendedores de la Ciudad de Salta',
                      tecnologias='SQL Server, ASP, Codecharge', link="https://compraentubarrio.gob.ar/",
                      imagen='img/compraen.png')

        p2.save()
        p1 = Proyecto(titulo='SGI de Pozos Petroleros',
                      descripcion='Plataforma web para la gestion de datos de pozos petroleros de estacion Caimancito',
                      tecnologias='SQL Server, ASP, Codecharge', link='https://www.lanacion.com',
                      imagen='img/pozos.png')
        p1.save()

    '''
    def generar(self, cantModels):
        cant = cantModels
        if cant == 3:
            p3 = Proyecto(titulo="SGI Toners y Reciclados",
                          descripcion="Aplicacion de escritorio para la gestion de reciclados de toner de ECIN",
                          tecnologias="VB SQL", link="https://www.ecinsoluciones.com", imagen="img/turismo.png")

            p3.save()
            cant = cant - 1
            
        if cant == 2:
            p2 = Proyecto(titulo='Compra en tu barrio',
                          descripcion='Plataforma web de comercio electronico para comercios y emprendedores de la Ciudad de Salta',
                          tecnologias='SQL Server, ASP, Codecharge', link="https://compraentubarrio.gob.ar/",
                          imagen='img/compraen.png')

            p2.save()
            cant = cant - 1
            
        if cant == 1:
            p1 = Proyecto(titulo='SGI de Pozos Petroleros',
                          descripcion='Plataforma web para la gestion de datos de pozos petroleros de estacion Caimancito',
                          tecnologias='SQL Server, ASP, Codecharge', link='https://www.lanacion.com',
                          imagen='img/pozos.png')

            p1.save()
    '''
