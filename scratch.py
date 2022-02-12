# print("The {2} {1} {0}".format("fox", "brown", "quick"))

# result = 100 / 777
# result = 104.12345

# print("The result was {r:1.2f}".format(r=result))

# name = "Jose"
# print(f"Hello, his name is {name}")

# name = "Sam"
# age = 3
# print(f"{name} is {age} years old")

my_list = [1, 2, 3]
my_list = ["STRING", 100, 23.2]
print(len(my_list))
new_list = ["ONE ALL CAPS", "two", "three", "four", "five"]
new_list[0] = "one"

new_list.append("six")
new_list.pop(-2)

new_list = ["a", "e", "x", "b", "c"]
num_list = [4, 1, 8, 3]
new_list.sort()
num_list.sort()
num_list.reverse()

print(new_list)
print(num_list)

my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict["key1"])

prices_lookup = {"apple": 2.99, "orange": 1.99, "milk": 5.80}
print(prices_lookup["apple"])

# d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insideKey": 100}}
# print(d["k2"])
# print(d["k3"]["insideKey"])

# d = {"key1": ["a", "b", "c"]}
# letter = d["key1"][2].upper()
# print(letter)

d = {"k1": 100, "k2": 200}
d["k3"] = 300
print(d.keys())
print(d.values())
print(d.items())


st = "Sam Print only the words that start with s in this sentence"
for word in st.split():
    if word[0].lower() == "s":
        print(word)


print([x for x in range(1, 51) if x % 3 == 0])

st = "Print every word in this sentence that has an even number of letters"
print([(word + " is even!") for word in st.split() if len(word) % 2 == 0])


for num in range(1, 101):
    if (num % 3 == 0) & (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

