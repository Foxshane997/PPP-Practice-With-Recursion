# Pascals Triangle Function

def pascal(n):
    triangle = []

    for i in range(n):
        # Initialize the current row with 1s
        row = [1] * (i + 1)
        
        # Calculating the values in the current row
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        # Adding the current row to the triangle
        triangle.append(row)
    
    for row in triangle:
        print(' '.join(map(str, row)).center(n * 2))

# calling the Function - The number can be changed to change the size of the pyramid
pascal(6) 

