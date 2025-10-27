
import java.util.Scanner;
import java.util.Random;

public class SubtractionGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Welcome Simple Arithmeti GameApp!");
        int score = 0;

        for (int count = 1; count <= 10; count++) {
            int number1 = random.nextInt(20);
            int number2 = random.nextInt(number1 + 1);
	   

            System.out.println("Question: What is " + number1 + " - " + number2 + "?");
	    }
            for (int i = 1; i <= 2; i++) {
                System.out.print("Your answer: ");
                int answer = scanner.nextInt();
		}
                if (answer == number1 - number2) {
                    System.out.println("Correct!");
                    score++;
                }else {
                    System.out.println("Try again");
                    System.out.println("Game Over! You got " + score + " out of 10 correct.");
            }
 
    }
}