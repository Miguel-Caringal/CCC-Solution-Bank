import java.util.Scanner;

public class fibonacii {

    static int fibonacii (int num) {
        if (num == 1 || num == 2)
        {
            return 1;
        }
        else
        {
            return fibonacii(num-2) + fibonacii(num-1);
        }
    }

    public static void main(String[] args) {
        int output;
        Scanner reader = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = reader.nextInt();
        output = fibonacii (n);
        reader.close();
        System.out.println(output);
    }
}
