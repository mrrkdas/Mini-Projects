package JavaProjects;

import java.util.Scanner;

import javax.swing.event.SwingPropertyChangeSupport;


public class Banking {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Welcome to Rishab's Bank");
        System.out.println("Are you here to open account, withdraw, or deposit  (a/b/c)?");

        String decision = scan.nextLine();

        switch (decision) {
            case "a" : 
                System.out.println("\nGreat lets get started with opening your account!!"); 
                // Age
                System.out.println("\n Enter your age: ");
                int age = scan.nextInt();

                if (age >= 18) {
                    // Phone Number
                    System.out.println("\nEnter Phone Number: ");
                    scan.nextLine();
                    String phoneNumber = scan.nextLine();

                    // Name and DOB
                    System.out.println("\nEnter your Full Name and DOB");
                    String fullName = scan.nextLine();
                    String DOB = scan.nextLine();

                    // Social Security
                    System.out.println("\nFinally, enter your social security number");
                    long socialSecurityNumber = scan.nextLong();

                    // Username 
                    System.out.println("\nGreat, now lets create a username!!");
                    scan.nextLine();
                    String username = scan.nextLine();

                    // Password 
                    System.out.println("\nGreat!! Now last step, enter a password");
                    String password = scan.nextLine();

                    //Re-check password
                    System.out.println("\nRe-enter password to varify: ");
                    String varifiedPassword = scan.nextLine();

                    if (varifiedPassword.equals(password)) {
                        System.out.println("\nIs the following correct? (yes/no)");
                        // Print the info
                        System.out.println("Age" + age);
                        System.out.println("Phone Number" + phoneNumber);
                        System.out.println("Full Name" + fullName);
                        System.out.println("Date of Birth" + DOB);
                        System.out.println("Social Security Number" + socialSecurityNumber);
                        System.out.println("Username" +  username);
                        System.out.println("Password" + password);

                        String correctOrNot = scan.nextLine();

                        if (correctOrNot.equals("yes")) {
                            System.out.println("Congrats on creating your bank account");
                        } else {
                            System.out.println("Sorry, you will have to do this process again if something is wrong");
                        }




                    } else {
                        System.out.println("Your passwords are not the same, you will have to do this process again. Sorry!!");
                    }




                } else {
                    System.out.println("We currently don't serve bank accounts for minors, sorry");
                }
                break;
            case "b" : 
                System.out.println("\nGreat, lets get started with the withdrawal process!!"); 
                break;
            case "c" : 
                System.out.println("\nGreat, lets get started with the depositing process!!");
        }


    }
}

