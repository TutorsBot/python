# Output

year = 2023
event = "Training"

print(f'{event} is going to happen in {year}')

yes = 223
no = 233
per = yes/(yes+no)
# print('{:2.3%} is the value in {:1}'.format(per, yes))

s = "Hello World"
print(str(s))
print(repr(s))

print(str(4/2))


print(event+' is going to happen in '+repr(year))

print("Sample Text about {} Training in {}".format("Python", "Chennai"))
print("Sample Text about {1} Training in {0}".format("Bangalore", "Java"))

print("Sample Text about {course} Course Program".format(course="Java"))


# input
x = int(input("enter the number you want to check : "))
# f = open('sample.txt', 'w', encoding="utf-8")

# with open('sample.txt', encoding="utf-8") as f:
#     read_data = f.read()
#     print(read_data)
# f.closed


with open('sample.txt', encoding="utf-8") as f:
    read_data = f.readline()
    print(read_data)
    read_data = f.readline()
    print(read_data)
f.closed

with open('sample.txt',encoding="utf-8") as f:
    for line in f:
        print(line)

    
with open('sample.txt', 'w', encoding="utf-8") as fi:
    fi.write('This the Test Coding \n')
fi.closed
