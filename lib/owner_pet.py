class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Stores the owner's pets

    def pets(self):
        """Returns a list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner after validating it's a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet class")
        pet.owner = self  # Assigns the owner to the pet
        self._pets.append(pet)  # Adds pet to owner's list

    def get_sorted_pets(self):
        """Returns a sorted list of pets by name."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Stores all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type. Choose from: " + ", ".join(Pet.PET_TYPES))

        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Owner is initially None

        if owner:
            self.set_owner(owner)  # Assign owner if provided

        Pet.all.append(self)  # Add pet to class-level list

    def set_owner(self, owner):
        """Sets the pet's owner after validating it's an Owner instance."""
        if not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner class")
        self.owner = owner
        owner.add_pet(self)  # Adds pet to owner's pet list
