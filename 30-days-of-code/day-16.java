import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String string = in.next();
        
        try {
            int integer = Integer.parseInt(string);
            System.out.println(integer);
        } catch(NumberFormatException exception) {
            System.out.println("Bad String");
        }
    }
}
