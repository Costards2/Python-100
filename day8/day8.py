text = input("Write your messag:\n")
off_set = input("Write the shift you want\n")

cypher_message =""

print()

for letter in text:
    if letter.isalpha():  # só letras
        num = ord(letter) - ord('a')
        num = (num + off_set) % 26
        cypher_message += chr(num + ord('a'))
    else:
        cypher_message += letter  # mantém espaços, pontuação etc.

print(cypher_message)