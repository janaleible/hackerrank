import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
   int divisorSum(int n);
}

class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        
        Set<Integer> divisors = new HashSet<Integer>();
        
        for (Integer i = 1; i <= n; i++) {
            if (n % i == 0) divisors.add(i);
        }
        
        return divisors.stream().mapToInt(i -> i).sum();
    }
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
      	AdvancedArithmetic myCalculator = new Calculator(); 
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}
