public class Project {

    // Attributes
    String projectName;
    String buildingType;
    String address;
    String deadline;
    int erfNumber;
    int projectNumber;
    float totalFee;
    float totalPaid;

    // Constructor
    public Project(
            String projectName,
            String buildingType,
            String address,
            String deadline,

            int erfNumber,
            int projectNumber,
            float totalFee,
            float totalPaid) {

        this.projectName = projectName;
        this.buildingType = buildingType;
        this.address = address;
        this.deadline = deadline;

        this.erfNumber = erfNumber;
        this.projectNumber = projectNumber;
        this.totalFee = totalFee;
        this.totalPaid = totalPaid;

    }

    // Method to dispaly the object is a string
    public String toString() {
        String output = "Project Details\nProject name: " + projectName;
        output += "\nBuilding type: " + buildingType;
        output += "\nAddress: " + address;
        output += "\nDeadline: " + deadline;
        output += "\nERF number: " + erfNumber;
        output += "\nProject number: " + projectNumber;
        output += "\nTotal Fee: " + totalFee;
        output += "\nTotal Paid: " + totalPaid;

        return output;
    }

    // Method to change the deadline of the project
    public void changeDeadline(String newDate) {
        this.deadline = newDate;
    }

    // Method to change the deadline of the project
    public void updatePaidFee(int newFee) {
        this.totalPaid = newFee;
    }
}
