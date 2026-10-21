# Create an Intramural score tracker

# Each team entry is a list that includes
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against

# You will ask how many teams are playing.
# Loop that many times, create a team and set all scores to 0, then append it to your list of teams
# Start an infinite loop for main menu
#   1) Add score
#   2) See Team stats
#   3) See Overall Standings
#   4) Quit

#   1) Enter team 1, team 2, goals for team 1, goals for team 2
#       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie

#   2) Print a list of team names.
#       Once the user selects, Print out their stats

#   3) Print out the teams in order from most team points to least
#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.

#   4) Say goodbye and break out of the loop
#Ask for number of teams
print("Welcome to SportsScores tracking system!")
numTeams = int(input("How many teams are playing? "))

#create lists to score team information

Team_names = []
Games_played = []
Team_wins = []
Team_losses = []
Team_ties = []
Team_goals_for = []
Team_goals_against = []

#Create loops

for team in range(numTeams):
    name = input(f"Enter Team {team+1} name: ")
    Team_names.append(name)
    Games_played.append(0)
    Team_wins.append(0)
    Team_losses.append(0)
    Team_ties.append(0)
    Team_goals_for.append(0)
    Team_goals_against.append(0)

#Create another loop
running=True
while running:
    print(" Menu Contents ")
    print("1) Add score")
    print("2) See Team stats ")
    print("3) See overall standings")
    print("4) Quit")

    choice = int(input("Enter your choice (1-4): "))
#Add scores
if choice == "1":
    t1_name = input("Enter Team 1 name: ")
    t2_name = input("Enter Team 2 name: ")

    g1 = int(input(f"Enter goals for {t1_name}:  "))
    g2 = int(input(f"Enter goals for {t2_name}: "))

