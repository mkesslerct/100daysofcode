
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return {name.title() for name in names}


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names_sorted = list(dedup_and_title_case_names(names))
    names_sorted.sort(
        reverse = True,
        key = lambda name: name.split()[1])
    return (names_sorted)



def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names_sorted = [
        name.split()[0] for name in dedup_and_title_case_names(names)]
    names_sorted.sort(
        key = lambda name: len(name))
    return(names_sorted[0])
    # ...

def main():
    print(shortest_first_name(NAMES))

if __name__ == "__main__":
    main()