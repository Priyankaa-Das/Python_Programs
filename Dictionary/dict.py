'''d={"sonam":1,"subham":2,3:[10,20,30],4:{5:'a',6:'b'}}

print(d)                        #{'sonam': 1, 'subham': 2, 3: [10, 20, 30], 4: {5: 'a', 6: 'b'}}
print(d['sonam'])               #1
print(d[3])                     #[10, 20, 30]
print(d[3][0])                  #10
print(d[4])                     #{5: 'a', 6: 'b'}                
print(d[4][5])                  #a

print(d.keys())                 #dict_keys(['sonam', 'subham', 3, 4])   "Returns all the keys"
print(d.values())               #dict_values([1, 2, [10, 20, 30], {5: 'a', 6: 'b'}])    "Returns all the values"
print(d.items())                #dict_items([('sonam', 1), ('subham', 2), (3, [10, 20, 30]), (4, {5: 'a', 6: 'b'})])"Returns all keys and values"

d[3]='Priyanka'                 #changing the value of key 3
print(d)                        #{'sonam': 1, 'subham': 2, 3: 'Priyanka', 4: {5: 'a', 6: 'b'}}
d[5]='Puja'                     #for adding new value to the dictionary
print(d)                        #{'sonam': 1, 'subham': 2, 3: 'Priyanka', 4: {5: 'a', 6: 'b'}, 5: 'Puja'}

d={}                            #making n
d=dict()
d[1]='puja'
d[2]='xoxo'
d[3]='Will'
print(d.items())                #dict_items([(1, 'puja'), (2, 'xoxo'), (3, 'Will')])

#d=dict(name='abc',roll=13)
r=[1,2,3,4,5,6]
n=['a','b','c','d','e','f']
d=dict(zip(r,n))
print(d)                        #{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}

for i in d.keys():
    print(i)                    #1
    
for i in d.values():
    print(i)                    #a\nb\nc\nd
    
for i in d.items():
    print(i)                    #(1, 'a')\n(2, 'b')\n(3, 'c')\n(4, 'd')\n(5, 'e')\n(6, 'f')
    
    
score={'pl1':100,'pl2':80,'pl3':72,'pl4':85,'pl5':130,'pl6':102}
sum=0
max=0

for i in score.values():
    sum=sum+i
    if i>max:
        max=i 
print(sum)                       #569
print(max)                       #130

for i in score.keys():
    if max not in score.keys():
        max=i
    else:
        if score[i] > score[max]:
            max=i
print(max)                        #pl5'''

'''i1={'p1':20,'p3':60,'p4':32}
i2={'p1':38,'p2':52,'p3':40}
i3={'p1':35,'p3':40,'p4':25}

d={}
for i in i1.keys():
    d[i]=i1[i]
print(d)                            # {'p1': 20, 'p3': 60, 'p4':32}
#for adding the values of players playing innings 1 and 2 from dictinary d and i2
for i in i2.keys():
    if i in d.keys():
        d[i]=d[i]+i2[i]
    else:
        d[i]=i2[i]           
print(d)                            #{'p1': 58, 'p3': 100, 'p4': 32, 'p2': 52}
# for adding the values of player inning 1 ,2 and 3 
for i in i3.keys():
    if i in d.keys():
        d[i]=d[i]+i3[i]
    else:
        d[i]=i3[i]
print(d)                            # {'p1': 93, 'p3': 140, 'p4': 57, 'p2': 52}'''


t1={'p1':30,'p2':40,'p3':35}
t2={'p4':70,'p5':25,'p6':28,'p7':12}
t3={'p8':60,'p9':35,'p10':40}
#Creating a new dictionary with the name of the players along with the player who scored the highest with their score
d1={}
max=0
for i in t1.keys():
    if max not in t1.keys():
        max=i
    else:
        if t1[i] > t1[max]:
            max=i
            p1=i
            d1[i]=max  
print(d1)
for i in t2.keys():
    if max not in t2.keys():
        max=i
    else:
        if t2[i] > t2[max]:
            max=i
            p1=i
            d1[i]=max
print(d1)  
for i in t3.keys():
    if max not in t3.keys():
        max=i
    else:
        if t3[i] > t3[max]:
            max=i
            p1=i
            d1[i]=max
print(d1)  
