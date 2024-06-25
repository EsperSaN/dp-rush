num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
m_num = num1 * num2
print(f"{num1} x {num2} = {m_num}")
if m_num > 0 :
    print("The result is positive.")
elif m_num == 0 :
    print("The result is positive and negative")
elif m_num < 0:
    print("The result is negative")
else:
    print("error")