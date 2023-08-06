#Imports
import numpy as np

###########Classes

#Operators
class Operator:
    #Initializing the operator
    def __init__(self,matrix,unrestricted=False):
        matrix=np.array(matrix)
        if(np.array(matrix.shape).size!=2):
            raise(Exception("The matrix should have 2 indicies."))
        if(matrix.shape[0]!=matrix.shape[1]):
            raise(Exception("The matrix is not a square matrix"))
        if(not unrestricted):
            if(np.log2(matrix.shape[0])-(int)(np.log2(matrix.shape[0]))!=0):
                raise(Exception("The matrix has to be 2^n dimensional"))
            if(np.abs(np.abs(np.linalg.det(matrix))-1)>0.00000000001):
                print(np.linalg.det(matrix))
                raise(Exception("Determinant of the matrix is not 1"))
        self.matrix=matrix
        self.dim=int(matrix.shape[0])
        self.qubits=int(np.log2(matrix.shape[0]))
    
    #print
    def __str__(self):
        return self.matrix.__str__()

    #Adjoint operator
    def dgr(self):
        return Operator(np.asarray(np.asmatrix(self.matrix).H))

    #~ can be used to get the adjoint operator
    def __invert__(self):
        return self.dgr()

    #Kronecker product
    def __mul__(self,other):
        if(type(other)!=Operator):
            raise(Exception("Only two operators can create a Kronecker product"))
        return Operator(kron(self.matrix,other.matrix))
    
    #Acting on the operator
    def __add__(self,other):
        if(type(other)==Statevector):
            raise(Exception("A statevector can't act on an operator.\n If you want to act on the state with the operator, switch the order."))
        if(type(other)!=Operator):
            raise(Exception("Incompatible type. Only an operator can act on an operator."))
        return Operator(other.matrix@self.matrix)

#Statevector
class Statevector:
    #Initializating statevector
    def __init__(self,vector,unrestricted=False,quiet=False):
        vector=np.array(vector)
        self.vector=vector
        if(np.array(vector.shape).size!=1):
            raise(Exception("The vector should have 1 index."))
        if(not unrestricted):
            if(np.log2(vector.shape[0])-(int)(np.log2(vector.shape[0]))!=0):
                raise(Exception("The vector has to be 2^n dimensional"))
            if(np.dot(vector.conjugate(),vector)!=1):
                if(not quiet):
                    print("WARNING! Initialized vector is not normal. Normalizing vector")
                self.normalize()
        self.dim=int(vector.shape[0])
        self.qubits=int(np.log2(vector.shape[0]))
    
    #Normalization
    def normalize(self):
        self.vector=self.vector/np.sqrt(np.dot(self.vector.conjugate(),self.vector))

    #Acting on the state
    def __add__(self,other):
        if(type(other)==Statevector):
            raise(Exception("A statevector can't act on a statevector."))
        if(type(other)!=Operator):
            raise(Exception("Incompatible type. Only an operator can act on a state."))
        return Statevector(other.matrix@self.vector,quiet=True)
    
    #Tensor product of states
    def __mul__(self,other):
        newState=[]
        for i in range(self.dim*other.dim):
            newState.append(other.vector[i%other.dim]*self.vector[(i//other.dim)%self.dim])
        return Statevector(newState,quiet=True)

    #Printing the statevector
    def __str__(self):
        retstr=""
        for i in range(len(self.vector)):
            if(not np.allclose(self.vector[i],0)):
                s=str(self.vector[i])+" * |"
                s2=""
                for j in range((int)(np.log2(len(self.vector)))):
                    s2=str(i%2)+s2
                    i=i//2
                s+=s2+">"
                if(retstr!=""):
                    retstr+="\n"
                retstr+=s
        return(retstr)

    #Measurement of a single qubit on the computational basis
    def measure(self,n):
        p=[0,0]
        v=[[],[]]
        for i in range(self.vector.size):
            p[(i//(2**n))%2]+=abs(self.vector[i])**2
            v[(i//(2**n))%2].append(1)
            v[(i//(2**n)+1)%2].append(0)
        v=np.array(v)
        if(p[0]>np.random.rand()):
            self.vector=v[0]*self.vector/np.sqrt(p[0])
            return 0
        else:
            self.vector=v[1]*self.vector/np.sqrt(p[1])
            return 1 
    
    #Measure all qubits on the computational basis
    def measure_all(self):
        returnValue=">"
        for i in range(self.qubits):
            s=self.measure(i)
            returnValue=str(s)+returnValue
        returnValue="|"+returnValue
        return returnValue
###########Functions

#Multi matrix kronecker product
def kron(*args):
    returnValue=np.array([1])
    for i in args:
        returnValue=np.kron(returnValue,i)
    return returnValue

#Outer product
def outer(a,b):
    return np.outer(a,np.conjugate(b))

###########Gate definitions

######Single qubit gates

#Identity
I=Operator(np.identity(2))

#Pauli-X
X=Operator(np.array([
    [0,1],
    [1,0]
    ]))


#Pauli-Y
Y=Operator(np.array([
    [0,-1j],
    [1j,0]
    ]))

#Pauli-Z
Z=Operator(np.array([
    [1,0],
    [0,-1]
    ]))

#Hadamard
H=Operator(np.array([
    [1,1],
    [1,-1]
    ])/np.sqrt(2))

#S gate
S=Operator(np.array([
    [1,0 ],
    [0,1j]
]))

#S dagger gate
Sdgr=Operator(np.array([
    [1,0 ],
    [0,-1j]
]))

#T gate
T=Operator(np.array([
    [1, 0                 ],
    [0, np.exp(np.pi*1j/4)]
]))

#T dagger gate
Tdgr=Operator(np.array([
    [1, 0                 ],
    [0, np.exp(-np.pi*1j/4)]
]))

#Phase gate
def P(angle):
    return Operator(np.array([
        [1, 0               ],
        [0, np.exp(1j*angle)]
    ]))

####Multi-qubit gates

#Controlled X gate
CX=Operator(np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
	]))

#Controlled Z gate
CZ=Operator(np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,-1]
]))

#Controlled Y gate
CY=Operator(np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,-1j],
    [0,0,1j,0]
]))

#Controlled Hadamard gate
CH=Operator(np.array([
    [np.sqrt(2),0         ,0,0 ],
    [0         ,np.sqrt(2),0,0 ],
    [0         ,0         ,1,1 ],
    [0         ,0         ,1,-1]
])/np.sqrt(2))

#SWAP gate
SWAP=Operator(np.array([
    [1,0,0,0],
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,1]
    ]))

#Toffoli gate
CCX = Operator(np.array([
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,0]
]))

#######Defining some useful states
#0
s0=Statevector([1,0])

#1
s1=Statevector([0,1])

#+
sp=Statevector([1/np.sqrt(2),1/np.sqrt(2)],quiet=True)

#-
sm=Statevector([1/np.sqrt(2),-1/np.sqrt(2)],quiet=True)