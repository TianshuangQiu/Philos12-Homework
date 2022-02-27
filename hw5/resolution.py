import sys

class clause():
    """
    All terms are conjunctions of each other (AND)
    """
    def __init__(self, terms):
        self.terms = terms
    
    
    def __eq__(self, other):
        if not isinstance(other, clause):
            return false
        return sorted(self.terms) == sorted(other.terms)
    
    def __str__(self):
        curr = ""
        for t in terms:
            curr += t
            curr += r" \land "
        
        curr = curr[:-6]


def main():
    statement = sys.argv[0]
    while True:
        


if __name__ == "__main__":
    main()