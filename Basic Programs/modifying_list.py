mob_brands = ['apple', 'oneplus', 'vivo', 'xiaomi', 'samsung']
mob_brands[0] = 'nothing'
print(mob_brands)

mob_brands = ['apple', 'oneplus', 'vivo', 'xiaomi', 'samsung']
mob_brands.append('oppo')
print(mob_brands)

mob_brands = ['apple', 'oneplus', 'vivo', 'xiaomi', 'samsung']
mob_brands.insert(0,  'lava')
print(mob_brands)

mob_brands = ['apple', 'oneplus', 'vivo', 'xiaomi', 'samsung', 'spice']
print(mob_brands)
popped_brand = mob_brands.pop()
print(mob_brands)
print(popped_brand)

mob_brands = ['apple', 'oneplus', 'vivo', 'xiaomi', 'samsung', 'spice']
first_owned = mob_brands.pop(5)
print(f"The First mobile phone I owned was of {first_owned.title()}. ")

mob_brands = ['apple', 'oneplus', 'vivo', 'xiaomi', 'samsung']
mob_brands.extend(['nothing', 'cmf phone', 'huawei'])
print(mob_brands)

mob_brands = ['apple', 'oneplus', 'vivo', 'xiaomi', 'samsung']
mob_brands.remove('apple')
print(mob_brands)