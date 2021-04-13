check = sum(code[i] if i%2 else code[i]*3 for i in range(8))
result = 0 if check % 10 else sum(code)
print(result)