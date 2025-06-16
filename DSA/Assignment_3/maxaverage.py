'''Write a Python function maxaverage(l) that takes a list of pairs of the form(name,score) as argument, 
where name is a string and score is an integer. 
Each pair is to be interpreted as the score of the named player.
For instance, an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7), ('Pujara',122),('Ashwin',90)] represents
two scores of 73 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one score of 122 for Pujara. 
Your function should compute the players who have the highest average score (average = total across all scores for that 
player divided by number of entries) and return the list of names of these players as a list, sorted in alphabetical order. 
If there is a single player, the list will contain a single name.For instance, maxaverage([('Kohli',73),('Ashwin',33),('Kohli',7),
('Pujara',122), ('Ashwin',90)]) should return ['Pujara'] because the average score of Kolhi is 40 (80 divided by 2), of 
Ashwin is 61.5 (123 divided by and of Pujara is 122 (122 divided by 1), of which 122 is the highest.'''
class PlayerScores:
    def __init__(self):
        self.scores = []

    def add_score(self, name, score):
        self.scores.append((name, score))

    def maxaverage(self):           
        
        player_scores = {}
        for name, score in self.scores:
            if name in player_scores:
                player_scores[name]['sum'] += score
                player_scores[name]['count'] += 1
            else:
                player_scores[name] = {'sum': score, 'count': 1}

       
        averages = {} 
        for name, scores in player_scores.items():
            averages[name] = scores['sum'] / scores['count']

        
        max_average = None
        for average in averages.values():
            if max_average is None or average > max_average:
                max_average = average 

        
        max_average_players = [name for name, average in averages.items() if average == max_average]

        
        max_average_players.sort()

        return max_average_players

def main():
    player_scores = PlayerScores()
    num_scores = int(input("Enter the number of scores: "))

    for i in range(num_scores):
        name = input(f"Enter the name of player {i+1}: ")
        score = int(input(f"Enter the score of player {i+1}: "))
        player_scores.add_score(name, score)

    result = player_scores.maxaverage()
    print("The players with the highest average score are:")
    print(result)

if __name__ == "__main__":
    main()
    
# This code:

# Asks the user to enter the number of scores they want to input.
# Asks the user to enter the name and score of each player.
# Calculates the average score for each player.
# Finds the maximum average score.
# Finds the players with the maximum average score.
# Sorts the list of players with the maximum average score.
# Prints the list of players with the highest average score.