class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
   
   def getMoto(self):
      moto = Moto()
      
      # Primeiro diz o tipo de moto
      tipo = self.__builder.getTipo()
      moto.setTipo(tipo)
      
      # Depois a cilindrada do motor
      motor = self.__builder.getMotor()
      moto.setMotor(motor)
      
      # e dois pneus 
      i = 0
      while i < 4:
         pneu = self.__builder.getPneu()
         moto.attachPneu(pneu)
         i += 1
      return moto

# The whole product
class Moto:
   def __init__(self):
      self.__pneus = list()
      self.__motor = None
      self.__tipo = None

   def setTipo(self, tipo):
      self.__tipo = tipo

   def attachPneu(self, pneu):
      self.__pneus.append(pneu)

   def setMotor(self, motor):
      self.__motor = motor

   def especificacoes(self):
      print ("tipo de moto: %s" % self.__tipo.forma)
      print ("cilindrada do motor: %d" % self.__motor.cilindrada)
      print ("tamanho dos pneus: %d\'" % self.__pneus[0].tamanho)

class Builder:
      def getPneu(self): pass
      def getMotor(self): pass
      def getTipo(self): pass

class CB300rBuilder(Builder):
   
   def getPneu(self):
      pneu = Pneu()
      pneu.tamanho = 17
      return pneu
   
   def getMotor(self):
      motor = Motor()
      motor.cilindrada = 300
      return motor
   
   def getTipo(self):
      tipo = Tipo()
      tipo.forma = "Street"
      return tipo

# Partes da moto
class Pneu:
   tamanho = None

class Motor:
   cilindrada = None

class Tipo:
   forma = None

def main():
   cb300rBuilder = CB300rBuilder() # inicializando a classe
   
   director = Director()
   
   # Build CB300r
   print ("CB300r")
   director.setBuilder(cb300rBuilder)
   CB300r = director.getMoto()
   CB300r.especificacoes()
   print ("")

if __name__ == "__main__":
   main()
