'''
1. Create a ticketing platform that has a 100 tickets limit and with each purchase return the new amount of tickets
'''
'''
class TicketingPlatform:
    def __init__(self, total_tickets: int = 100):
        self.total_tickets = total_tickets
        self.sold_tickets = 0

    def purchase_tickets(self, number_of_tickets: int) -> str:
        if number_of_tickets <= 0:
            return "Number of tickets must be greater than zero."
        if self.sold_tickets + number_of_tickets > self.total_tickets:
            return f"Cannot purchase {number_of_tickets} tickets. Only {self.total_tickets - self.sold_tickets} tickets left."
        
        self.sold_tickets += number_of_tickets
        return f"Successfully purchased {number_of_tickets} tickets. {self.total_tickets - self.sold_tickets} tickets remaining."
    
    def available_tickets(self, number_of_tickets: int) ->str:
        return f"{self.total_tickets - self.sold_tickets} tickets available."   


crowdpass = TicketingPlatform()
print(crowdpass.purchase_tickets(0))   # Number of tickets must be greater than zero.
print(crowdpass.purchase_tickets(10))  # Successfully purchased 10 tickets. 90 tickets remaining.
print(crowdpass.purchase_tickets(95))  # Cannot purchase 95 tickets. Only 90 tickets left.
print(crowdpass.purchase_tickets(90))  # Successfully purchased 90 tickets. 0 tickets remaining.
print(crowdpass.purchase_tickets(1))   # Cannot purchase 1 tickets. Only 0 tickets left. 
print(crowdpass.available_tickets(10))
'''
class EventTickets:
    def __init__(self, number_of_event_tickets:int = 100) -> int:
        pass