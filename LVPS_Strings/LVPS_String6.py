def main():
    #declaração de variavel
    mes = str("")
    mes_num = int(0)
    data_de_nascimento = str("")
    #recebimento de variavel
    data_de_nascimento = input()
    
    if data_de_nascimento[3:5] == "08":
        mes = 'de agosto de'
        print(f"{data_de_nascimento[0:2]} {mes} {data_de_nascimento[6:10]}")
       
        
    
    
    
    
    
if __name__ == "__main__":
    main()