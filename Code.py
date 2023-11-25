

product=('Leather wallet','Umberella','Cigarette','Honey')
unit= (1100,900,200,100)
gst=(18,12,28,0)
quant=(1,4,3,2)

basket={'Product':product,'Unit price in Rupees':unit, 'GST in %':gst, 'Quantity':quant}

total=0

for i in basket.values():
    
    price= unit[i]+unit[i]*gst[i]

    if unit[i]>500:
        price= unit[i]- unit[i]*.05
    
    total+=price
    
    maxgst= max(gst[i])

print(maxgst)
print(total)

        
        
    