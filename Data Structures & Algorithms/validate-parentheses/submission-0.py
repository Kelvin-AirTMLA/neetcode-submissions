class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = dict()
        parenthesis_map["("] = ")"
        parenthesis_map["{"] = "}"
        parenthesis_map["["] = "]"

        stack = []
        
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in parenthesis_map:
                stack.append(char)
            else:
                # It's a closing bracket
                # Check if stack is empty or if it doesn't match
                if not stack or parenthesis_map[stack[-1]] != char:
                    return False
                # If it matches, pop the opening bracket from stack
                stack.pop()
        
        # Stack should be empty if all brackets are matched
        return len(stack) == 0
