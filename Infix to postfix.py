###########2. Convert an infix expression to a postfix expression.

def precedence(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*': 
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

# Function to perform infix to postfix conversion
def Postfix(expression):
    list = []
    postfix =[]
    for i in expression:
        if i.isalnum(): 
            postfix.append(i)
        elif i == '(': 
            list.append(i)
        elif i == ')':
            while  list[-1] != '(': 
                postfix.append(list.pop())
            list.pop()
        else:
            while list and (precedence(i) < precedence(list[-1]) or precedence(i) == precedence(list[-1])):
                postfix.append(list.pop())
            list.append(i)
    while list:
       postfix.append(list.pop())
    joined=''.join(postfix)
    return joined
exp = "a+b*(c^d-e)&^(f+g*h)-i"
print(exp)
print(Postfix(exp))
















# def prec(c):
#     if c == '^': return 3
#     elif c == '/' or c == '*': return 2
#     elif c == '+' or c == '-': return 1
#     else: return -1

# # Function to perform infix to postfix conversion
# def Postfix(expression):
#     list = []
#     result = ""
#     for i in range(len(expression)):
#         c = expression[i]
#         if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'): 
#             result += c
#         elif c == '(': 
#             list.append('(')
#         elif c == ')':
#             while list[-1] != '(': result += list.pop()
#             list.pop()
#         else:
#             while list and (prec(c) < prec(list[-1]) or prec(c) == prec(list[-1])):result += list.pop()
#             list.append(c)
#     while list: 
#         result += list.pop()
#     print(result)
# exp = "a+b*(c^d-e)&^(f+g*h)-i"
# Postfix(exp)










#def precedence(c):
#     if c == '^':
#         return 3
#     elif c == '/' or c == '*': 
#         return 2
#     elif c == '+' or c == '-':
#         return 1
#     else:
#         return -1

# # Function to perform infix to postfix conversion
# def Postfix(expression):
#     list = []
#     postfix =[]
#     for i in expression:
#         if i.isalnum(): 
#             postfix.append(i)
#         elif i == '(': 
#             list.append(i)
#         elif i == ')':
#             while  list[-1] != '(': 
#                 postfix.append(list.pop())
#             list.pop()
#         else:
#             while list and (precedence(i) < precedence(list[-1]) or precedence(i) == precedence(list[-1])):
#                 postfix.append(list.pop())
#             list.append(i)
#     while list:
#        postfix.append(list.pop())
#     joined=''.join(postfix)
#     return joined
# exp = "a+b*(c^d-e)&^(f+g*h)-i"
# print(exp)
# print(Postfix(exp))

