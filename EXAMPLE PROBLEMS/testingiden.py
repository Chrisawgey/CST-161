cd= float(input("input the cd amount: "))
digital= float(input("input the digital amount: "))
totalfordays= float(input("input how many days you renting it: "))

costforcd= cd * 5
costfordig= digital * 15

totalsum= costfordig + costforcd

renttime= totalsum + 2.00

print(f"this is the total sum for cd and digital {totalsum}")
print(f"this is the rent time total {renttime}")