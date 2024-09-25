def is_valid_parentheses(s):
    brackets = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs:  
            top_element = brackets.pop() if brackets else '#'
            if pairs[char] != top_element:
                return False
        elif char in pairs.values():
            brackets.append(char)
    
    return not brackets

s = input("Enter a string of parentheses: ")
print(is_valid_parentheses(s))
