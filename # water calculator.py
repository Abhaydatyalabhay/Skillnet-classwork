# water calculator

total_bottles = int(input("enter the water bottle you have:"))
bottles_per_day = int(input("enter the bottle you have drinl water bottle per day:"))
 
day= 1
while total_bottles >0:
    if total_bottles >= bottles_per_day:
        print("Day {day}: Drank {bottle_per_day} bottles,{total_bottle - bottle_per_day}left.")
        total_bottles = bottles_per_day
    else:
        print("Day{day}: Drank {total_bottles} bottles(s).0 left")
        total_bottles = 0
        day +=1

    print("no more bottle present")