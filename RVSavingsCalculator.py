__author__ = 'Nick'


PriceOfRV=7000
HypotheticalRent=1800
HypotheticalRoomateRent=int(HypotheticalRent/2)

Rent=800
PropaneCostsMonthly=25
months=14
costs=[{'name':'Fantastic Vent','price':330},
        {'name':'Fantastic Vent','price':330},
        {'name':'Fridge','price':150},
        {'name':'Clothes Rod','price':25},
        {'name':'nothing','price':0},
]

HypotheticalRentTotal = HypotheticalRent*months

HypotheticalRoomateRentTotal = HypotheticalRoomateRent * months


ActualRentTotal=Rent*months
ActualRentTotal=(ActualRentTotal+PriceOfRV)


print 'saved if I had my own apt: '+ '${:,.2f}'.format(HypotheticalRentTotal-ActualRentTotal) + 'at ' + str(HypotheticalRent-Rent)  +'\mo'
print 'saved if I lived with roomate: ' '${:,.2f}'.format(HypotheticalRoomateRentTotal-ActualRentTotal)