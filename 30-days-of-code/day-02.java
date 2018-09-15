import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the solve function below.
    static int solve(double meal_cost, int tip_percent, int tax_percent) {
        double tip = (meal_cost * tip_percent) / 100;
        double tax = (meal_cost * tax_percent) / 100;

        return (int)Math.round(meal_cost + tip + tax);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        double meal_cost = scanner.nextDouble();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int tip_percent = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int tax_percent = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();

        int total = solve(meal_cost, tip_percent, tax_percent);

        System.out.println(String.format("The total meal cost is %d dollars.", total));

    }
}
