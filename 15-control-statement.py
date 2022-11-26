# For Loop 
# for n in range(15):
#     print(n+1)
    
# While Loop
num = 0
while(num < 3):
    print(num)
    num = num +1
   
    
# break keyword
# name = "TutorsBot"
# for c in name:
#     if c == 'B':
#         break
#     print(c)
    


# continue
name = "TutorsBot"
for n in name:
    if n == "B":
        continue
        # print(n)
    print(n)
    
# pass
name = "TutorsBot"
for w in name:
    pass



def weekday(day):
    # date = 8
    # Switch Cases 
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid day number. Try again"
        
        
print(weekday(8))