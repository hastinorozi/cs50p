fruit={
    "apple":130,
    "banana":110,
    "lemon":"15",
    "pear":"100",
    "peach":"60",
}
item=input(Item:).title().strip()
for test in fruit:
    if item in test:
        print(f"Calories: fruit[test]")