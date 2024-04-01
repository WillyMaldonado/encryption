import numpy as np 

def main():
    rows = int(input("Write the number of rows you want \n"))
    cols = int(input("Write the number of cols you want \n"))
    key_matrix = np.zeros((rows,cols), dtype=int)
    determinant = 0
    if cols == rows:
        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                number = int(input('Write the number \n'))
                key_matrix[i][j] = number
        if cols == 2 or  rows == 2:
            print(key_matrix)
            print("Get the determinant by multiply the principal and inverse diagonals and add a"
                    ,'subtraction sing to the inverse diagonal',key_matrix.diagonal(),"and", key_matrix[::-1].diagonal()[::-1])
            print('Like this:', key_matrix.diagonal(),'-',key_matrix[::-1].diagonal()[::-1])
            print((key_matrix.diagonal()[0] * key_matrix.diagonal()[1]),'-',(key_matrix[::-1].diagonal()[0] * key_matrix[::-1].diagonal()[1]))
            print('Result = ',((key_matrix.diagonal()[0] * key_matrix.diagonal()[1])-(key_matrix[::-1].diagonal()[0] * key_matrix[::-1].diagonal()[1])))
            determinant = ((key_matrix.diagonal()[0] * key_matrix.diagonal()[1])-(key_matrix[::-1].diagonal()[0] * key_matrix[::-1].diagonal()[1]))
        else:
            print(key_matrix)
            aux_matrix = key_matrix
            aux_matrix2 = key_matrix
            print("First we need to add the first and the second row to the matrix:")
            key_matrix = np.resize(key_matrix,(rows + 2,cols))
            print(key_matrix)
            print("Then you need to found the principal diagonals like the following ones:")
            print(key_matrix.diagonal())
            diagonal1 = key_matrix.diagonal()
            key_matrix = np.delete(key_matrix,0,axis=0)
            print(key_matrix.diagonal())
            diagonal2 = key_matrix.diagonal()
            key_matrix = np.delete(key_matrix,0,axis=0)
            print(key_matrix.diagonal())
            diagonal3 = key_matrix.diagonal()
            print("Then you need to found the inverse diagonals like the following:")
            print(aux_matrix[::-1].diagonal()[::-1])
            idiagonal1 = aux_matrix[::-1].diagonal()[::-1]
            aux_matrix = np.resize(aux_matrix,(rows+2,cols))
            aux_matrix = aux_matrix[::-1]
            aux_matrix = np.delete(aux_matrix,0,axis=0)
            print(aux_matrix.diagonal()[::-1])
            idiagonal2 = aux_matrix.diagonal()[::-1]
            row_deleted = np.delete(aux_matrix2,1,0)
            aux_matrix2 = np.flip(aux_matrix2)
            aux_matrix2 = np.roll(aux_matrix2,2,axis=0)
            print(aux_matrix2[::-1].diagonal())
            idiagonal3 = aux_matrix2[::-1].diagonal()
            print("The last step is adding '-' to the multiply of the inverse diagonal \n")
            print(f'({np.prod(diagonal1)} + {np.prod(diagonal2)} + {np.prod(diagonal3)})',
                    ' - ',f'({np.prod(idiagonal1)} + {np.prod(idiagonal2)} + {np.prod(idiagonal3)})')
            print(f'({np.prod(diagonal1) + np.prod(diagonal2) + np.prod(diagonal3)})',
                    ' - ',f'({np.prod(idiagonal1) + np.prod(idiagonal2) + np.prod(idiagonal3)})')
            print('Determinant = ',(np.prod(diagonal1) + np.prod(diagonal2) + np.prod(diagonal3))-(np.prod(idiagonal1) + np.prod(idiagonal2) + np.prod(idiagonal3)))
            determinant = (np.prod(diagonal1) + np.prod(diagonal2) + np.prod(diagonal3))-(np.prod(idiagonal1) + np.prod(idiagonal2) + np.prod(idiagonal3))

        if determinant != 0:
            print("The key have inverse so let's find it:")
            
        else:
            print("The determinant is 0 so the matrix don't have inverse and you cannot find the encrypted message with this.")



    else:
        print("The matrix isn't square so don't have a determinant")

        
    # print(key_matrix)
    # det = np.linalg.det(key_matrix)
    # if round(det) != 0:
    #     print(f"This matrix have inverse")
    # else:
    #     print(f"This matrix not have inverse")
main()