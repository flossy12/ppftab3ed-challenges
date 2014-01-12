#Counting program

start = int(input("enter a starting number to count from: "))
end = int(input("enter a number to end counting at: ")) +int(1)
countBy = int(input("enter the number you want to count by: "))

for i in range(start, end, countBy):
    print(i)
