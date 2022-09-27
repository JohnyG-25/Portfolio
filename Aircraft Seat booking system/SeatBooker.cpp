// Imports/includes
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;

// Creating each flight
// Created here to make them global.

// 2D array for flight 1
string flight_1[6][6] = {{"A1", "A2", "A3", "A4", "A5", "A6"},
                         {"B1", "B2", "B3", "B4", "B5", "B6"},
                         {"C1", "C2", "C3", "C4", "C5", "C6"},
                         {"D1", "D2", "D3", "D4", "D5", "D6"},
                         {"E1", "E2", "E3", "E4", "E5", "E6"},
                         {"F1", "F2", "F3", "F4", "F5", "F6"}};
// 2D array for flight 2
string flight_2[6][6] = {{"A1", "A2", "A3", "A4", "A5", "A6"},
                         {"B1", "B2", "B3", "B4", "B5", "B6"},
                         {"C1", "C2", "C3", "C4", "C5", "C6"},
                         {"D1", "D2", "D3", "D4", "D5", "D6"},
                         {"E1", "E2", "E3", "E4", "E5", "E6"},
                         {"F1", "F2", "F3", "F4", "F5", "F6"}};
// etc
string flight_3[6][6] = {{"A1", "A2", "A3", "A4", "A5", "A6"},
                         {"B1", "B2", "B3", "B4", "B5", "B6"},
                         {"C1", "C2", "C3", "C4", "C5", "C6"},
                         {"D1", "D2", "D3", "D4", "D5", "D6"},
                         {"E1", "E2", "E3", "E4", "E5", "E6"},
                         {"F1", "F2", "F3", "F4", "F5", "F6"}};

string flight_4[6][6] = {{"A1", "A2", "A3", "A4", "A5", "A6"},
                         {"B1", "B2", "B3", "B4", "B5", "B6"},
                         {"C1", "C2", "C3", "C4", "C5", "C6"},
                         {"D1", "D2", "D3", "D4", "D5", "D6"},
                         {"E1", "E2", "E3", "E4", "E5", "E6"},
                         {"F1", "F2", "F3", "F4", "F5", "F6"}};

string flight_5[6][6] = {{"A1", "A2", "A3", "A4", "A5", "A6"},
                         {"B1", "B2", "B3", "B4", "B5", "B6"},
                         {"C1", "C2", "C3", "C4", "C5", "C6"},
                         {"D1", "D2", "D3", "D4", "D5", "D6"},
                         {"E1", "E2", "E3", "E4", "E5", "E6"},
                         {"F1", "F2", "F3", "F4", "F5", "F6"}};

vector<string> tickets;

string getdetails()
{
    // Function to get the full name of user using the system
    string f_name, s_name;
    // Get user name input
    cout << "Enter your first name" << endl;
    cin >> f_name; // Get user input from the keyboard
    cout << "Enter your surname" << endl;
    cin >> s_name; // Get user input from the keyboard
    return f_name + " " + s_name;
}

int selectflight()
{
    // Function to allow user to select a flight
    int choice;
    string output;
    output += "\nThe available travel times for flights are\n";
    output += "  \tArrive\tDepart\n";
    output += "1.\t7:00\t9:30\n";
    output += "2.\t9:00\t11:30\n";
    output += "3.\t11:00\t13:30\n";
    output += "4.\t13:00\t15:30\n";
    output += "5.\t15:00\t17:30\n";
    output += "Choose the time by entering the option number from the displayed list";

    while (true)
    {
        cout << output << endl;
        cin >> choice; // Get user input from the keyboard
        // If statement to check if question is valid
        if ((choice == 1) || (choice == 2) || (choice == 3) || (choice == 4) || (choice == 5))
        {
            return choice;
            break;
        }
        else
        {
            cout << "\nPlease make sure you enter a valid choice.\n\n\n";
        }
    }

    return choice;
}

void pickaseat(string array[6][6], int flightnumber)
{

    // Function to allow user to choose a seat
    string output;
    output += "\tFirst class\n";
    for (int i = 0; i < 6; i++)
    {
        output += "|";
        for (int j = 0; j < 6; j++)
        {
            output += array[i][j];
            output += "|";
            if (j == 2)
            {
                output += "\t|";
            }
        }
        if (i == 2)
        {
            output += "\n\tEconomy class";
        }
        output += "\n";
    }
    cout << output << endl;

    string rowchoice;
    int seatchoice;

    int rownumber;
    while (true)
    {
        while (true)
        {
            cout << "Please pick a row by entering just the letter" << endl;
            cin >> rowchoice;
            if ((rowchoice == "A") || (rowchoice == "B") || (rowchoice == "C") || (rowchoice == "D") || (rowchoice == "E") || (rowchoice == "F"))
            {
                if (rowchoice == "A")
                {
                    rownumber = 0;
                }
                else if (rowchoice == "B")
                {
                    rownumber = 1;
                }
                else if (rowchoice == "C")
                {
                    rownumber = 2;
                }
                else if (rowchoice == "D")
                {
                    rownumber = 3;
                }
                else if (rowchoice == "E")
                {
                    rownumber = 4;
                }
                else if (rowchoice == "F")
                {
                    rownumber = 5;
                }

                break;
            }
            else
            {
                cout << "That is not a valid row. " << endl;
            }
        }

        cout << "Please pick a seat number by entering just the number" << endl;
        cin >> seatchoice;

        if (array[rownumber][seatchoice - 1] == "**")
        {
            cout << "That seat is already taken. Please choose another seat" << endl;
        }
        else
        {
            array[rownumber][seatchoice - 1] = "**";
            string ticketname = rowchoice + to_string(seatchoice);
            cout << "Ticket " << ticketname << " Has been booked" << endl;
            tickets.push_back(to_string(flightnumber));
            tickets.push_back(ticketname);
            break;
        }
    }
}

void displaytickets(string name)
{
    // Function to display each ticket
    for (int i = 0; i < tickets.size(); i = i + 2)
    {
        string output;
        output += "\n\n------------------------------------------------------\n";
        output += "Ticket booked to ";
        output += name + "\n";
        output += "\nGate ";
        output += tickets[i] + "\n";
        if (tickets[i] == "1")
        {
            output += "Departure time is 7:00\n";
            output += "Arrival time is 9:30\n";
        }
        else if (tickets[i] == "2")
        {
            output += "Departure time is 9:00\n";
            output += "Arrival time is 11:30\n";
        }
        else if (tickets[i] == "3")
        {
            output += "Departure time is 11:00\n";
            output += "Arrival time is 13:30\n";
        }
        else if (tickets[i] == "4")
        {
            output += "Departure time is 13:00\n";
            output += "Arrival time is 15:30\n";
        }
        else if (tickets[i] == "5")
        {
            output += "Departure time is 15:00\n";
            output += "Arrival time is 17:30\n";
        }
        output += "\nSeat number ";
        output += tickets[i + 1];
        output += "\n------------------------------------------------------";
        cout << output << endl;
    }
}

void displayflight(int flightnumber)
{
    // Function to display available seats dependant on the chosen fligth

    if (flightnumber == 1)
    {
        pickaseat(flight_1, 1);
    }
    else if (flightnumber == 2)
    {
        pickaseat(flight_2, 2);
    }
    else if (flightnumber == 3)
    {
        pickaseat(flight_3, 3);
    }
    else if (flightnumber == 4)
    {
        pickaseat(flight_4, 4);
    }
    else if (flightnumber == 5)
    {
        pickaseat(flight_5, 5);
    }
}

void viewalltickets()
{
    // Function to count all tickets for each flight.
    string output;
    for (int i = 1; i <= 5; i++)
    {
        int tempcount = 0;
        output += "There are a total of ";
        for (int j = 0; j < tickets.size(); j = j + 2)
        {
            if (tickets[j] == to_string(i))
            {
                tempcount = tempcount + 1;
            }
        }
        output += to_string(tempcount);
        output += " For flight number " + to_string(i) + "\n";
    }
    cout << output << endl;
}

void bookaticket(string name)
{
    // Runs function to select a flight
    int selectedflight = selectflight();
    displayflight(selectedflight);
}

void menu(string name)
{
    // Function to display the main menu
    string output;
    int choice;
    cout << "\n\nHello " + name + "." << endl;
    output += "Please select one of the following by entering only a number\n";
    output += "(1) Book a ticket\n";
    output += "(2) View my tickets\n";
    output += "(3) Get count of all tickets\n";
    output += "(4) Exit\n";

    while (true)
    {

        cout << output << endl;
        cin >> choice;

        if (choice == 1)
        {
            // Book a ticket
            bookaticket(name);
        }
        else if (choice == 2)
        {
            // View my tickets
            displaytickets(name);
        }
        else if (choice == 3)
        {
            // Get count of all tickets
            viewalltickets();
        }
        else if (choice == 4)
        {
            // Exit
            break;
        }
        else
        {
            cout << "That is not a valid choice. Please try again." << endl;
        }
    }
}

int main()
{
    // Runs getdetails function to return details of user using system
    string name;
    name = getdetails();
    // Runs main menu
    menu(name);
}
