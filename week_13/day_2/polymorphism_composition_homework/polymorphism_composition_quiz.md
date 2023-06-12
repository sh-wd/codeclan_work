# Polymorphism & Composition Homework - Quiz

# Polymorphism

1. What does the ___word___ 'polymorphism' mean?

Many forms.


2. What does it mean when we apply polymorphism to OO design? Give a simple Java example.

This means that we can use the same method to perform different actions on differing subclasses of a superclass. An example would be that a super class of Animal has a method of make a sound. This class has subclasses of cats, dogs and pigs that all make a sound but a different one to one another.


3. What can we use to implement polymorphism in Java?

We can use inheritance (super and subclasses) to do this.


4. How many 'forms' can an object take when using polymorphism?

Unlimited.


5. Give an example of when you could use polymorphism.

An example could be of modelling bluetooth devices connecting to a computer. The method would be connect and each device would when connected to the computer display a different string to state that that specific device was connected.



# Composition and Aggregation

6. What do we mean by 'composition' in reference to object-oriented programming?

Composition describes the relationship of one object to another. It is described as a 'has a' relationship.


7. When would you use composition? Provide a simple example in Java.

Composition would be used when you want objects to have a close relationship but not have the parent object rely on the existence of the child. An example would be a building has a room(s) but it can exist without the rooms if we were to destroy the walls and the room no longer exists but the building still does.


8. Give a difference between composition and aggregation?

A difference between the two is that aggregation means that both objects can exist independently of one another.


9. What is/are the advantage(s) of using composition/aggregation?

They are more flexible than inheritance. They allow for polymorphism.


10. When using composition, when an object is destroyed, what happens to all the objects it is composed of?

As composition a close relationship the life cycle of the objects that compose the larger object are destroyed when it is destroyed.


11. When using aggregation, when an object is destroyed, what happens to all the objects it is composed of?

In aggregation the life cycles are independent therefore the the child objects will remain in existence
