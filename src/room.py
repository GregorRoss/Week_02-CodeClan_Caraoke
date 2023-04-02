class Room:

    def __init__(self, name, entry, till, size):
        self.name = name
        self.entry = entry
        self.till = till
        self.size = size
        self.playlist = []
        self.occupancy = []

    def guest_check_in(self,guest):
        self.occupancy.append(guest)
        # print(f"pre entry fee ",{guest.name}, ' wallet ',{guest.wallet})
        guest.wallet -= self.entry
        # print(f"post entry fee ",{guest.name}, ' wallet ',{guest.wallet})
        self.till += self.entry
        # print(f"Room: ", {self.name}, "till total: ",{self.till}) 


    def guest_check_out(self, guest):
        self.occupancy.remove(guest)

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        self.playlist.remove(song)


    def clear_room(self):
        self.occupancy.clear()
        self.playlist.clear()

    def favourite_song(self, guest):
        if guest.favourite in self.playlist:
            print("yay favourite song")



    def guest_check_in_check_size(self,guest):
        if len(self.occupancy)+1 <= self.size:
            self.guest_check_in(guest)
        elif len(self.occupancy)+1 > self.size:
             return "Room full, please return in 10 minutes or select another room"




