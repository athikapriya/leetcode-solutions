class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False

        special = "!@#$%^&*()-+"

        has_lower = has_upper = has_digit = has_special = False

        for i , char in enumerate(password):
            has_lower |= char.islower()
            has_upper |= char.isupper()
            has_digit |= char.isdigit()
            has_special |= char in special

            if i > 0 and char == password[i - 1]:
                return False

        return has_lower and has_upper and has_digit and has_special


'''
Time Complexity : O(n)
Space complexity: O(1)
'''