package kahootPackage;

import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class kahootJAVA {

    public static void main(String[] args) {
        // Create a scanner to read input from the user
        Scanner scanner = new Scanner(System.in);
        // Create a HashMap to store the domains and their counts
        HashMap<String, Integer> domainCounts = new HashMap<>();
        
        System.out.println("Enter email addresses (type 'done' to stop):");

        while (true) {
            String email = scanner.nextLine();  // Read the next email
            if (email.equals("done")) {  // Stop if the user types "done"
                break;
            }
            String domain = getDomain(email);  // Get the domain from the email
            if (!domain.isEmpty()) {
                // Increment the count for this domain in the HashMap
                if (domainCounts.containsKey(domain)) {
                    domainCounts.put(domain, domainCounts.get(domain) + 1);
                } else {
                    domainCounts.put(domain, 1);
                }
            }
        }

        // Print the top domains
        for (Map.Entry<String, Integer> entry : domainCounts.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }

    // A simple method to extract the domain from an email
    public static String getDomain(String email) {
        int atIndex = email.indexOf('@');
        if (atIndex != -1 && atIndex < email.length() - 1) {
            return email.substring(atIndex + 1);  // Get the part after '@'
        } else {
            return "";  // Return empty string if no '@' is found
        }
    }
}

