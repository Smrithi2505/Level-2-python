import random

# Cards and suits
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']
suits = ['C', 'D', 'H', 'S']      # Clubs < Diamonds < Hearts < Spades

# ---------------- CREATE DECK ----------------

deck = []

for suit in suits:
    for card in cards:
        deck.append(suit + card)

# Add two Jokers
deck.append('JK1')
deck.append('JK2')

print("Unshuffled Deck:")
for card in deck:
    print(card, end=" ")
print()

random.shuffle(deck)

print("\nShuffled Deck:")
for card in deck:
    print(card, end=" ")
print()

# ---------------- TOSS ----------------

print("\n\nTOSS")

# Pick 3 random cards for the toss
toss_cards = random.sample(deck, 3)

print("Toss Cards:", toss_cards)

toss_total = 0

for card in toss_cards:
    if card.startswith('JK'):
        toss_total += 15          # Joker value for toss
    else:
        toss_total += cards.index(card[1]) + 2

print("Toss Total =", toss_total)

if toss_total % 2 == 0:
    print("Player wins the toss!")
else:
    print("Computer wins the toss!")

# ---------------- DEAL CARDS ----------------

# Alternate card dealing
player_cards = deck[0::2]
computer_cards = deck[1::2]

table_cards = []

# Stores Joker values already used
used_jokers = []

# Suit order: Clubs < Diamonds < Hearts < Spades
suit_order = ['C', 'D', 'H', 'S']

# ---------------- GAME ----------------

while len(player_cards) > 0 and len(computer_cards) > 0:

    input("\nPress Enter to play a card...")

    p_card = player_cards.pop(0)
    c_card = computer_cards.pop(0)

    print("\nPlayer Card:", p_card)
    print("Computer Card:", c_card)

    table_cards.append(p_card)
    table_cards.append(c_card)

    # ---------- PLAYER JOKER ----------

    if p_card.startswith('JK'):

        print("\nYou played a Joker!")

        while True:

            print("\nChoose a card value for your Joker:")
            print("2 3 4 5 6 7 8 9 X J Q K A")

            choice = input("Enter your choice: ").upper()

            if choice not in cards:
                print("Invalid choice!")

            elif choice in used_jokers:
                print("That value has already been used!")

            else:
                used_jokers.append(choice)
                p_value = cards.index(choice) + 2
                break

    else:
        p_value = cards.index(p_card[1]) + 2

    # ---------- COMPUTER JOKER ----------

    if c_card.startswith('JK'):

        print("\nComputer played a Joker!")

        available_cards = []

        for card in cards:
            if card not in used_jokers:
                available_cards.append(card)

        computer_choice = random.choice(available_cards)
        used_jokers.append(computer_choice)

        c_value = cards.index(computer_choice) + 2

        print("Computer chose:", computer_choice)

    else:
        c_value = cards.index(c_card[1]) + 2

    # ---------- COMPARE VALUES ----------

    if p_value > c_value:

        print("\nPlayer wins this round!")
        player_cards.extend(table_cards)
        table_cards.clear()

    elif c_value > p_value:

        print("\nComputer wins this round!")
        computer_cards.extend(table_cards)
        table_cards.clear()

    else:

        # Same value -> compare suits

        if p_card.startswith('JK') or c_card.startswith('JK'):

            print("\nWAR!")

            if len(player_cards) < 4 or len(computer_cards) < 4:
                break

            table_cards.extend(player_cards[0:3])
            table_cards.extend(computer_cards[0:3])

            del player_cards[0:3]
            del computer_cards[0:3]

        else:

            p_suit = suit_order.index(p_card[0])
            c_suit = suit_order.index(c_card[0])

            if p_suit > c_suit:

                print("\nSame value! Player wins by suit.")
                print("Suit order: Clubs < Diamonds < Hearts < Spades")

                player_cards.extend(table_cards)
                table_cards.clear()

            elif c_suit > p_suit:

                print("\nSame value! Computer wins by suit.")
                print("Suit order: Clubs < Diamonds < Hearts < Spades")

                computer_cards.extend(table_cards)
                table_cards.clear()

            else:

                print("\nWAR!")

                if len(player_cards) < 4 or len(computer_cards) < 4:
                    break

                table_cards.extend(player_cards[0:3])
                table_cards.extend(computer_cards[0:3])

                del player_cards[0:3]
                del computer_cards[0:3]

    print("\nPlayer Cards Left:", len(player_cards))
    print("Computer Cards Left:", len(computer_cards))

# ---------------- RESULT ----------------

print("\n\nGAME OVER")

if len(player_cards) > len(computer_cards):
    print("PLAYER WINS THE GAME!")

elif len(computer_cards) > len(player_cards):
    print("COMPUTER WINS THE GAME!")

else:
    print("GAME DRAWN!")
    