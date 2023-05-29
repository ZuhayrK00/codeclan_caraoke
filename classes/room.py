class Room:
    def __init__(self, name, max_guests, till):
        self.name = name
        self.max_guests = max_guests 
        self.till = till
        self.playlist = []
        self.guests = []
        self.guest_tabs = {} 

# MVP 

    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def check_in_guest(self, guest):
        if len(self.guests) < self.max_guests: 
            self.guests.append(guest)
            self.add_entry_fee_to_tab(guest) 

    def check_out_guest(self, guest):
        if guest in self.guests:
            self.clear_fully_paid_guest_tab(guest) 
            self.guests.remove(guest)
    

# Extensions

    def take_entry_fee(self, guest):
        entry_fee = 10.00
        if guest.cash >= entry_fee:
            guest.cash -= entry_fee
            self.till += entry_fee
    
    def add_entry_fee_to_tab(self, guest):
        if guest in self.guest_tabs:
            self.guest_tabs[guest] += 10.00
        else:
            self.guest_tabs[guest] = 10.00

    def clear_fully_paid_guest_tab(self, guest):
        if guest in self.guest_tabs:
            tab_amount = self.guest_tabs[guest]
            if tab_amount == 0.00:
                del self.guest_tabs[guest]

