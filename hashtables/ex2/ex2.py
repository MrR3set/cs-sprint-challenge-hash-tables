#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    routeHash = {}
    route = [None] * length
    val = routeHash["NONE"]
    for ticket in tickets:
        if ticket not in routeHash:
            routeHash[ticket.source]=ticket.destination
            
    for i in range(0,length):
        route[i] = val
        val = routeHash[val]

    return route



ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))