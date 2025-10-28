import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class DepreciationTest{

	
	@Test
	public void testThatDepreciation(){
	// Arrange

	Deprecion = new Depreciation();

	// Act
	int result = library.totalNumberOfBooks();

	//Assert
	assertEquals(result, 0);
	}


	@Test
	public void testThatOneBookIsAddedToTheLibraryAndTheTotalNumberOfBooksIsOne(){
