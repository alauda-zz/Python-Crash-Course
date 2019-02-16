def describe_pet(pet_name, animal_type='dog'):
    """Describe information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry','hamster')
describe_pet('willie','dog')
describe_pet(pet_name='barbara')