# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapulation can be used by putting the products information such as its name, price, and quantity inside of a Product object. It can also have ways to update the quantity by using e.g itemSold() and another variable that can add to the stock. This keeps the product data and its related funvtions together, making it more organized and manageable.

### 2. Abstraction
Abstraction can be used through hiding unneccessary and complicated parts of the inventory system and showing only the neccessary functions toward the user. Another method is that by using a variable called checkStock() can tell the store owner how much items are currently available without showing how the program searches through the products. It makes it easier to use since the user only needs to know what the method is, not how it actually works from the code itself.

### 3. Inheritance
Inheritance can be used when the store has different types of products that share common information. An example is Product this time can be a parent class, while foodProduct and cleaningProduct can be child classes that can be given from the parents basic information which is the product name anf price. This is very efficient, since the features only need to be written once, while the product types can have own individual features.

### 4. Polymorphism
Polymorphism can be used if different types of products use the same action but in different methods. Say a getPrice() method could work differently for regular products and discounted products, based on the type of product. The program is now more flexible due to one method being able to be used for different objects without creating a seperate method for each one.

## Reflection

I like to keep things simple, so among all of the four pillars, I would choose encapsulation since it would be the most useful. it would help keep the products name, price, and quantity together instead of having many seperate variables. As I said earlier, it can make information be easier to organize and manage, when the store has a variety of products. 
