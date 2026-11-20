def senators_states(filename):
    file1 = open(filename)
    list1 = file1.readlines()
    file1.close()
    senators_states = {}
    for item in list1:
        result = item.split(",")
        name = result[0]
        state = result[1].strip()
        senators_states[name] = state
    return senators_states

def main():
    senators_states_list = senators_states("senators_states.csv")
    print(senators_states_list)
    
if __name__ == "__main__":
    main()
    
