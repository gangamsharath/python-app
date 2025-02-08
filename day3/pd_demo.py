import pandas as pd
data={'apple':[3,2,0,1],'orange':[0,3,7,2]}
purchases=pd.DataFrame(data)
print(purchases)
purchases=pd.DataFrame(data,index=['Pramod','Kumar','Somesh','Kiran'])
print(purchases.tail(2))
print(purchases.head(2))
print(purchases)
#print(purchases.loc('Prmaod'))
print(purchases.shape)