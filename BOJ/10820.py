import sys

while 1:
    try:
        string_input = input()
    
        list_answer = [0, 0, 0, 0]
        for s in string_input:
            if s == ' ':
                list_answer[3] += 1
    
            elif '0' <= s <= '9':
                list_answer[2] += 1
    
            elif 'a' <= s <= 'z':
                list_answer[1] += 1
    
            elif 'A' <= s <= 'Z':
                list_answer[0] += 1
    
    
        print("{} {} {} {}".format(list_answer[1], list_answer[0],
                                   list_answer[2], list_answer[3]))
        
        
    except EOFError: break


