def listaTerminos(**terminos):
    for llave , valor in terminos.items():
        print(f'{llave}: {valor}')

listaTerminos(IDE= 'Integrated Developement Environment', PK='Primary Ket')