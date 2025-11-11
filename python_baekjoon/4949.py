ans = []

while True:
    line = input()
    if line == ".":
        break
    stack = []
    flag = True
    for s in line:
        if s == "(":
            stack.append(s)
        elif s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    
    if flag and not stack:
        ans.append("yes")
    else:
        ans.append("no")
        

print("\n".join(ans))