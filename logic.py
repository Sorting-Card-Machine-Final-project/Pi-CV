from random import shuffle

suites = {'S': 0, 'D': 1, 'C': 2, 'H':3 }
ranks = {str(key) : key for key in range(2,11)}
special_ranks = {'J': 11, 'Q': 12, 'K': 13, 'A':1}
ranks.update(special_ranks)

HEAD = -1

class Deck:

    def __init__(self):
        self.deck =  [r + s for s in suites for r in ranks]
    
    def shuffle_deck(self):
        return shuffle(self.deck)


class Sorter:

    def __init__(self):
        self.suites = suites
        self.num_of_cards_per_suite = {'S': 0, 'D': 0, 'C': 0, 'H':0 }
        self.ranks = ranks
        self.cells = [[], [], [], []]
        self.iteration_q = []

    #1st Sort.
    def suite_sort(self, card):
        return self.suites[card[-1]] #Get the card suite to point to the right sorting cell. 

    #2nd Sort, sorting by ranks in batches.
    def first_sort(self, card):
        rank = self.ranks[card[:-1]]
        if rank < 4:
            return 0
        if rank < 7:
            return 1
        if rank < 10:
            return 2
        return 3
    
    def second_sort(self, card):
        rank = card[:-1]
        #print(f"in second sort, current card: {card}, current rank: {rank}")
        if rank in ['A', '4', '7', '10']:
            return 3
        if rank in ['2', '5', '8', 'J']:
            return 2
        if rank in ['3', '6', '9', 'Q']:
            return 1
        if rank in ['K']:
            return 0
        
    def second_sort_v2(self, card):
        rank = card[:-1]
        #print(f"in second sort, current card: {card}, current rank: {rank}")
        if rank in ['10', '6', '2']:
            return 3
        if rank in ['J', '7', '3']:
            return 2
        if rank in ['Q', '8', '4']:
            return 1
        if rank in ['K', '9', '5', 'A']:
            return 0
            
    def final_sort(self, card):
        rank = card[:-1]
        #print(f"in second sort, current card: {card}, current rank: {rank}")
        if rank in ['A']:
            return 0
        if rank in ['5', '4', '3', '2']:
            return 1
        if rank in ['9', '8', '7', '6']:
            return 2
        if rank in ['K', 'Q', 'J', '10']:
            return 3
            
    def sort_iteration(self, deck, sort_method, destination):
        complexity_counter, eject_counter = 0,0
        while len(deck) > 1:
            suite = self.suite_sort(deck[HEAD])
            while self.suite_sort(deck[HEAD]) == suite:
                complexity_counter += 1
                self.send_card_to_cell(deck, sort_method)
                if len(deck) == 0:
                    break

            self.eject_cells(self.cells, destination)
            eject_counter += 1

            
        return complexity_counter, eject_counter

    def send_card_to_cell(self, deck, method):
        card = deck.pop()
        self.cells[method(card)].append(card)
        return card
    
    def eject_cells(self, cells, iter_queue):
        for i in range(4):
            iter_queue.extend(cells[3-i]) #remove all items from all cells by order and add them to the queue.
            cells[3-i] = []

    def sort(self, deck): #the deck will be the system[deck_order] list
        complexity_counter = 0
        eject_counter = 0
        # SUITE SORTING
        while len(deck) > 0:
            complexity_counter += 1
            self.send_card_to_cell(deck, self.suite_sort)
        self.eject_cells(self.cells, deck)
        eject_counter += 1

        # 1ST SORT
        print(f"#######before 1st sort, the deck is:\n{deck}")
        while len(deck) > 1:
            
            suite = self.suite_sort(deck[HEAD])
            while self.suite_sort(deck[HEAD]) == suite:
                complexity_counter += 1
                self.send_card_to_cell(deck, self.first_sort)
                if len(deck) == 0:
                    break

            self.eject_cells(self.cells, self.iteration_q)
            eject_counter += 1

        deck = self.iteration_q
        self.iteration_q = []

        print(f"#######before 2st sort, the deck is:\n{deck}")
        #2ND SORT
        while len(deck) > 0:
            suite = self.suite_sort(deck[HEAD])
            for _ in range(3):
                complexity_counter += 1
                if len(deck) == 0:
                    break
                if self.suite_sort(deck[HEAD]) != suite:
                    break
                if "K" in deck[HEAD]:
                    self.send_card_to_cell(deck, self.second_sort)
                    if len(deck) == 0:
                        break
                self.send_card_to_cell(deck, self.second_sort)

            self.eject_cells(self.cells, self.iteration_q)
            eject_counter += 1

            #sorted?
        #self.eject_cells(self.cells, self.iteration_q)
        deck = self.iteration_q
        self.iteration_q = []
        print(f"#######final deck sort, the deck is:\n{deck}")
        return complexity_counter, eject_counter

    def sort_v2(self, deck):
        complexity_counter = 0
        eject_counter = 0
        # SUITE SORTING
        while len(deck) > 0:
            complexity_counter += 1
            self.send_card_to_cell(deck, self.suite_sort)
        self.eject_cells(self.cells, deck)
        eject_counter += 1

        # 1ST SORT
        print(f"#######before 1st sort, the deck is:\n{deck}")
        
        self.sort_iteration(deck, self.first_sort, self.iteration_q)
                #print(destination)
        deck = self.iteration_q
        self.iteration_q  = []
        
        print(f"#######before 2st sort, the deck is:\n{deck}")
        self.sort_iteration(deck, self.second_sort_v2, self.iteration_q)
        deck = self.iteration_q
        self.iteration_q = []

        print(f"#######before FINAL sort, the deck is:\n{deck}")
        self.sort_iteration(deck, self.final_sort, self.iteration_q)
        deck = self.iteration_q
        self.iteration_q = []

        print(f"Done operation, the sorted deck: \n{deck}")
        return complexity_counter, eject_counter
        
def test():
    sorter = Sorter()
    deck = Deck()
    print(deck.deck)
    deck.shuffle_deck()

    comp, ejec = sorter.sort_v2(deck.deck)
    print(f"The complexity counter is: {comp}\nEject counter is: {ejec}")

if __name__ == "__main__":
    test()    
# end main



