# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
There were no revisions needed from my previous activity.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|Name|String|Public | |
|level|Integer|Public| |
|health|Integer|Private| |
|isAzureDragoon|Boolean|Private| |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
So that the data type Health or isAzureDragoon is protected from being directly changed outside of the class.

### Which method changes the state of your object?
The TrueThrust() and DragonDive() methods can change the state of the object because they perform attacks that can affect the objects health.

### How did your two objects demonstrate that instances are independent?
The two objects have their own separate attribute values. Changes made to one object do not affect the other object therefore showing that each instance is independent.

### What is the difference between your class diagram and your object diagram?
The class diagram shows the blueprint of the Estinien class, including its attributes and methods. The object diagram shows the actual objects created from the class and the specific values of their attributes.
