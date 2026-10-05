***********
Expressions
***********

Expressions are used to gather named entities needed for various operations.  

The special characters used are ``*``, ``!``, and spaces or commas. These characters
can be used within a string as follows: 

* ``abc\*`` collects all required entities with a name starting with abc.
* ``\*abc`` collects all required entities with a name ending with abc.
* ``\*abc*`` collects all required entities with a name containing abc.
* ``!abc\*`` collects all required entities with a name that is not starting with abc.
* ``\*abc,\*xyz`` ``\*abc \*xyz`` collects all required entities with a name ending with abc or xyz. A comma or a space represents ``OR``. 

The following example uses expressions in the :class:`ScopeDefinition <ansys.meshing.prime.ScopeDefinition>`
class. The :attr:`part_expression <ansys.meshing.prime.ScopeDefinition.part_expression>` parameter
is used to gather part entities to define a scope. You can provide the exact part name or use
expressions for more complex entity collections. 
 
.. code-block:: pycon
    
    >>> part = model.parts[0]
    >>> # First part in model
    >>> scope = prime.ScopeDefinition(model=model, part_expression=part.name)

    >>> # All parts except solid
    >>> scope = prime.ScopeDefinition(model=model, part_expression="* !solid")
