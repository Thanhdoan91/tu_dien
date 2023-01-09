
dictionary_db = { 
    "Cá":"Fish",
    "Thỏ":"Rabbit",
    "Rùa":"Turtle",
    "Cây":"Tree",    
}

def display_word(dictionary_db, input_word):
    for key in dictionary_db.keys():
        if key == input_word:
            return dictionary_db[key]
        
while True:    
    input_word = input("Nhập từ cần dịch: ")
    translate_word = display_word(dictionary_db, input_word)
    print(translate_word)
    y_o_n = input("Bạn muốn tiếp tục [Y/N]?: ")
    if y_o_n.upper() == "N":
        break
        
