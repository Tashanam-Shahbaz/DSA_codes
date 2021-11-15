import operator


class mystack:
    def __init__(self):
        self.elements = list()

    def isEmpty(self):
        return len(self.elements) == 0

    def pop(self):
        assert not self.isEmpty(), "Empty stack!"
        x = self.elements.pop()
        return x

    def push(self, value):
        self.elements.append(value)


def eval_postfix():
    post_list = input("Enter postfix Expression separated by space ")
    post_list = post_list.split(" ")
    print("The Postfix expression you have enter is : ", *post_list, sep=' ')
    stack = mystack()
    operators = {"^": pow, "*": operator.mul, "/": operator.truediv, "+": operator.add, "-": operator.sub}
    for x in post_list:
        if x in list(operators.keys()):
            T = int(stack.pop())
            NT = int(stack.pop())
            res = operators[x](NT, T)
            stack.push(res)
        else:
            stack.push(x)
    print(stack.elements)
    return stack.elements.pop()


print("RESULT :", eval_postfix())

##ALGORITHUM A8.2
def precedence(x):
    if x == '[' or x == '{' or x == '(':
        return 0
    if x == '+' or x == '-':
        return 1
    if x == '*' or x == '/':
        return 2
    return 3  # highest precedence is of ^


def aishigherthanb(a, b):
    return precedence(a) > precedence(b)


def infixtopostfix(expr):
    st = mystack()
    postfix = list()
    for i in range(len(expr)):
        token = expr[i]
        if token == '[' or token == '{' or token == '(':
            st.push(token)
        elif token == ']' or token == '}' or token == ')':
            done = False
            while not done:
                if not st.isEmpty():
                    top = st.pop()
                    if top == '[' or top == '{' or top == '(':
                        done = True
                    else:
                        postfix.append(top)
                else:
                    done = True
        elif token == '^' or token == '*' or token == '/' or token == '+' or token == '-':
            done = False
            while not done:
                if st.isEmpty():
                    st.push(token)
                    done = True
                else:
                    top = st.pop()
                    if aishigherthanb(token, top):
                        st.push(top)
                        st.push(token)
                        done = True
                    else:
                        postfix.append(top)
        else:
            postfix.append(token)
    while not st.isEmpty():
        top = st.pop()
        postfix.append(top)
    return postfix


Infix = ["8","+","9","-","(","5","-","2",")","*","(","(","1","-","7",")","+","4",")","/","2"]
Postfix = infixtopostfix(Infix)
print("postfix=", Postfix)
