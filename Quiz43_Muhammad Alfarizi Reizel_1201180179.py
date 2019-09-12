ListGPA = [2.1,2.5,4,3]

def Reward (GPA):
    bonus = 500000
    Reward = GPA*bonus
    return Reward
for GPA in ListGPA:
    if GPA > 2.5:
        print("Congratulation! here's Your Reward : Rp", Reward(GPA))
    else :
        print("Sorry, Only for smart people.")