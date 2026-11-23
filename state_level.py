import dictionaries

senators_states_list = dictionaries.senators_states("senators_states.csv")
house_district_list = dictionaries.house_state_district("hr_statedistrict.csv")
zip_district_list = dictionaries.zip_district("zip_district.csv")
state_abbr_list = dictionaries.state_abbr("state_abbr.csv")

def get_home():
    state = input("What state are you looking for? (type in entire state name) ").upper()
    abstate = state_abbr_list.get(state)
    district = input("What is your zip code? ")

def main():
    get_home()

if __name__ == "__main__":
    main()