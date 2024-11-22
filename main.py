from animal import Animal
from dog import Dog


if __name__ == "__main__":
    
    a_cat = Animal("Generic", "Unknown")
    print(a_cat)
    a_cat.speak()
    
    a_dog = Dog("Buddy", "Caine", "'Golden Retriever'")
    print(a_dog)
    a_dog.speak()

    print("All Animals: ")
    all_animals = Animal.get_all_animals()
    for animal in all_animals:
        print(animal)
        