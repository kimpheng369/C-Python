// H_Kimpheng Blackjack.
// Algorithm at june,1,2024.
// start at june,2,2024.
// finish at june,3,2024.
// improve at june,5,2024.

#include <iostream>
#include <cstdlib>
using namespace std;

enum Suit { HEARTS, DIAMONDS, CLUBS, SPADES };
enum Rank { TWO = 2, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK = 10, QUEEN = 10, KING = 10, ACE = 11 };

struct Card {
    Suit suit;
    Rank rank;
    
    // _______________Display a card______________
    void displayCard() const {
        string suits[] = { "Hearts", "Diamonds", "Clubs", "Spades" };
        string ranks[] = { "", "", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" };

        cout << ranks[rank] << " of " << suits[suit] << endl;
    }
};

const int DECK_SIZE = 52;
Card deck[DECK_SIZE];
int currentCardIndex = 0;

void initializeDeck() {
    int index = 0;
    for (int suit = HEARTS; suit <= SPADES; ++suit) {
        for (int rank = TWO; rank <= ACE; ++rank) {
            deck[index].suit = static_cast<Suit>(suit);
            deck[index].rank = static_cast<Rank>(rank);
            ++index;
        }
    }
}
void shuffleDeck() {
    srand(static_cast<unsigned int>(time(0)));
    for (int i = 0; i < DECK_SIZE; ++i) {
        int j = rand() % DECK_SIZE;
        swap(deck[i], deck[j]);
    }
    currentCardIndex = 0;
}
Card dealCard() {
    return deck[currentCardIndex++];
}
int getHandValue(const Card hand[], int numCards) {
    int value = 0;
    int numAces = 0;

    for (int i = 0; i < numCards; ++i) {
        value += hand[i].rank;
        if (hand[i].rank == ACE) {
            ++numAces;
        }
    }
    // _____________Over 21_____________
    while (value > 21 && numAces > 0) {
        value -= 10;
        --numAces;
    }
    return value;
}
void displayHand(const Card hand[], int numCards, const string& owner) {
    cout << owner << "'s hand:" << endl;
    for (int i = 0; i < numCards; ++i) {
        hand[i].displayCard();
    }
    cout << "Total value: " << getHandValue(hand, numCards) << endl << endl;
}
void displayOneDealerCard(const Card hand[]) {
    cout << "Dealer's hand:" << endl;
    hand[0].displayCard();
    cout << "and one hidden card" << endl << endl;
}
//______________Main_____________;
int main() {
    initializeDeck();
    shuffleDeck();

    Card playerHand[12];
    Card dealerHand[12];
    int playerCards = 0;
    int dealerCards = 0;

    playerHand[playerCards++] = dealCard();
    playerHand[playerCards++] = dealCard();
    dealerHand[dealerCards++] = dealCard();
    dealerHand[dealerCards++] = dealCard();

    displayHand(playerHand, playerCards, "Player");
    displayOneDealerCard(dealerHand);

    int choice;
    while (true) {
        cout << "--> Do you want to (1) Hit or (2) Stand? ";
        cin >> choice;
        if (choice == 1) {
            playerHand[playerCards++] = dealCard();
            displayHand(playerHand, playerCards, "Player");
            if (getHandValue(playerHand, playerCards) > 21) {
                cout << "\t--> [Player busts! Dealer wins.] <--" << endl;
                displayHand(dealerHand, dealerCards, "Dealer");
                return 0;
            }
        } else if (choice == 2) {
            break;
        } else {
            cout << "--> Invalid choice. Please enter 1 to hit or 2 to stand." << endl;
        }
    }
    while (getHandValue(dealerHand, dealerCards) < 17) {
        dealerHand[dealerCards++] = dealCard();
    }

    int playerTotal = getHandValue(playerHand, playerCards);
    int dealerTotal = getHandValue(dealerHand, dealerCards);

    if (dealerTotal > 21) {
        cout << "\t--> [Dealer busts! Player wins.] <--" << endl;
    } else if (playerTotal > dealerTotal) {
        cout << "\t--> [Player wins!] <--" << endl;
    } else if (playerTotal < dealerTotal) {
        cout << "\t--> [Dealer wins!]  <--" << endl;
    } else {
        cout << "\t--> [It's a tie!] <--" << endl;
    }
    displayHand(dealerHand, dealerCards, "Dealer");

    return 0;
}