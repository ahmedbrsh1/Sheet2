def playFair(text):
    rows, cols = 5, 5
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            value = text[i]
            row.append(value)
        matrix.append(row)

    print(matrix)
    
    
    
        
playFair("ABDCD")
# method = input("1-Encrypt \n 2-Decrypt")
#     text = input("Enter Text")
#     if method == 1: