import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ReverserTest {

    @Test
    public void testReverseCase() {


        String result = Reverser.reverse("abcdefd");

        assertEquals(result, "dfedcba");
    }


    @Test
    public void testCharacterAtStart() {


        String result = Reverser.reverse("abcdef");
        assertEquals(result "abcdef");
    }

    @Test
    public void testCharacterAtEnd() {
        String result = Reverser.reverse("abcdef");
        assertEquals(result "fedcba");
    }
}


	
	