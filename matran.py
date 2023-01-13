import random
import numpy as np
def nhan_vector_voi_matran():

  x =[random.randint(-10,10) for i in range(4)]
  print("vecto x =", x)

  v = np.random.randint(low=-1,high=10, size=8)
  a = v.reshape(2,4)
  print("ma trận A =\n",a)

  n = x*a
  print("x*A =\n",n)

def nhan_matran_voi_matran():
  v = np.random.randint(low=-1, high=10, size=16)
  a = v.reshape(4, 4)
  print("ma trận A =\n",a)

  v = np.random.randint(low=-1,high=10, size=20)
  b = v.reshape(4,5)
  print("B =\n", b)
  print("Ma trận A*B = \n",a.dot(b))

  at=np.transpose(a)
  print("Ma trận chuyển vị A^T = \n",at)

  ab = at@b
  print("Ma trận nhân A^T*B = \n",ab)
def main():
  nhan_vector_voi_matran()
  nhan_matran_voi_matran()

if __name__=="__main__":
  main()





