class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new_string += s[i]

        new_string = new_string.casefold()
        new_string = new_string.replace(" ", "")
        print(new_string)
        n = len(new_string)
        left = n - 1

        for right in range(len(new_string)):
            if new_string[right].isalnum():
                if new_string[right] != new_string[left]:
                    print(new_string[right], new_string[left])
                    return False

            left -= 1
        return True

