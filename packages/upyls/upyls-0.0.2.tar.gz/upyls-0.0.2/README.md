# upyls - A collection of Python utilities

This library can now be found on [PyPi](https://pypi.org/project/upyls/)
or simply installed with:
```bash
pip install upyls
```

## Limited List

A List which can have a lower limit nd an upper limit set and only be filled with the number of items set by those 
limits

Just import and instantiate it
```python
from upyls import LimitedList
limited_list = LimitedList(lower=0, upper=1)
```

## Unit of Work
Implementation of the Unit of Work pattern out of Martin Fowler's book [Patterns of 
Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/unitOfWork.html)

### UnitOfWorkMixin
This class is an abstract class (derived from ABC). It is designed as mixin, so you just can derive your class from it 
and your class gets the functionality of this mixin
class. 

For example:
```python
from upyls import UnitOfWorkMixin

class MyUnitOfWork(UnitOfWorkMixin):
    <your code here>
```
The added functionality is to keep track of the attributes of the classes instances. If an attribute gets changed, it is marked as 
dirty and its old value is kept aside the new value.

If you have saved your instance you can call its commit-method and is will not be marked as dirty anymore and its old. 
value will be discarded. As in database transactions you can as well rollback, which means that the old value is put 
back into place and the new Value discarded. As well as with committing, the rollback-method leads to the instance not 
being marked as dirty anymore.

### Managing Unit of Works 
If you're planning to have multiple objects which you want to be Units of Work it might come handy to be able to manage 
them all. So if you're using a persistent storage, like a database or simply on disk, you might not want to save every 
single one on its own, but save them in bulks. After you saved them you should mark all saved ones. For this purpose 
there's is a derivative of the Unit of Work mixin, which is manageable and a manager class, which exposes the 
possibility to commit or rollback all manageable Units of Work, that have been registered with the manager. The two 
classes are very tightly coupled so the methods about connecting a unit with a manager are always two-ways: If you add a
manager to a unit the unit will be registered with the manager as well and if it changes it will notify the manager. If
you unregister a unit from a manager it also will stop using this manager to notify.    

#### ManageableUnitOfWorkMixin
This class is a derivative of UnitOfWorkMixin and adds the functionality to be manageable by the UnitOfWorkManager. 
First thi functionality has been in the UnitOfWorkMixin but it added some clutter if you did not want to use it in a 
manageable way. So it became a derivate, which just contains the extra functionatlity and uses the Unit of Work 
functionality of its parent.

#### UnitOfWorkManager
This class offers the functionality to manage a collection of (manageable) Units of Work. It will keep track of 
registered units that have changed and you can commit all changed units or roll them all back. Of cource you can ask the
manager if a certain unit is registered or if it is dirty. 