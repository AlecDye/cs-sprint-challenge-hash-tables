#  Hint:  You may not need all of these.  Remove the unused functions.

"""
where the `source` string represents the starting airport and the
`destination` string represents the next airport along our trip. The
ticket for your first flight has a destination with a `source` of
`NONE`, and the ticket for your final flight has a `source` with a
`destination` of `NONE`. 

tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]

output:
["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
"""

# tickets refer to an array of these
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = [None] * length

    # loop Ticket class entries into cache
    for ticket in tickets:
        # Ticket.source(key) Ticket.destination(item)
        cache[ticket.source] = ticket.destination

    # specifically looking for "NONE"
    destination = cache["NONE"]

    for flight in range(length):
        route[flight] = destination
        destination = cache[destination]

    return route
