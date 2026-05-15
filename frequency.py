age = [21,13,14,15,15,14,15,13,12,17,18,17,18,15,16,16,15,13,12]
frequency = {}

for item in age :
    if item in frequency :
        frequency[item] += 1
    else :
        frequency[item] = 1

print("Frequency of age:-")
for key,value in frequency.items():
        print(key,':',value)