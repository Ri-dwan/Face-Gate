import java.util.Scanner;

public class QuizGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Quiz Game");

        int score = 0;
        int total = 3;

        System.out.println("What is the capital of France?");
        System.out.println("1. Paris");
        System.out.println("2. London");
        System.out.println("3. Berlin");
        System.out.println("4. Rome");
        System.out.print("Your answer : ");
        int answer1 = scanner.nextInt();

        if (answer1 == 1) {
            System.out.println("Correct");
            score += 1;
        } else {
            System.out.println("Wrong");
        }
	

        System.out.println("Where is semicolon located?");
        System.out.println("1. Ikeja");
        System.out.println("2. Sabo Yaba");
        System.out.println("3. Yaba Sabo");
        System.out.println("4. Ikotun");
        System.out.print("Your answer : ");
        int answer2 = scanner.nextInt();

        if (answer2 == 2) {
            System.out.println("Nice");
            score += 1;
        } else {
            System.out.println("Fair");
        }
	

        System.out.println("What is the color of Nigeria Flag?");
        System.out.println("1. Green,White");
        System.out.println("2. White,Green");
        System.out.println("3. Green,Green");
        System.out.println("4. Green,White,Green");
        System.out.print("Your answer : ");
        int answer3 = scanner.nextInt();

        if (answer3 == 4) {
            System.out.println("Good");
            score += 1;
        } else {
            System.out.println("At this point I can't help you");
        }
	

 	System.out.println("You scored " + score + " out of " + total);

    }



}


