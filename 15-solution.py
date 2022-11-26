
persons = ["John", "Jack", "Mills", "Paul", "Pain", "Rahman", "Kader", "Ghani", "Jaya", "Sowmeya"]

# for person in persons :
#     print('The Person name is '+person)
    
# a = 0
# while(a < len(persons)):
#     print('The Person Name is '+persons[a])
#     a = a + 1


# Exercise 2
# def UserFunc(name, empid, organisation='OpsEazy', department= 'IT', designation= 'Developer'):
#     print(name,empid, organisation, department, designation)

# UserFunc("Fazlur", "OE000027")

# Exercise 3
def Calculator(op, a, b):
    match op:
        case "Add":
            print(a+b)
        case "Sub":
            print(a-b)
        case "Mul":
            print(a*b)
        case "Div":
            print(a/b)
        case "Mod":
            print(a%b)
        case _:
            print("No Other Operation Allowed")
            
Calculator('MMMM', 7, 6)