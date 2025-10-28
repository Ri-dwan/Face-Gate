
import java.util.Scanner;

public class Depreciation {
	public static void main(String[] args) {
        double fixedPrice = 50000;
        double depreciationRate = 0.08;

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of years: ");
        int years = scanner.nextInt();
        double finalValue = calculateDepreciation(fixedPrice, years, depreciationRate);
        System.out.printf("After %d years, the value is: %.2f\n", years, finalValue);
    }
}
    
















































































