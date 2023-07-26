import ipdb


class Animal:
    def set_species(self, new_species):
        self.species = new_species
        return self.species


holly = Animal()

print(holly.set_species("cat"))
print(holly.set_species("dog"))
