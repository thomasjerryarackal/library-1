dic={}
listk=[]
n=int(input("enter the limit"))
for i in range (n):
	a=input("enter the title name:")
	n=input("enter the copies:")
	b=input("enter the publisher :")
	listk=[a]+[b]
	c=tuple(listk)
	dic[c]=n
print(dic)
i=input("enter add - to add the books or remove-to remove the book")
e=[]
if (i=="add"):
	q=input("enter the title to add:")
	w=input("enter the author:")
	new=[q]+[w]
	y=tuple(new)
	t=int(input("enter the numbers"))
	dic[y]=dic[y]+t
print(dic)
else:
	
	q=input("enter the title to add:")
	w=input("enter the author:")
	new=[q]+[w]
	y=tuple(new)
	t=int(input("enter the numbers"))
	dic[y]=dic[y]-t
print(dic)
