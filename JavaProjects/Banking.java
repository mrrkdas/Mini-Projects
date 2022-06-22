package JavaProjects;

import java.util.Scanner;

public class Banking {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Welcome to Rishab's Bank");
        System.out.println("Are you here to open account, withdraw, or deposit  (a/b/c)?");

        String decision = scan.nextLine();

        if (decision.equals("a")) {
            // Opening account
            System.out.println("Great, let's get started openning your account");

        } else if (decision.equals("b")) {
            // Withdraw 
            System.out.println("You want to withdraw, great, let's get started");

        } else {
            // Deposit
            System.out.println("You want to deposit, great, let's get started");
        }




    }
}

