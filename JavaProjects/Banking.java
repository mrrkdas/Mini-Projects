package JavaProjects;

import java.util.Scanner;


public class Banking {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Welcome to Rishab's Bank");
        System.out.println("Are you here to open account, withdraw, or deposit  (a/b/c)?");

        String decision = scan.nextLine();

        switch (decision) {
            case "a" : 
                System.out.println("Great lets get started with opening your account!!"); 
                break;
            case "b" : 
                System.out.println("Great, lets get started with the withdrawal process!!"); 
                break;
            case "c" : 
                System.out.println("Great, lets get started with the depositing process!!");
        }




    }
}

