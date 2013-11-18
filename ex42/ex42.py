## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ?? is-a object
class Dog(Animal):

    def __init__(self, name):
        ## ?? Dog has-a name
        self.name = name

## ?? is-a object
class Cat(Animal):

    def __init__(self, name):
        ## ?? Cat has-a name
        self.name = name

## ?? is-a object
class Person(object):

    def __init__(self, name):
        ## ?? pearson has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ?? is-a object
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? Employee has-a name and salary
        super(Employee, self).__init__(name)
        ## ?? employee has-a salary
        self.salary = salary

## ?? is-a objet
class Fish(object):
    pass

## ?? is a object
class Salmon(Fish):
    pass

## ?? is-a object
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ?? satan is-a Cat
satan = Cat("Satan")

## ?? mary is-a Person
mary = Person("Mary")

## ?? mary has-a pet called satan
mary.pet = satan

## ?? frank is-a Employee making 120000
frank = Employee("Frank", 120000)

## ?? frank has-a pet named rover
frank.pet = rover

## ?? flipper is-a Fish
flipper = Fish()

## ?? crouse is-a Salmon
crouse = Salmon()

## ?? harry is-a Halibut
harry = Halibut()
