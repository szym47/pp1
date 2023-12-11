def f(player1,player2):
    p1= dict()
    for i in player1:
        if i in ('A','K','Q','J','T'):
            p1[i] =p1.get(i,0)+10
        else:
            p1[i] =p1.get(i,0)+int(i)
    p2= dict()
    for j in player2:
        if j=='A' or j=='J' or j=='K' or j=='Q' or j=='T':
            p2[j] =p2.get(j,0)+10
        else:
            p2[j] =p2.get(j,0)+int(j)
    if sum(list(p1.values()))>=sum(list(p2.values())):
        print('True')
    else:
        print('False')
f("AJ972","AQT72") 
f("9532","K8") 
