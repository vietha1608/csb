def simplifyPath(path: str) -> str:
    stack = []
    parts = path.split('/')
    
    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    
    return '/' + '/'.join(stack)
path = "/home/"
parts = ['', 'home', '']
stack = ['home']
path = "/home//directory"
parts = ['', 'home', '', 'directory']
stack = ['home', 'directory']