import random
from abc import ABC, abstractmethod

class BasePokemon:
    def __str__(self):
        return f'{self.name}/{self.poketype}'

class EmojiMixin:
    emoji = {'grass': 'em1',
             'fire': 'em2',
             'water': 'em3',
             'electric': 'em4'}
    def __str__(self):
        text_poketype = super().__str__()
        return text_poketype.replace(self.poketype, self.emoji[self.poketype])

class AnimeMon(ABC):
    @classmethod
    @abstractmethod
    def inc_exp(self):
        pass

    @property
    @abstractmethod
    def inc_exp(self):
        pass

class Pokemon(EmojiMixin, BasePokemon, AnimeMon):
     def __init__(self, name: str, poketype: str = None):
         self.name = name
         self.poketype = poketype
         self.exp = 0

     def inc_exp(self, step_size):
         self.exp += step_size


class Digimon(Pokemon):
    def inc_exp(self, value: int):
        self.exp += value * 8

def train(pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
    if win:
        pokemon.inc_exp(step_size)



