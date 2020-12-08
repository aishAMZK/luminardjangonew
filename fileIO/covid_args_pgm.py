f=open("complete.csv","r")

#1st,4conf,5death,6cured

covid_data={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1].lower()
    if state=="telengana":
        state="telangana"
    confirmed=data[4]
    death=data[5]
    cured=data[6]
    if state not in covid_data:
        covid_data[state]={
            "state":state,
            "confirmed":confirmed,
            "death":death,
            "cured":cured
        }
    else:
        covid_data[state] = {
            "state": state,
            "confirmed": confirmed,
            "death": death,
            "cured": cured
        }


def print_covid_data(**kwargs):
    state=kwargs.get("state")
    if state in covid_data:
        print(state,covid_data[state]["confirmed"])
        if "property" in kwargs:
            prop=kwargs["property"]
            if prop in covid_data[state]:
                print(prop,"=>",covid_data[state][prop])
    else:
        print("there is no state with provided name")

print_covid_data(state="kerala",property="cured")
