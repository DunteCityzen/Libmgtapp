# Simple Library Management Application

* Built with Flask
* Simple SQLite database

## Booksview snapshpt
![books snap](https://github.com/DunteCityzen/Libmgtapp/assets/65547730/e723d3cc-ca12-4a18-9d4d-061365d7ce08)


## Membersview snapshot
![members snap](https://github.com/DunteCityzen/Libmgtapp/assets/65547730/50ac0dd9-cef7-459a-a7b2-2fe9d43bf54c)


## Transactionsview snapshot
![transactions snap](https://github.com/DunteCityzen/Libmgtapp/assets/65547730/1fa6abc4-b085-407d-b438-3793525df045)


## Disclaimer
On the vercel link you might experience problems adding new items(members, transactions and books). Probably due to an issue that occured with the database during deployment.
However, by cloning the repository and taking care of the prerequisites in the requirements.txt file, and hosting it locally, everything should run just fine.

## More info
The app is a simple library management system that gives a user(librarian) abilities to perform all the functions that might be necessary in the day to day operations of a library.

### Models
There were four models in this application that allowed it to make and edit database entries:
 * Book
 * Members
 * Transaction

 The Book model had the following attributes
    id of type integer which is the primary key
    title of type string
    author of type string
    status of type string as well

The Member model had the following attributes
    id of type integer which is the primary key
    name of type string
    debt of type integer

The Transaction model had the following attributes and relationships
    id of type integer
    borrow_date of type date 
    return_date of type date
    fee of type integer
    
    #### Foreign Keys
    member_id of type integer
    book_id of type integer

    #### Defining Relationships between Member and Transaction as well as Book and Transaction
    member = db.relationship('Member', backref='transactions')
    book = db.relationship('Book', backref='transactions')