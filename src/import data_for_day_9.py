from data_for_day_9 import states_list, us_state_abbrev

def main():
    print('The 10th item on the list is ' + 
    states_list[9])
    print('The 10th item in the dictionary is ' + 
    str(list(us_state_abbrev.items())[9]))
    print('The 45th key in the dictionary is ' + 
    str(list(us_state_abbrev.keys())[44]))

if __name__ == "__main__":
    main()