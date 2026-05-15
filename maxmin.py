num = [90,67,100,4,3,56,66,23]
max_val = num[0]
min_val = num[0]
for i in num:
     if i >= max_val:
        max_val = i
     if i <= min_val:
            min_val = i
            
print("Maximum number is", max_val)
print("Minimum number is", min_val)

