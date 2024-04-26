# Example-5: Categorize as "Even" or "Odd"

categories = []
for x in range(10):
    if x % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")

print(categories)



# Using list comprehension 
categ2 = ["Even" if x%2 ==0 else "Odd" for x in range(10)]

print(categ2)