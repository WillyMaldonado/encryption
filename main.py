import numpy as np 

def inverse_diagonal(matrix):
    return np.where(matrix != 0, 1 / matrix, 0)

def main():
    rows = int(input("Write the number of rows you want \n"))
    cols = int(input("Write the number of cols you want \n"))
    key_matrix = np.zeros((rows,cols), dtype=int)
    if cols == rows:
        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                number = int(input('Write the number \n'))
                key_matrix[i][j] = number
        # print(key_matrix)
        # print(key_matrix.diagonal())
        # print(key_matrix[::-1].diagonal())
        # key_matrix = np.resize(key_matrix,(rows + 2,cols))
        if cols == 2 or  rows == 2:
            print(key_matrix)
            print("Get the determinant by multiply the principal and inverse diagonals and add a"
                    ,'subtraction sing to the inverse diagonal',key_matrix.diagonal(),"and", key_matrix[::-1].diagonal()[::-1])
            print('Like this:', key_matrix.diagonal(),'-',key_matrix[::-1].diagonal()[::-1])
            print((key_matrix.diagonal()[0] * key_matrix.diagonal()[1]),'-',(key_matrix[::-1].diagonal()[0] * key_matrix[::-1].diagonal()[1]))
            print('Result = ',((key_matrix.diagonal()[0] * key_matrix.diagonal()[1])-(key_matrix[::-1].diagonal()[0] * key_matrix[::-1].diagonal()[1])))


    else:
        print("The matrix isn't square so don't have a determinant")

        
    # print(key_matrix)
    # det = np.linalg.det(key_matrix)
    # if round(det) != 0:
    #     print(f"This matrix have inverse")
    # else:
    #     print(f"This matrix not have inverse")
main()