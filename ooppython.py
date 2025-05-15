from dataclasses import dataclass
from typing import ClassVar
@dataclass
class American:
    national_language: ClassVar[str] = "english"
    national_food: ClassVar[str] = "karachibiryani"
    normal_bodytemperature: ClassVar[float]=98.6
    name: str
    age: int
    weight: float
    liked_food=str
    # national_language: ClassVar[str] = "english"
    # national_food: ClassVar[str] = "karachibiryani"

    def speaks(self):
        return f"{self.name} is speaking... {American.national_language}"

    def eats(self):
        return f"{self.name} is eating...{American.national_food}"

    @staticmethod
    def country_language():
        return American.national_language
john = American(name="harry", age=16, weight=65,like_food="p")
print(john.speaks())  # Output: harry is speaking... english
print(john.eats())
# print(American.language)
print(American.national_language)
print(john.name)
print(john.age)
print(john.weight)
print(john)

