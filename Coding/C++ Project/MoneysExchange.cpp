#include <iostream> 
using namespace std;

int main(){
    string choice;
    do {
        int option, amount;
        cout << "1. USD to Riel" << endl;
        cout << "2. Reil to USD" << endl;
        cout << "3. Reil to Bath" << endl;
        cout << "4. Bath to Reil" << endl;
        cout << "Enter your choice: " << endl;
        cin >> option;
        switch (option) {
            case 1: cout << "Enter amount in USD: ";
            cin >> amount; 
            cout << "Equivalent amount in Riel: " << amount * 4100 << " Reil\n"; break;
            case 2: cout << "Enter amount in Riel: ";
            cin >> amount;
            cout << "Equivalent amount in USD: $" << amount / 4100 << endl; break;
            case 3: cout << "Enter amount in Riel: ";
            cin >> amount;
            cout << "Equivalent amount in Baht: " << (amount / 10000) * 90 << " Baht/n"; break;
            case 4: cout << "Enter amount in Baht: ";
            cin >> amount;
            cout << "Equivalent amount in Riel: " << (amount / 90) * 10000 << " Riel\n"; break;
            default: cout << "Invalid option\n";
            }
        cout << "Do you want to perform another conversion? (yes/no): ";
        cin >> choice;
    }while(choice == "yes");
    cout << "Thank you for using the currency converter!\n";

    return 0;
}