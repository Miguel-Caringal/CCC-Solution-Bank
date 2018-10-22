import java.util.Scanner;

public class fibonaciimemoized {

    static int fibonacii (int num, int data []) {
        int result;
        if (num == 1 || num == 2)
        {
            result = 1;
        }
        else
        {
            result = fibonacii(num-2, data) + fibonacii(num-1, data);
        }
        data[num-1] = result;
        return result;
    }

    public static void main(String[] args) {
        int output;
        Scanner reader = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = reader.nextInt();
        int data [] = new int [n+1];
        output = fibonacii (n,data);
        reader.close();
        System.out.println(output);
    }
}
