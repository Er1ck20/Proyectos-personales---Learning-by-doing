class funciones_str_utiles:

    def __init__(self, x):
        self.x = x

    def mayusculas(self):
        return self.x.upper()
    
    def sin_espacios(self):
        return self.x.strip()
    
if __name__ == 'main':
    text = funciones_str_utiles(" Sant Domingo     ")
    print(text.sin_espacios())
    print(text.mayusculas())