print('THE AVG STOCK CALCULATOR')
a =int( input("enter no of stock:"))
b= int (input('what it is worth:'))
print("no of stock you own initially",a)
print( 'worth of your stock right now',b)     
c= int (input ('what is your budget now for buying today:'))
print ('your current budget too buy',c)
d= int (input('what is the price of stock:'))
print('price of the stock',d)
e= c/d
print('stock can be bought in the sum',e)
f=a+e
print('total no of stocks',f)
g=b+c
print( 'total sum of stocks',g)
h=g/f
print('Avg stock price ',h)