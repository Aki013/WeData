def rectangle(pligne, pcolonne, pchar):
    for i in range(0,pligne):
        text = ''
        for j in range(0,pcolonne):        
            text = text + pchar
        print(text)

input_1 = input()
int_1 = int(input_1.split(' ',1)[0])
int_2 = int(input_1.split(' ',1)[1])

rectangle(int_1,int_2,input())
