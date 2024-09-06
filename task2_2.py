def rotate_matrix_90(matrix):
    for i in range(len(matrix)):
     for j in range (i,len(matrix)):
      test1=matrix[i][j]
      test2=matrix[j][i]
      matrix[i][j]=test2
      matrix[j][i]=test1


    for i in range(len(matrix)):
      matrix[i].reverse()  

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

 
def main():
 print("The Original Matrix:")
 for i in range(len(matrix)):
  print(matrix[i])
 rotate_matrix_90(matrix)
 print("The Rotated Matrix:")
 for i in range(len(matrix)):
  print(matrix[i])



if __name__ == "__main__":
    main()        