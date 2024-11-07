def pascal_triangle(n):
    triangle = []

    for row in range(n):
        new_row = [1] * (row + 1)
        
        for col in range(1, row):
            new_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        
        triangle.append(new_row)
    
    for row in triangle:
        print(" ".join(map(str, row)))

n = int(input("Podaj liczbę wierszy trójkąta Pascala: "))
pascal_triangle(n)
