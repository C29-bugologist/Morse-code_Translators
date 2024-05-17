# Define the Morse code dictionary.
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Convert a message to Morse code.
def to_morse_code(message):
    
  morse_code = ''
  for char in message.upper():
      if char in morse_dict:
          morse_code += morse_dict[char] + ' '
  return morse_code

def to_text_code(morse_code):
  text_code = ''
  morse_code = morse_code.split(' ')
  for code in morse_code:
      for char, morse in morse_dict.items():
          if morse == code:
              text_code += char
  return text_code

print("\n----------Morse Code---------\n")
while True:
  choice = input("Enter '1' for converting into Morse Code\nEnter '2'for converting into text\nEnter '3' to Exit\n  ")
  if choice == "1":
     message = input("Enter the text:\n")
     print(to_morse_code(message))
  elif choice =="2":
     message = input("Enter the Morse Code:\n")
     print(to_text_code(message))
  elif choice == "3":
     print("Good Bye")
     break
  else:
     print("invalid input chosse 1,2 or 3")
