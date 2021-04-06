iterms = []
print ("-----welcome to our supermarket------")
print (" 1. View iterms \n 2. Add iterms \n 3. Purchase iterms \n 4. Search iterms")
choice = int(input("please enter the number of your choice:   "))

if choice == 1:
    print("----view iterms----")
    print("the number of iterms in the inventory are %d: " %len(iterms))
    if len(iterms) !=0:
        print("here are all the iterms available in the supermarket")

        for iterm in iterms:
            for key, value in iterm.iterms():
                print(" %s : %S" %(key, value) )
elif choice ==2:
    print("------add iterms-------")
    print("to add an iterm fill in the form")

    iterm={}
    iterm["name"] = input("iterm name:  ")

    while True:
        try:
            iterm["quantity"]=int(input("enter the iterm: "))
            break
        except ValueError:
                print("iterm must be a digit")
                

    while True: 
        try:
            iterm["Price"] = int(input("please enter a price$:  "))
            print("iterms are successfully added")
            iterms.append(iterm)
            print(iterms)
            break
            
        except ValueError:
            print(" price should be only in digitd ")
        #print("iterms are successfully added")
        #iterms.append(iterm)
        #print(iterms)