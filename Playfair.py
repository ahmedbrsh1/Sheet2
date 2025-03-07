def generate_matrix(keyword):
    keyword = keyword.replace("j", "i")
    matrix = []
    seen = []
    
    for char in keyword:
        if char not in seen and char.isalpha():
            seen.append(char)
    
    for char in "abcdefghiklmnopqrstuvwxyz":
        if char not in seen:
            seen.append(char)
    
    for i in range(0, 25, 5):
        matrix.append(seen[i:i+5])
    
    return matrix

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def prepare_text(text):
    text = text.replace("j", "i").lower()
    prepared = ""
    
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        
        if a == b:
            prepared += a + 'x'
            i += 1
        else:
            prepared += a + b
            i += 2
    
    if len(prepared) % 2 != 0:
        prepared += 'x'
    
    return prepared

def encrypt(text, matrix):
    text = prepare_text(text)
    encrypted = ""
    
    for i in range(0, len(text), 2):
        row1, col1 = find_position(matrix, text[i])
        row2, col2 = find_position(matrix, text[i+1])
        
        if row1 == row2:
            encrypted += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            encrypted += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            encrypted += matrix[row1][col2] + matrix[row2][col1]
    
    return encrypted

def decrypt(text, matrix):
    decrypted = ""
    
    for i in range(0, len(text), 2):
        row1, col1 = find_position(matrix, text[i])
        row2, col2 = find_position(matrix, text[i+1])
        
        if row1 == row2:
            decrypted += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            decrypted += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            decrypted += matrix[row1][col2] + matrix[row2][col1]
    
    return decrypted

def main():
    keyword = input("Enter keyword: ").lower()
    matrix = generate_matrix(keyword)
    
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    text = input("Enter text: ").lower()
    
    if choice == 'e':
        print("Encrypted text:", encrypt(text, matrix))
    elif choice == 'd':
        print("Decrypted text:", decrypt(text, matrix))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
