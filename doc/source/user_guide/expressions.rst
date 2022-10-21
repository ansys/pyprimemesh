************
Expressions 
************

Expressions can be used to gather entities needed for certain operations.  

Special characters currently used are “*”, “!” and spaces/commas.  These special characters can be used within a string as follows: 

* “abc\*” collects all required entities with a name starting with abc  
* “\*abc” collects all required entities with a name ending with abc 
* “\*abc*” collects all required entities with a name containing abc  
* “!abc\*” collects all required entities with a name that is not starting with abc 
* "\*abc,\*xyz" "\*abc \*xyz" (comma/space represents OR) collects all required entities with a name ending with abc or xyz 

An example of expressions being used is in the :class:`ScopeDefinition <ansys.meshing.prime.ScopeDefinition>` class 
where the :attr:`part_expression <ansys.meshing.prime.ScopeDefinition.part_expression>` attribute allows part entities to be gathered to define a scope.  
The exact part name can be provided or expressions can be used for more complex entity collections. 
 
.. code:: python
    
    >>> part = model.parts[0]
    >>> # First part in model
    >>> scope = prime.ScopeDefinition(model=model, part_expression=part.name)
    
    >>> # All parts except solid
    >>> scope = prime.ScopeDefinition(model=model, part_expression="* !solid")
