# Program to calculate the average of three exam scores


# function to calculate the average
def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average


# ask user for input 
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

#Calculate the average
average = calculate_average(score1, score2, score3)

# Display the result
print("The average of the scores is: ", average)


# if average is greater than 90, print "Bra jobbat!"
if average > 90:
    print("Bra jobbat!")

