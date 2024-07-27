# # Enter your code here. Read input from STDIN. Print output to STDOUT
# t= int(input())
# while t:
#     a= int(input())
#     b= int(input())
#     try:
#         print(a/b)
#     except ZeroDivisionError as e:
#         print(e)
#     except ValueError as VE:
#         print(VE)
#     t-=1
    

input_size = int(input())

for _ in range(input_size):
    try:
        numerator, denominator = map(int, input().split())
        print(numerator // denominator)
    except Exception as e:
        print("Error Code:", e)