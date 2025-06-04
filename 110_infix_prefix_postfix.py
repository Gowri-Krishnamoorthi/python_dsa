# 🔢 1. What Are These Notations?
# Notation	Format	Example for A + B
# Infix	Operator is between operands	A + B
# Prefix	Operator is before operands	+ A B
# Postfix	Operator is after operands	A B +

# 🧠 Why Use Prefix/Postfix?
# Infix is natural for humans but needs parentheses and operator precedence.

# Prefix/Postfix is easier for computers — no need for parentheses or operator precedence rules.

# 🔁 Conversion Techniques
# All conversions involve using stacks effectively.


# ✅ 2. Infix → Postfix (Shunting Yard Algorithm)
# Rules:
# Operands go directly to output.

# Operators go to a stack (pop based on precedence).

# Parentheses handled specially:

# Push '(',

# On ')', pop until '('.

def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = []

    for token in expression:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Example:
exp = "(A+B)*C"
print(infix_to_postfix(exp))  # Output: AB+C*


# ✅ 3. Infix → Prefix
# Trick: Reverse the infix expression, swap ( and ), convert to postfix, then reverse the result.

def infix_to_prefix(expression):
    def reverse_expr(expr):
        expr = expr[::-1]
        expr = ['(' if ch == ')' else ')' if ch == '(' else ch for ch in expr]
        return expr

    reversed_expr = reverse_expr(expression)
    postfix = infix_to_postfix(reversed_expr)
    return postfix[::-1]

# Example:
exp = "(A+B)*C"
print(infix_to_prefix(exp))  # Output: *+ABC

# ✅ 4. Postfix → Infix
# Use a stack:

# Push operands

# On operator: pop two operands, combine "(a op b)", push result back.

def postfix_to_infix(expression):
    stack = []
    for token in expression:
        if token.isalnum():
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a}{token}{b})")
    return stack[0]

# ✅ 5. Prefix → Infix
# Reverse process of Postfix → Infix.

def prefix_to_infix(expression):
    stack = []
    for token in reversed(expression):
        if token.isalnum():
            stack.append(token)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a}{token}{b})")
    return stack[0]

# Conversion	Approach
# Infix → Postfix	Shunting Yard (stack)
# Infix → Prefix	Reverse + postfix + reverse
# Postfix → Infix	Stack, combine a op b
# Prefix → Infix	Stack, reversed, combine a op b