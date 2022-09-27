// We can use this person object to created 
// architects, contractors or customers using the "type" attribute

public class Person {

    // Attributes
    String name;
    String surname;
    String type;
    String email;
    String physicalAddress;
    String tellNum;

    // Constructor
    public Person(String name,
            String surname,
            String type,
            String email,
            String physicalAddress,
            String tellNum) {

        this.name = name;
        this.surname = surname;
        this.type = type;
        this.email = email;
        this.physicalAddress = physicalAddress;
        this.tellNum = tellNum;
    }

    // Method to update contact details
    public void updateContactDetails(String newEmail, String newTell) {
        this.email = newEmail;
        this.tellNum = newTell;
    }

    // Method to dispaly object as a string
    public String toString() {
        String output = "Name: " + name + " " + surname;
        output += "\nType: " + type;
        output += "\nEmail: " + email;
        output += "\nPhysical Address: " + physicalAddress;
        output += "\nContact number: " + tellNum;

        return output;
    }
}
