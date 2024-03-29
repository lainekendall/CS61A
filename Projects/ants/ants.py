"""The ants module implements game logic for Ants Vs. SomeBees."""

import random
import sys
from ucb import main, interact, trace
from collections import OrderedDict


################
# Core Classes #
################


class Place:
    """A Place holds insects and has an exit to another Place."""

    def __init__(self, name, exit=None):
        """Create a Place with the given exit.

        name -- A string; the name of this Place.
        exit -- The Place reached by exiting this Place (may be None).
        """
        self.name = name
        self.exit = exit
        self.bees = []        # A list of Bees
        self.ant = None       # An Ant
        self.entrance = None  # A Place
        # Phase 1: Add an entrance to the exit
        if self.exit:
            self.exit.entrance = self

    def add_insect(self, insect):
        """Add an Insect to this Place.

        There can be at most one Ant in a Place, unless exactly one of them is
        a BodyguardAnt (Phase 4), in which case there can be two. If add_insect
        tries to add more Ants than is allowed, an assertion error is raised.

        There can be any number of Bees in a Place.
        """
        if insect.is_ant:
            # Phase 4: Special handling for BodyguardAnt
            if self.ant:
                if self.ant.can_contain(insect):
                    self.ant.contain_ant(insect)
                    insect.place = self
                    return
                elif insect.can_contain(self.ant):
                    insect.contain_ant(self.ant)
                    insect.place = self
                    self.ant = insect
                    return 
                assert self.ant is None, 'Two ants in {0}'.format(self)
            self.ant = insect
        else:
            self.bees.append(insect)
        insect.place = self

    def remove_insect(self, insect):
        """Remove an Insect from this Place."""
        if insect.is_ant:
            assert self.ant == insect, '{0} is not in {1}'.format(insect, self)
            # Phase 4: Special handling for BodyguardAnt and QueenAnt
            if isinstance(insect, BodyguardAnt):
                self.ant = insect.ant
                return
            elif isinstance(insect, QueenAnt):
                return
            else:
                self.ant = None
        else:
            self.bees.remove(insect)

        insect.place = None

    def __str__(self):
        return self.name


class Insect:
    """An Insect, the base class of Ant and Bee, has armor and a Place."""

    is_ant = False
    watersafe = False

    def __init__(self, armor, place=None):
        """Create an Insect with an armor amount and a starting Place."""
        self.armor = armor
        self.place = place  # set by Place.add_insect and Place.remove_insect
    

    def reduce_armor(self, amount):
        """Reduce armor by amount, and remove the insect from its place if it
        has no armor remaining.

        >>> test_insect = Insect(5)
        >>> test_insect.reduce_armor(2)
        >>> test_insect.armor
        3
        """
        self.armor -= amount
        if self.armor <= 0:
            print('{0} ran out of armor and expired'.format(self))
            self.place.remove_insect(self)

    def action(self, colony):
        """The action performed each turn.

        colony -- The AntColony, used to access game state information.
        """

    def __repr__(self):
        cname = type(self).__name__
        return '{0}({1}, {2})'.format(cname, self.armor, self.place)


class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = 'Bee'
    watersafe = True

    def sting(self, ant):
        """Attack an Ant, reducing the Ant's armor by 1."""
        ant.reduce_armor(1)

    def move_to(self, place):
        """Move from the Bee's current Place to a new Place."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Phase 3: Special handling for NinjaAnt
        if self.place.ant and self.place.ant.blocks_path:
            return True

    def action(self, colony):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        colony -- The AntColony, used to access game state information.
        """
        if self.blocked():
            self.sting(self.place.ant)
        elif self.place is not colony.hive and self.armor > 0:
            self.move_to(self.place.exit)


class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    is_ant = True
    implemented = False  # Only implemented Ant classes should be instantiated
    damage = 0
    food_cost = 0
    blocks_path = True
    container = False

    def __init__(self, armor=1):
        """Create an Ant with an armor quantity."""
        Insect.__init__(self, armor)

    def can_contain(self, other):
        if self.container and not self.ant and not other.container:
            return True
        return False


class HarvesterAnt(Ant):
    """HarvesterAnt produces 1 additional food per turn for the colony."""

    name = 'Harvester'
    implemented = True
    food_cost = 2

    def action(self, colony):
        """Produce 1 additional food for the colony.

        colony -- The AntColony, used to access game state information.
        """
        colony.food += 1


def random_or_none(s):
    """Return a random element of sequence s, or return None if s is empty."""
    if s:
        return random.choice(s)


class ThrowerAnt(Ant):
    """ThrowerAnt throws a leaf each turn at the nearest Bee in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    food_cost = 4
    min_range = 0
    max_range = 10

    def nearest_bee(self, hive):
        """Return the nearest Bee in a Place that is not the Hive, connected to
        the ThrowerAnt's Place by following entrances.

        This method returns None if there is no such Bee (or none in range).
        """
        start = self.place
        for _ in range(self.min_range):
            start = start.entrance
        place = start
        for _ in range(self.min_range, self.max_range):
            if place == hive:
                return None
            if place == None:
                return None
            if place.bees:
                return random_or_none(place.bees)
            place = place.entrance
        return None
 

    def throw_at(self, target):
        """Throw a leaf at the target Bee, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a leaf at the nearest Bee in range."""
        self.throw_at(self.nearest_bee(colony.hive))


class Hive(Place):
    """The Place from which the Bees launch their assault.

    assault_plan -- An AssaultPlan; when & where bees enter the colony.
    """

    def __init__(self, assault_plan):
        self.name = 'Hive'
        self.assault_plan = assault_plan
        self.bees = []
        for bee in assault_plan.all_bees:
            self.add_insect(bee)
        # The following attributes are always None for a Hive
        self.entrance = None
        self.ant = None
        self.exit = None

    def strategy(self, colony):
        exits = [p for p in colony.places.values() if p.entrance is self]
        for bee in self.assault_plan.get(colony.time, []):
            bee.move_to(random.choice(exits))


class AntColony:
    """An ant collective that manages global game state and simulates time.

    Attributes:
    time -- elapsed time
    food -- the colony's available food total
    queen -- the place where the queen resides
    places -- A list of all places in the colony (including a Hive)
    bee_entrances -- A list of places that bees can enter
    """

    def __init__(self, strategy, hive, ant_types, create_places, food=2):
        """Create an AntColony for simulating a game.

        Arguments:
        strategy -- a function to deploy ants to places
        hive -- a Hive full of bees
        ant_types -- a list of ant constructors
        create_places -- a function that creates the set of places
        """
        self.time = 0
        self.food = food
        self.strategy = strategy
        self.hive = hive
        self.ant_types = OrderedDict((a.name, a) for a in ant_types)
        self.configure(hive, create_places)

    def configure(self, hive, create_places):
        """Configure the places in the colony."""
        self.queen = Place('AntQueen')
        self.places = OrderedDict()
        self.bee_entrances = []
        def register_place(place, is_bee_entrance):
            self.places[place.name] = place
            if is_bee_entrance:
                place.entrance = hive
                self.bee_entrances.append(place)
        register_place(self.hive, False)
        create_places(self.queen, register_place)

    def simulate(self):
        """Simulate an attack on the ant colony (i.e., play the game)."""
        while len(self.queen.bees) == 0 and len(self.bees) > 0:
            self.hive.strategy(self)    # Bees invade
            self.strategy(self)         # Ants deploy
            for ant in self.ants:       # Ants take actions
                if ant.armor > 0:
                    ant.action(self)
            for bee in self.bees:       # Bees take actions
                if bee.armor > 0:
                    bee.action(self)
            self.time += 1
        if len(self.queen.bees) > 0:
            print('The ant queen has perished. Please try again.')
        else:
            print('All bees are vanquished. You win!')

    def deploy_ant(self, place_name, ant_type_name):
        """Place an ant if enough food is available.

        This method is called by the current strategy to deploy ants.
        """
        constructor = self.ant_types[ant_type_name]
        if self.food < constructor.food_cost:
            print('Not enough food remains to place ' + ant_type_name)
        else:
            self.places[place_name].add_insect(constructor())
            self.food -= constructor.food_cost

    def remove_ant(self, place_name):
        """Remove an Ant from the Colony."""
        place = self.places[place_name]
        if place.ant is not None:
            place.remove_insect(place.ant)

    @property
    def ants(self):
        return [p.ant for p in self.places.values() if p.ant is not None]

    @property
    def bees(self):
        return [b for p in self.places.values() for b in p.bees]

    @property
    def insects(self):
        return self.ants + self.bees

    def __str__(self):
        status = ' (Food: {0}, Time: {1})'.format(self.food, self.time)
        return str([str(i) for i in self.ants + self.bees]) + status


def ant_types():
    """Return a list of all implemented Ant classes."""
    all_ant_types = []
    new_types = [Ant]
    while new_types:
        new_types = [t for c in new_types for t in c.__subclasses__()]
        all_ant_types.extend(new_types)
    return [t for t in all_ant_types if t.implemented]

def interactive_strategy(colony):
    """A strategy that starts an interactive session and lets the user make
    changes to the colony.

    For example, one might deploy a ThrowerAnt to the first tunnel by invoking
    colony.deploy_ant('tunnel_0_0', 'Thrower')
    """
    print('colony: ' + str(colony))
    msg = '<Control>-D (<Control>-Z <Enter> on Windows) completes a turn.\n'
    interact(msg)

def start_with_strategy(args, strategy):
    """Reads command-line arguments and starts a game with those options."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Ants vs. SomeBees")
    parser.add_argument('-f', '--full', action='store_true',
                        help='loads a full layout and assault plan')
    parser.add_argument('-w', '--water', action='store_true',
                        help='loads a full layout with water')
    parser.add_argument('-i', '--insane', action='store_true',
                        help='loads a difficult assault plan')
    parser.add_argument('--food', type=int,
                        help='number of food to start with', default=2)
    args = parser.parse_args()

    assault_plan = make_test_assault_plan()
    layout = test_layout
    food = args.food
    if args.full:
        assault_plan = make_full_assault_plan()
        layout = dry_layout
    if args.water:
        layout = wet_layout
    if args.insane:
        assault_plan = make_insane_assault_plan()
    hive = Hive(assault_plan)
    AntColony(strategy, hive, ant_types(), layout, food).simulate()


###########
# Layouts #
###########

def wet_layout(queen, register_place, length=8, tunnels=3, moat_frequency=3):
    """Register a mix of wet and and dry places."""
    for tunnel in range(tunnels):
        exit = queen
        for step in range(length):
            if moat_frequency != 0 and (step + 1) % moat_frequency == 0:
                exit = Water('water_{0}_{1}'.format(tunnel, step), exit)
            else:
                exit = Place('tunnel_{0}_{1}'.format(tunnel, step), exit)
            register_place(exit, step == length - 1)

def dry_layout(queen, register_place, length=8, tunnels=3):
    """Register dry tunnels."""
    wet_layout(queen, register_place, length, tunnels, 0)

def test_layout(queen, register_place, length=8):
    """Register a single dry tunnel."""
    dry_layout(queen, register_place, length, 1)


#################
# Assault Plans #
#################


class AssaultPlan(dict):
    """The Bees' plan of attack for the Colony.  Attacks come in timed waves.

    An AssaultPlan is a dictionary from times (int) to waves (list of Bees).

    >>> AssaultPlan().add_wave(4, 2)
    {4: [Bee(3, None), Bee(3, None)]}
    """

    def __init__(self, bee_armor=3):
        self.bee_armor = bee_armor

    def add_wave(self, time, count):
        """Add a wave at time with count Bees that have the specified armor."""
        bees = [Bee(self.bee_armor) for _ in range(count)]
        self.setdefault(time, []).extend(bees)
        return self

    @property
    def all_bees(self):
        """Place all Bees in the hive and return the list of Bees."""
        return [bee for wave in self.values() for bee in wave]

def make_test_assault_plan():
    return AssaultPlan().add_wave(2, 1).add_wave(3, 1)

def make_full_assault_plan():
    plan = AssaultPlan().add_wave(2, 1)
    for time in range(3, 15, 2):
        plan.add_wave(time, 1)
    return plan.add_wave(15, 8)

def make_insane_assault_plan():
    plan = AssaultPlan(4).add_wave(1, 2)
    for time in range(3, 15):
        plan.add_wave(time, 1)
    return plan.add_wave(15, 20)

##############
# Extensions #
##############

class Water(Place):
    """Water is a place that can only hold 'watersafe' insects."""

    def add_insect(self, insect):
        """Add insect if it is watersafe, otherwise reduce its armor to 0."""
        print('added', insect, insect.watersafe)
        Place.add_insect(self, insect) #put the insect in the place
        if not insect.watersafe: #if the insect is not watersafe
            insect.reduce_armor(insect.armor) #reduce the armor to 0


class FireAnt(Ant):
    """FireAnt cooks any Bee in its Place when it expires."""

    name = 'Fire'
    damage = 3
    implemented = True
    food_cost = 6
    armor = 1

    def reduce_armor(self, amount):
        self.armor -= amount
        if self.armor <= 0:
            copy = self.place.bees[:]
            for bee in copy:
                bee.reduce_armor(self.damage)

class WallAnt(Ant):
    name = 'Wall'
    implemented = True
    armor = 4
    food_cost = 4

    def __init__(self, armor=4):
        """Create an Ant with an armor quantity."""
        Ant.__init__(self, armor)


class LongThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees at least 4 places away."""

    name = 'Long'
    min_range = 4
    implemented = True
    food_cost = 3


class ShortThrower(ThrowerAnt):
    """A ThrowerAnt that only throws leaves at Bees less than 3 places away."""

    name = 'Short'
    max_range = 3
    implemented = True
    food_cost = 3


"*** YOUR CODE HERE ***"
# The WallAnt class


class NinjaAnt(Ant):
    """NinjaAnt does not block the path and damages all bees in its place."""

    name = 'Ninja'
    damage = 1
    blocks_path = False
    implemented = True
    food_cost = 6

    def action(self, colony):
        for bee in self.place.bees[:]:
            bee.reduce_armor(self.damage)


class ScubaThrower(ThrowerAnt):

    name = 'Scuba'
    implemented = True
    food_cost = 5
    armor = 1
    watersafe = True

# The ScubaThrower class


class HungryAnt(Ant):
    """HungryAnt will take three turns to digest a Bee in its place.
    While digesting, the HungryAnt can't eat another Bee.
    """
    name = 'Hungry'
    time_to_digest = 3
    implemented = True
    food_cost = 4
    armor = 1


    def __init__(self):
        Ant.__init__(self)
        self.digesting = 0

    def eat_bee(self, bee):
        bee.reduce_armor(bee.armor)

    def action(self, colony):
        if self.digesting:
            self.digesting -= 1
        else:
            if self.place.bees:
                self.eat_bee(random_or_none(self.place.bees))
                self.digesting = self.time_to_digest
        return None


class BodyguardAnt(Ant):
    """BodyguardAnt provides protection to other Ants."""
    name = 'Bodyguard'
    container = True
    implemented = True
    food_cost = 4
    armor = 2

    def __init__(self):
        Ant.__init__(self, 2)
        self.ant = None  # The Ant hidden in this bodyguard

    def contain_ant(self, ant):
        self.ant = ant        

    def action(self, colony):
        print(self.ant)
        if self.ant:
            self.ant.action(colony)

class LaserAnt(ThrowerAnt):
    """
    This class is optional. No tests are provided for this class.
    """
    name = 'Laser'
    distance_weakening = 0.3
    insects_shot_weakening = 0.5
    "*** YOUR CODE HERE ***"
    implemented = False

class QueenPlace:
    """A place that represents both places in which the bees find the queen.

    (1) The original colony queen location at the end of all tunnels, and
    (2) The place in which the QueenAnt resides.
    """
    def __init__(self, colony_queen, ant_queen):
        self.queen = ant_queen
        self.colony = colony_queen

    @property
    def bees(self):
        return self.queen.bees + self.colony.bees


class QueenAnt(ScubaThrower):  # You should change this line
    """The Queen of the colony.  The game is over if a bee enters her place."""

    name = 'Queen'
    food_cost = 6
    implemented = True
    num_queens = 0

    def __init__(self):
        "*** YOUR CODE HERE ***"
        Ant.__init__(self)
        self.double_trouble_ants = []
        if QueenAnt.num_queens == 0:
            self.imposter = False
        else:
            self.imposter = True
        QueenAnt.num_queens += 1



    def action(self, colony):
        """A queen ant throws a leaf, but also doubles the damage of ants
        in her tunnel.

        Impostor queens do only one thing: reduce their own armor to 0.
        """
        "*** YOUR CODE HERE ***"
        colony.queen = QueenPlace(colony.queen, self.place)
        if self.imposter:
            # self.reduce_armor(self.armor)
            return

        def double_damage(self, place):
            if place.ant and (place.ant not in self.double_trouble_ants):
                self.double_trouble_ants += [place.ant]
                if isinstance(place.ant, QueenAnt):
                    return
                place.ant.damage = 2 * place.ant.damage
                if isinstance(place.ant, BodyguardAnt):
                    if isinstance(place.ant.ant, QueenAnt):
                        return
                    if place.ant.ant:
                        place.ant.ant.damage = 2 * place.ant.ant.damage 
            return

        place = self.place
        while place:
            double_damage(self, place)
            place = place.entrance
        place = self.place.exit
        while place:
            double_damage(self, place)
            place = place.exit

        ScubaThrower.action(self, colony)



class AntRemover(Ant):
    """Allows the player to remove ants from the board in the GUI."""

    name = 'Remover'
    implemented = False

    def __init__(self):
        Ant.__init__(self, 0)


##################
# Status Effects #
##################

def make_slow(action):
    """Return a new action method that calls action every other turn.

    action -- An action method of some Bee
    """
    def new_action(colony):
        if colony.time % 2 == 0:
            return action(colony)
        else:
            print('slow')
            return None
    return new_action



def make_stun(action):
    """Return a new action method that does nothing.

    action -- An action method of some Bee
    """
    def new_action(colony):
        print('stun') ##
        return
    return new_action

def apply_effect(effect, bee, duration):
    """Apply a status effect to a Bee that lasts for duration turns."""
    def new_action(colony):
        # print('duration = ')
        # print(duration)
        nonlocal duration
        if duration>0:
            # print('effected') 
            duration -= 1
            return effect(bees_original_action)(colony)
        else:
            # print('nothing')
            duration -= 1
            return bees_original_action(colony)
        # print(duration)
    bees_original_action = bee.action
    bee.action = new_action

    # if colony.time in range(start, start + duration):
    #     bee.action = effect(bee.action)
    # for _ in range(duration):
    #     effect(bee.action)
    #     duration -= 1



class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = 'Slow'
    food_cost = 4
    armor = 1
    implemented = False

    def throw_at(self, target):
        if target:
            apply_effect(make_slow, target, 3)


class StunThrower(ThrowerAnt):
    """ThrowerAnt that causes Stun on Bees."""

    name = 'Stun'
    food_cost = 6
    armor = 1
    implemented = False

    def throw_at(self, target):
        if target:
            apply_effect(make_stun, target, 1)

@main
def run(*args):
    start_with_strategy(args, interactive_strategy)
