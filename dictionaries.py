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

def house_state_district(filename):
    file1 = open(filename)
    list1 = file1.readlines()
    file1.close()
    hr_statedist = {}
    for item in list1:
        result = item.split(",")
        name = result[0]
        statedist = result[3].strip()
        hr_statedist[name] = statedist
    return hr_statedist

def zip_district(filename):
    file1 = open(filename)
    list1 = file1.readlines()
    file1.close()
    zip_district = {}
    for item in list1:
        result = item.split(",")
        zip = result[0]
        district = result[1].strip()
        zip_district[zip] = district
    return zip_district

def state_abbr(filename):
    file1 = open(filename)
    list1 = file1.readlines()
    file1.close()
    state_abbr = {}
    for item in list1:
        result = item.split(",")
        state = result[0]
        abbr = result[1].strip()
        state_abbr[state] = abbr
    return state_abbr

