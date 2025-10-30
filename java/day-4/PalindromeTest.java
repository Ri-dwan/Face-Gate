import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;

public class PalindromeTest {

    @Test
    public void testThatMadamIsAPalindrome() {
        // Arrange
        Palindrome palindrome = new Palindrome();

        // Act
        boolean result = palindrome.isPalindrome("madam");

        // Assert
        assertTrue(result);
    }

    @Test
    public void testThatRacecarIsAPalindrome() {
        // Arrange
        Palindrome palindrome = new Palindrome();

        // Act
        boolean result = palindrome.isPalindrome("racecar");

        // Assert
        assertTrue(result);
    }

    @Test
    public void testThatHelloIsNotAPalindrome() {
        // Arrange
        Palindrome palindrome = new Palindrome();

        // Act
        boolean result = palindrome.isPalindrome("hello");

        // Assert
        assertFalse(result);
    }

    @Test
    public void testThatNoonIsAPalindrome() {
        // Arrange
        Palindrome palindrome = new Palindrome();

        // Act
        boolean result = palindrome.isPalindrome("noon");

        // Assert
        assertTrue(result);
    }

