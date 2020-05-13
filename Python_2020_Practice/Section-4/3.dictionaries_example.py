item_catalog = {"CD Drive's": 7.99, "Hard Disk": 12.50, "Keyboard": 14.00}
# print item_catalog["Hard Disk"]
for x in item_catalog:
    print x

def exists_in(A,name):
    result = False
    for x in A:
        if x == name:
            result = True
    return result

# print exists_in(item_catalog,"Hard Disk")

exit_var = False
while exit_var == False:
    in_var = raw_input("Enter a product to look up the price (or press x to quit): ")
    if exists_in(item_catalog,in_var):
        print "The price of this item is:"
        print item_catalog[in_var]
    if exists_in(item_catalog,in_var) == False and in_var != "x":
        print "That item does not exists"
        print exists_in(item_catalog,"Hard Disk")
    if in_var == "x":
        exit_var = True
    
