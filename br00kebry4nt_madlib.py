def mad_lib():
    color = input("enter a color: ")
    zoo_animal = input("enter the name of a zoo animal: ")
    textile = input("enter a textile: ")
    number1 = input("enter a number: ")
    number2 = input("enter another number: ")
    aquatic_animal = input("enter the name of an aquatic animal: ")
    body_part = input("enter the name of a body part: ")
    size = input("enter a size: ")
    verb = input("enter a verb: ")
    direction = input("enter a direction of travel: ")
    mad_lib = f"baa, baa, {color} {zoo_animal} have you any {textile}. yes sir, yes sir, {number1} bags full. {number2} for the {aquatic_animal}, and one for the {body_part} and one for the {size} boy who {verb} {direction} the lane."
    print("\nhere's your mad lib story:")
    print(mad_lib)

mad_lib()
