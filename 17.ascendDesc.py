Dict={'Carl':40,'james':50,'bob':30,'danny':45}

asc_orders = sorted(Dict.items(), key=lambda x: x[1])
print('Ascending order is',asc_orders)

desc_orders = sorted(Dict.items(), key=lambda x: -x[1])
print('Descending order is',desc_orders)
