
//Imports
import java.util.Scanner;

public class PoisedProject {
        // Declaring this here, so it can be used acrross multiple methods
        public static Project[] projectArray = {};
        public static Person[] PersonArray = {};
        public static Scanner menuChoiceScanner = new Scanner(System.in);

        public static Project createProject()
        // Allow a user to create a new project (This will be moved to its own method
        // during later capstone projects)
        // New Project name
        {
                Scanner newProjectName = new Scanner(System.in);
                System.out.println("Please enter a project name");
                String projectName = newProjectName.nextLine();
                // New Project type
                Scanner newProjectType = new Scanner(System.in);
                System.out.println("Please enter building type for that project");
                String projectType = newProjectType.nextLine();
                // New Project Address
                Scanner newProjectAddress = new Scanner(System.in);
                System.out.println("Please enter address for that project");
                String projectAddress = newProjectAddress.nextLine();
                // New Project Deadline
                Scanner newProjectDeadline = new Scanner(System.in);
                System.out.println("Please enter deadline for that project");
                System.out.println("Format should be DD/MM/YYYY");
                String projectDeadline = newProjectDeadline.nextLine();
                // New Project ERF
                Scanner newProjectERF = new Scanner(System.in);
                System.out.println("Please enter ERF Number for that project");
                int projectErf = newProjectERF.nextInt();
                // New Project number
                Scanner newProjectNumber = new Scanner(System.in);
                System.out.println("Please enter Project number for that project");
                int projectNumber = newProjectNumber.nextInt();
                // New Project total fee
                Scanner newProjectTotalFee = new Scanner(System.in);
                System.out.println("Please enter total fee for that project");
                int projectTotalFee = newProjectTotalFee.nextInt();

                // Create object with above details
                Project newProject = new Project(
                                projectName,
                                projectType,
                                projectAddress,
                                projectDeadline,
                                projectErf,
                                projectNumber,
                                projectTotalFee,
                                0);
                // Pritns out our new project
                System.out.println(newProject);
                // Closes our scanners
                newProjectName.close();
                newProjectType.close();
                newProjectAddress.close();
                newProjectDeadline.close();
                newProjectERF.close();
                newProjectNumber.close();
                newProjectTotalFee.close();
                // Returns our new project
                return newProject;

        }

        public static void addToProjectList(Project project) {
                // Method to add a "project" to our global array "projectArray"
                Project arrNew[] = new Project[projectArray.length + 1];
                // Creates a new array with +1 length, copies old array to new array, adds new
                // item to new array, and overwrites old array
                int i;
                for (i = 0; i < projectArray.length; i++) {
                        arrNew[i] = projectArray[i];
                }
                arrNew[i] = project;
                projectArray = arrNew;

        }

        public static void addToPersonList(Person person) {
                // Method to add a "person" to our global array "PersonArray"
                Person arrNew[] = new Person[PersonArray.length + 1];
                // Creates a new array with +1 length, copies old array to new array, adds new
                // item to new array, and overwrites old array
                int i;
                for (i = 0; i < PersonArray.length; i++) {
                        arrNew[i] = PersonArray[i];
                }
                arrNew[i] = person;
                PersonArray = arrNew;

        }

        public static void changeDate() {
                // Method to change the due date for a project
                // Lists possible projects to change
                System.out.println("Current active projects:");
                for (int i = 0; i < projectArray.length; i++) {
                        System.out.print(projectArray[i].projectName + ", ");
                }

                // Lets user pick the project that we want to edit from a list
                Scanner projectChoiceScanner = new Scanner(System.in);
                System.out.println("\nPlease enter a project name to change");
                String projectChoice = projectChoiceScanner.nextLine();

                // Lets user enter a new formatted date to input into selected project
                Scanner newDateScanner = new Scanner(System.in);
                System.out.println("Please enter a new date");
                System.out.println("Format must be DD/MM/YYYY");
                String newDate = newDateScanner.nextLine();

                // Goes through our list of projects. Finds the selected project. Uses the
                // "changeDeadline" method on that project.
                for (int i = 0; i < projectArray.length; i++) {
                        String tempName = projectArray[i].projectName;
                        if (tempName.equals(projectChoice)) {
                                projectArray[i].changeDeadline(newDate);
                                System.out.println(projectArray[i]);
                                break;
                        }
                }
                // Closes our scanners
                projectChoiceScanner.close();
                newDateScanner.close();
        }

        public static void changePaidFee() {

                // Gets user to pick a project to change
                Scanner projectChoice = new Scanner(System.in);
                System.out.println("Current active projects:");
                for (int i = 0; i < projectArray.length; i++) {
                        System.out.print(projectArray[i].projectName + ", ");
                }
                System.out.println("\nPlease enter a project name to change");
                String projectChoiceString = projectChoice.nextLine();

                // Gets user to input a new number
                Scanner newPaidFee = new Scanner(System.in);
                System.out.println("Please enter a Paid Fee number");
                System.out.println("Please only enter a number");
                int newPaidFeeString = newPaidFee.nextInt();

                // Finds the requested project in our list of prjects. Uses the ...
                // updatePaidFee() method to change the fee in that project
                for (int i = 0; i < projectArray.length; i++) {
                        String tempName = projectArray[i].projectName;
                        if (tempName.equals(projectChoiceString)) {
                                projectArray[i].updatePaidFee(newPaidFeeString);
                                System.out.println(projectArray[i]);
                                break;
                        } else {
                                System.out.println("That project does not exist");
                        }
                }
                // Closes scanners
                projectChoice.close();
                newPaidFee.close();
        }

        public static void changeContactDetails() {
                Scanner personScanner = new Scanner(System.in);
                System.out.println("Current Active Persons:");
                for (int i = 0; i < PersonArray.length; i++) {
                        System.out.print(PersonArray[i].name + ", ");
                }
                System.out.println("\nPlease enter a persons name to change");
                String Person = personScanner.nextLine();

                Scanner newEmailScanner = new Scanner(System.in);
                System.out.println("Please enter the new email");
                String newEmail = newEmailScanner.nextLine();

                Scanner newTellScanner = new Scanner(System.in);
                System.out.println("Please enter the new contact number");
                String newTell = newTellScanner.nextLine();

                for (int i = 0; i < PersonArray.length; i++) {
                        String tempName = PersonArray[i].name;
                        if (tempName.equals(Person)) {
                                PersonArray[i].updateContactDetails(newEmail, newTell);
                                System.out.println(PersonArray[i]);
                                break;
                        } else {
                                System.out.println("That project does not exist");
                        }
                }
                personScanner.close();
                newEmailScanner.close();
                newTellScanner.close();
        }

        public static void finalizeProject() {
                ;
        }

        public static void main(String[] args) {
                // Task Variables

                // Create test person
                Person jeff = new Person(
                                "Jeff",
                                "Ham",
                                "Builder",
                                "JeffHam@Builder.com",
                                "The road",
                                "123 456 7890");

                // Create test project
                Project TwoOneEight = new Project(
                                "218A",
                                "House",
                                "This is the address",
                                "29/08/2022",
                                182612,
                                218,
                                200000,
                                180000);
                // Create test project
                Project TwoOnenine = new Project(
                                "219C",
                                "House",
                                "This is the address",
                                "13/12/2024",
                                182612,
                                218,
                                200000,
                                180000);

                // Adding our test project to our array
                addToProjectList(TwoOneEight);
                addToProjectList(TwoOnenine);
                addToPersonList(jeff);

                // Test toString methods
                // Menu

                System.out.println("Welcome. ");
                System.out.println("1. Create a new project.");
                System.out.println("2. Changed the due date on a project.");
                System.out.println("3. Update the paid fee on a project.");
                System.out.println("4. Update a contractors contact details.");
                System.out.println("5. Finalize a project.");
                System.out.println("6. Exit.");
                // Get user choice
                System.out.println("Please enter a choice");
                int menuChoice = menuChoiceScanner.nextInt();
                // If choice == number, run a function for that choice
                if (menuChoice == 1) {
                        Project newProject = createProject();
                        addToProjectList(newProject);
                } else if (menuChoice == 2) {
                        changeDate();
                } else if (menuChoice == 3) {
                        changePaidFee();
                } else if (menuChoice == 4) {
                        changeContactDetails();
                } else if (menuChoice == 5) {
                        finalizeProject();
                } else if (menuChoice == 6) {
                        System.exit(0);
                }
                // Closes scanners
                menuChoiceScanner.close();
                menuChoiceScanner = null;
        }
}