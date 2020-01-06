# if else in Dictionary_Comprehension
# Dictionary : {key:(value if condition else condition) loop Condition}
even_odd = {num:("is even" if num % 2 == 0 else "is odd")for num in range(1,11)}
print(even_odd)
# Output : {1: 'is odd', 2: 'is even', 3: 'is odd', 4: 'is even', 5: 'is odd', 6: 'is even', 7: 'is odd', 8: 'is even', 9: 'is odd', 10: 'is even'}
