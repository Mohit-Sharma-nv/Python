# dictionary

dictionary = {
    "a": [1,2,3],
    "b": "hello",
    "x": True
  }

print(dictionary["a"][2])

my_list = [
{
    "a": [1,2,3],
    "b": "hello",
    "x": True
  },
{
    "a": [4,5,6],
    "b": "Bye",
    "x": False
  }
]

print(my_list[0]["a"][1])

dic = {
    "123": 12,
    "123": "Hello"
}
print(dic)

user = {
    "basket": [1,23,4,4],
    "greet": "hello",
    "age":100
}

print(user.get("age",39))

print(100 in user.values())

print(user.items())