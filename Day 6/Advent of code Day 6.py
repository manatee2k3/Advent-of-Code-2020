
with open('Customs questions AoC Day 6.txt') as f:
    questions = f.read().strip().split('\n\n')
# inports the data and pulls each group into its own string within the list,
# seperating each individual questionaire by a '\'

questions = [line.split() for line in questions]
# splits each group into its own lst and
# seperates each individual questionaire into its own string.

def yes_answers(questions, function):
    for group in questions:
        yield len(function(*(set(s) for s in group)))
        # The yield expression converts the function into a generator to return values one by one.
        # The * is an Unpacking Operator
        
       
print(sum(yes_answers(questions, set.union)))
# Union will combine two sets with all elements from the two sets without any repeating.

print(sum(yes_answers(questions, set.intersection)))
#  Intersection finds and returns elements which can be found in both sets. 
