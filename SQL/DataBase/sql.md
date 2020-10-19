

* Structured data: pre-defined organizational property about it and it easily searchable and analyzable.
  - The data is backed by a model that dictates the size of each field of the data: its type, length, restriction.
* unStructured data: characterized by lack of organization and a data model that describes the structure of a single record or attribution of any individual fields.
* Semi-structured data: is a cross between structured and unstructured data, and though there's no explicit data model or structure definition. JSON, XML

- unstructured data such as video, images, documents, social media postings, file etc is really semi-structured data. 

- relational data: data store as rows , columns of a table rigidly follow a defined schema that describes the type and size of the data that a table column can hold.


* Temperary Table: Temporary tables are persisted for the duration of the MySQL monitor session and removed once the session is terminated. User doesnot need to explicitly clean-up a temporary table.

* Character set defines what characters MySQL can store
* Collation set decides how strings are ordered.
  
* Insert value 
* Query the value  , BETWEEN ... AND ,  COALESCE() ... GREATEST(), IN, INTERVAL . IS
* Like return the same pattern here!

```
    SELECT * FROM Actors WHERE FirstName LIKE "Jen%";
    SELECT * FROM Actors WHERE FirstName LIKE "Jennifer%";


```