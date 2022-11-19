nombre=[]
password=[]
cedula=[]
class Password:
  def registra_(self):
    print("POR FAVOR REGISTRARSE PARA CREAR TU CUENTA")
    self.nombre = input("NOMBRE TITULAR\n:")
    self.password = int(input("CONTRASEÑA TITULAR\n:"))
    self.cedula=int(input("CEDULA TITULAR\n:"))
    nombre.append(self.nombre)
    password.append(self.password)
    cedula.append(self.cedula)
    print("      REGISTRO EXITOSO    ")
class Usuario(Password):
   def inicio(self):
    print("      BIENVENID@S       ")
    usuario = input("USUARIO\n:")
    if usuario in nombre:
        contraseña = int(input("CONTRASEÑA\n"))
        if contraseña in password:
                print(" USUARIO O CONTRASEÑA CORRECTAS")
        else:
            print("USUARIO O CONTRASEÑA INCORRECTOS")
            self.inicio()

class Transferencias(Usuario):
   def datos (self):
        print("BIENVENIDO A BANCO PRESTAMAS "f"{nombre}")
        balance=0
        print("SALDO DE:",balance)
        print("DESEA CONSIGNAR SU CUENTA?")
        print("1= si")
        print("2-no")
        cuenta= int(input("DIGITA LA OPCION DESEADA:"))

        if cuenta== 1:
            deposito= int(input("VALOR A CONSIGNACION: "))
            saldo=deposito+ balance
            print("TU CONSIGNACION SE HA REALIZADO CON EXITO :"f"{saldo}")
            print("DESEAS RETIRAR O TRANSFERIR")
            print("1=RETIRAR")
            print("2=TRANSFERIR ")
            print("3= Salir")
            depositar= int(input("DIGITA LA OPCION QUE DESEAS:"))

            if depositar== 1:
                print("SALDO:",saldo)
                print("VALOR A RETIRAR: ")
                sacar=int(input("="))
                if sacar <= deposito:
                    print(" RETIRO EXITOSO")
                    print("SALDO DISPONIBLE:",sacar-saldo)
                    print("GRACIAS POR RETIRAR EN BANCO PRESTAMAS")
                else:
                    if sacar > deposito:
                        print("\n Saldo Insufiente")
                        self.datos()
            if depositar==2:
                print("TRANSFERIR:")
                num= int(input("NUMERO DE CUENTA:"))
                print("SU SALDO DISPONIBLE",deposito)
                total=int(input("TOTAL A TRANSFERIR:"))
                if total <= deposito:
                    print("TRANSFERENCIA EXITOSA")
                    print("# de cuenta",num)
                    print("TOTAL A TRANSFERIR",total)
                else:
                    if total > deposito:
                        print("Saldo Insufiente")
                        exit()
            if depositar==3:
                print("FUE UN GUSTO PARA NOSOTROS ATENDERTE ATT:BANCO PRESTAMAS")
                exit()
        else:
            if cuenta==2:
                print("FUE UN GUSTO PARA NOSOTROS ATENDERTE ATT:BANCO PRESTAMAS")
                exit()

banco=Password()
banco.registra_()
banco=Usuario()
banco.inicio()
banco=Transferencias()
banco.datos()
