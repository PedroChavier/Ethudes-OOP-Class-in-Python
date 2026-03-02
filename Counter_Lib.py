from enum import Enum 
class PolarPosition(Enum):
    Upper = 0
    Lower = 1
    PolarInvers = 2

from typing import Union 
LimiteVall = Union[None , tuple[float, bool]]
LimitType = tuple[LimiteVall,LimiteVall]
  
class Counter:
    #Anotações:
        #CORREÇÕES:
        #IMPLEMENTAÇÕES
                    # 01 Fazer adição da sub-rotina → def config(*args):. 
                    # 02 Desenvolver criativamente o argumento self.analog (lembrét: a função se dispõe a orientar a modalidade 
                                                                                                            # que o contador exercerá após atingir limites).
                    # 03 Fazer o def commit(): e o def charge(): + def __getattribute__(): para comitar e carregar marcas dos passos
        #FEEDBACK:
                    # 01 Lógica matématica de limites se comportou como o esperado em todo o teste.
                    # 02 Deslocamento do self.register auxiliado por: self.increment/self.polar mostrou-se ter lógica correta.
    def __init__(self,
                 increment: float,
                 limit: LimitType=None, 
                 register: float = None,
                 analog: bool = False,
                 polar: bool = True,
                 operant: bool = True):
        """
        limit : LimitType
            Tipo aceito: [[None, Tuple[float,bool]], [None, Tuple[float,bool]]]
        """
        from sympy import oo as infinit
        # Procuração caso não haja limite inferior e superior.: Tratação booleana (self.unlimit:bool)
        self.unlimit=(limit is None) or ((limit[0] is None) and (limit[1] is None))

        # Extração de máximo e mínimo. Definição de self.register caso não exista e inicialização de self.init_point:
        if not self.unlimit:
            inf, sup = limit
            newIc=[None,None]
            if isinstance(inf, tuple):
                self.min, newIc[0] = inf
            else:
                self.min, newIc[0] = -infinit, None
            if isinstance(sup, tuple):
                self.max, newIc[1] = sup
            else:
                self.max, newIc[1] = infinit, None

            # Extração de self.wall para definir Limite permitido em __call__.:
            wall_map = {
                (None, False): 1,
                (None, True): 2,
                (False, None): 3,
                (False, False): 4,
                (False, True): 5,
                (True, None): 6,
                (True, False): 7,
                (True, True): 8
            }
            self.wall = wall_map[tuple(newIc)] 

            if register is None:
                if newIc[0] is None and newIc[1] is not None :
                    self.register=self.max
                elif newIc[0] is not None and newIc[1] is None :
                    self.register=self.min
                else:
                    self.register=(self.max + self.min)/2
            else:
                match self.wall:
                    case 1:  # (-∞, b)
                        if not (-infinit < register < self.max): raise TypeError("Invalid -register- unresponse about -limit-")
                    case 2:  # (-∞, b]
                        if not (-infinit < register <= self.max): raise TypeError("Invalid -register- unresponse about -limit-")
                    case 3:  # (a, +∞)
                        if not (self.min < register < infinit): raise TypeError("Invalid -register- unresponse about -limit-")
                    case 4:  # (a, b)
                        if not (self.min < register < infinit): raise TypeError("Invalid -register- unresponse about -limit-")
                    case 5:  # (a, b]
                        if not (self.min < register <= self.max): raise TypeError("Invalid -register- unresponse about -limit-")
                    case 6:  # [a, +∞)
                        if not (self.min <= register < infinit): raise TypeError("Invalid -register- unresponse about -limit-")
                    case 7:  # [a, b)
                        if not (self.min <= register < self.max): raise TypeError("Invalid -register- unresponse about -limit-")
                    case 8:  # [a, b]
                        if not (self.min <= register <= self.max): raise TypeError("Invalid -register- unresponse about -limit-")
                self.register=register
        else:
            self.register=0 if register is None else register
        self.init_point=self.register

        self.increment=increment
        self.polar=polar
        self.analog=analog
        self.operant=operant

    def __repr__(self):
        return str(self.register)
    
    def __call__(self,polar_pass: int | PolarPosition | None = None,increment_pass:float=None):
            from sympy import oo as infinit
            from decimal import Decimal as decim, getcontext as gcont
            gcont().prec=10
            if not self.operant: return float(self.register)

            if polar_pass is not None:
                if isinstance(polar_pass,PolarPosition) == True:
                    try:
                        polar_pass== PolarPosition(polar_pass)
                    except:
                        raise TypeError("-polar_pass- value unexpected")
                match polar_pass:
                    case 0: polo=1
                    case 1: polo=(-1)
                    case 2: polo= 1 if self.polar == False else (-1)
                    case _: raise TypeError("-polar_pass_ unexpected")        
            else:
                polo= 1 if self.polar == True else (-1)
            
            inc=self.increment if increment_pass==None else increment_pass

            prog= decim(str(self.register))+(decim(str(inc))*polo)
            if self.unlimit==False:
                match self.wall:
                    case 1:  # (-∞, b)
                        if not (-infinit < prog < self.max): return self.register
                    case 2:  # (-∞, b]
                        if not (-infinit < prog <= self.max): return self.register
                    case 3:  # (a, +∞)
                        if not (self.min < prog < infinit): return self.register
                    case 4:  # (a, b)
                        if not (self.min < prog < infinit): return self.register
                    case 5:  # (a, b]
                        if not (self.min < prog <= self.max): return self.register
                    case 6:  # [a, +∞)
                        if not (self.min <= prog < infinit): return self.register
                    case 7:  # [a, b)
                        if not (self.min <= prog < self.max): return self.register
                    case 8:  # [a, b]
                        if not (self.min <= prog <= self.max): return self.register
            self.register=decim(str(prog))
            return float(decim(str(self.register)))

    
    def Config(self):
        pass

    def SetPlace(self,Vall:float):
        if Vall<=self.max or Vall>=self.min:
            self.register=Vall

    def SetOrigem(self):
        self.register=self.init_point
            

test=Counter(2)
test.config()
test()

print(test)