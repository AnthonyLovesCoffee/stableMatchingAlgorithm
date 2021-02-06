# stable matching algorithm to find the most stable pair between two, equally sized, sets where each set gives a list of ranked preferences
# this implementation will try find the most stable couples, where the men will propose to the women

# the men's preferences, where index 0 is the most preferred woman
preferred_rankings_men = {
	'ronald': 	['livvy', 'sarah', 'zoey', 'daniella'],
	'john': 	['sarah', 'livvy', 'daniella', 'zoey'],
	'boris': 	['sarah', 'daniella', 'zoey', 'livvy'],
	'chet': 	['livvy', 'sarah', 'zoey', 'daniella']
}

# the women's preferences, where index 0 is the most preferred man
preferred_rankings_women = {
	'livvy': 	['ronald', 'boris', 'john', 'chet'],
	'sarah': 	['ronald', 'boris', 'chet', 'john'],
	'zoey':  	['chet', 'john', 'ronald', 'boris'],
	'daniella':	['ronald', 'john', 'chet', 'boris'] 
}

# list of couples that can be a possible match
possibleMatch = []

# men who still need to propose and not get rejected
singleMen = []

# initalising the arrays of men and women to show that they are all single at the start
def init_single_men():
    for man in preferred_rankings_men.keys():
        singleMen.append(man)

def stableMatchingAlg(man):
    # we want to try to find the first free woman available to any man at any given time
    print(f"Currently dealing with {man}")
    for woman in preferred_rankings_men[man]:
        taken = [couple for couple in possibleMatch if woman in couple] # returns whether the woman is already paired with a possible match

        if len(taken) == 0:
            possibleMatch.append([man, woman])
            singleMen.remove(man)
            print(f"{man} is no longer single, possible match with {woman}")
            break

        elif len(taken) > 0:
            print(f"{woman} is already taken")

            # now checking the ranking of the current man and the ranking of the other possible man for the woman
            currentMan = preferred_rankings_women[woman].index(taken[0][0])
            possibleMan = preferred_rankings_women[woman].index(man)

            if currentMan < possibleMan:
                print("{} is satisfied with {}".format(woman, taken[0][0]))
            else:
                print("{} is better than {}".format(man, taken[0][0]))
                print("{} is now single again... {} and {} are now a possible match".format(taken[0][0], man, woman))
            
                singleMen.remove(man) # the man who was single is now taken
                singleMen.append(taken[0][0]) # the man who was taken is now single

                # the woman's new partner 
                taken[0][0] = man
                break


def stableMatch():
    while len(singleMen) > 0:
        for man in singleMen:
            stableMatchingAlg(man)


def main():
    init_single_men()
    print(singleMen)
    stableMatch()
    print(possibleMatch)

main()