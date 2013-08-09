import java.util.Scanner;
public class Primes {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter n for the nth prime to be calculated: ");
        int n = scanner.nextInt();
        int counter = 1;
        int[] primes = new int[n];
        primes[0] = 2;
        for (int i = 3; counter < n; i+=2) {
            for (int m = 0; m < counter; ++m) {
                if (i % primes[m] == 0) break;
                if (i/primes[m] <= primes[m]) {
                    primes [counter++] = i;
                    break;
                }
            }
        }
        System.out.println("The " + n + "th prime is: " + primes[n-1]);
    }
}
