
test_list = ["madam", "racecar", "hello", "noon"]

def get_palindrome(list):
    result = []
    for string in list:
        left = 0
        right = len(string) - 1
        palindrome = True
        
        while left < right:
            if string[left] == string[right]:
                palindrome = False
                break
            left += 1
            right -= 1
        
        result.append(palindrome)
    
    return result


print(get_palindrome(test_list))
