import java.util.Scanner;

public class Hanoi {

    static int Hanoi (int num) {
        if (num == 1 || num == 2)
        {
            return 1;
        }
        else
        {
            return Hanoi(num-2) + Hanoi(num-1);
        }
    }

    public static void main(String[] args) {
        int output;
        Scanner reader = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = reader.nextInt();
        output = Hanoi (n);
        reader.close();
        System.out.println(output);
    }
}