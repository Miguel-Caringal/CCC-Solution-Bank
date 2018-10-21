import java.util.Scanner;

public class Factorial {

    static int factorial (int num) {
        if (num == 0)
        {
            return 1;
        }
        else
        {
            return num * factorial (num-1);
        }

    }

    public static void main(String[] args) {
        int output;
        Scanner reader = new Scanner(System.in);  // Reading from System.in
        System.out.println("Enter a number: ");
        int n = reader.nextInt(); // Scans the next token of the input as an int.
        output = factorial (n);
        reader.close();
        System.out.println(output);
    }
}
