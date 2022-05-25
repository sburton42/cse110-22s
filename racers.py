from operator import index


racers = []
times = []

racers.append("Andy")
times.append(25)

racers.append("Chelsea")
times.append(22)

racers.append("Allison")
times.append(27)

for i in range(len(racers)): # 0, 1, 2
    person = racers[i]
    time = times[i]
    human_count = i + 1
    
    print(f"{human_count}. {person} - {time}")

item_to_remove = int(input("Which item do you want to remove? "))
index_to_remove = item_to_remove - 1

racers.pop(index_to_remove)
times.pop(index_to_remove)

for i in range(len(racers)): # 0, 1, 2
    person = racers[i]
    time = times[i]
    human_count = i + 1
    
    print(f"{human_count}. {person} - {time}")