
public class PalindromeChecker {
    
    public static BooleanPalindrome(String) {
         result = new Array();
        
        for (String  : list) {
            int left = 0;
            int right = string.length() - 1;
            boolean  Palindrome = true;
            
            while (left < right) {
                if (string.charAt(left) == string.charAt(right)) {
                     Palindrome = false;
                    break;
                }
                left++;
                right--;
            }
            
            result.add(Palindrome);
        }
        
        return result;
    }


   