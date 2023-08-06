## Security Notice

> THIS MODULE IS NOT INTENDED FOR *FULL PRODUCTION USE* \
> I AM UNSURE TO WEATHER IT IS ACTUALLY SECURE OR NOT,  \
> AND NO SECURITY EXPERT HAS REVIEWED THE CODE.  \
> \
> PLEASE IMPLIMENT WITH CAUTION; REVIEW THE CODE FIRST IF \
> YOU ARE GOING TO USE THIS FOR FULL PRODUCTION USE. 


## Introduction

HashedDB allows you to safely and secuerly store usernames and passwords (<-- *hopefully* securely) in a database ready for you to use.
HashedDB stores all passwords under a **sha256 hash**, ensuring that even if a hacker did gain the database file, object or dictionary
created by this script, they would not be able to access the true user's passwords; they are encrypted using one-way cryptography.
Now, if you are no expert at this, you may be thinking "Well, how do I use this then? How do I check if the user has logged in 
with the right password?" Well, it is quite simple.

How it works is this: The typed password the user is attempting to log in with is computed using the same algorithm as the origional one 
that was then stored in the database. The newly computed password that the user just entered is then checked against the one in the 
database and if they are the same, the user can log in, as they have typed the correct password. This way, the user's data can be stored 
in a secure manner that is entierly safe from hackers.

## Security 

### Compromisation

There is only one or two ways that a user's account can be compromised (99% sure... ); 1. if they use a silly password, eg. "password" or 2. if an attacker uses a brute-force.
The explination to how the user's account can be compromised is simple: the password "password" will always create the same hash value, 
no matter how many times it is computed. Hence, an attacker can check for matches between a computation of "password" that was pre-generated and
the password hashes in the file.

### Salt

*While the concept of "salt" is not implemented in this version of HashedDB, it is intended to be added in future versions.*

### Support & Legacy Systems

It is possible to change the algorithm that is used to compute hashes. See **Techical** section.

## Tutorials

### Baisc Usage

Below is a basic example file that adds users and then logs in. Note that the plaintext passwords are *never stored* in the database - only their hashes!

`# Import Module`\
`import HashedDB`\
\
`# Create Database`\
`db = HashedDB.HashedDB()`\
\
`# Add Users`\
`db.add_user('bobsmith', 'password1234')`\
`db.add_user('shellythames', 'neonchickenABCD1234')`\
\
`# Simple CLI - Ask for username and password`\
`print('Login: ')`\
`un = input('Username > ')`\
`pw = input('Password > ')`\
\
`# Check Details Against Database`\
`result = db.check_user(un, pw)`\
\
`# Report Results`\
`if result:`\
	`print('Login Succesful!')`\
`else:`\
	`print('Login Failed!')`


### Using File Saving - Tutorial

Here is a more complex example - this time, we have two scripts an a `.json` file shared between them. One of the files (`add_people.py`) adds users into the database (`database.json`), while the other file (`login.py`)reads the database and contains a simple CLI login program, like the last.

**Directory:** \
`Example 2 `\
` ├ add_people.py `\
` ├ login.py `\
` ⎩ database.json `\
\
**FILE: add_people.py** \
\
`# Import Module`\
`import HashedDB`\
\
`# Create New Database`\
`db = HashedDB.HashedDB()`\
\
`# Add Users`\
`db.add_user('bobsmith', 'password1234')`\
`db.add_user('shellythames', 'neonchickenABCD1234')`\
\
`# Save To A JSON File`\
`db.to_json('database.json')`\
\
**FILE: login.py**\
\
`# Import Modules`\
`import HashedDB`\
\
`# Create Database`\
`db = HashedDB.HashedDB()`\
\
`# WARNING!!!! Use the following method with caution!` \
`# All data stored in the database before calling this method will be lost. `\
`# If you would like to look at methods that can add data but not delete data, `\
`# See the "Loading without loosing" subsection. `\
\
`# Fill Database With Usernames From JSON File`\
`db.from_json('database.json')`\
\
`# Simple CLI - Ask for username and password`\
`print('Login: ')`\
`un = input('Username > ')`\
`pw = input('Password > ')`\
\
`# Check Details Against Database`\
`result = db.check_user(un, pw)`\
\
`# Report Results`\
`if result:`\
	`print('Login Succesful!')`\
`else:`\
	`print('Login Failed!')`

### Using custom file formats

To use custom file formats, you simply have to call `db.filesave_format(filename, format_)` instead of `db.to_json(filename)` and `db.fileload_format(filename, format_)` instead of `db.from_json(filename)`! \
\
The argument `format_` must be a module or class that has a .dump(filename, data) and .load(filename) method. An error will be raised otherwise.

### Loading without loosing

In all the examples previously listed, any function that loaded any data into the database would have *deleted* any data already contained within it (as mentioned by the file data warnings). However, if you would like to load more data without loosing any that is already contained, for instance, or you would like to load data from a collection of multiple files, you have to use a different set of functions. Below is a table that lists the function that loads data but deletes data stored from before, and on the right is the equivilent function that *does not* lose the data previously stored: 

| Deletes Data  | Dosn't Delete Data  |
|:----------|:----------|
| `db.load_json(...)`    | `db.append_json(...)`    |
| `db.import_dict(...)`    | `db.add_by_dict(...)`    |
| `db.fileload_format(...)`    | `db.fileapnd_format(...)`    |

It should also be noted that if there is data previously stored that has the same name as new data added, the previously stored data *will be over-ridden*.

### "The Dictionary"

If you wish to obtain or import (or append) a dictionary containing all the usernames an password hashes, you can use the method listed below: 

- db.get_dict() - Gets the dictionary
- db.import_dict(dict_) - Imports a dictionary
- db.add_by_dict(dict_) - Appends all the items from the dictionary into the database.

### Removing Users

If you wish to remove a user from the database, you can use:
`db.rem_user(un)` - Simply pass the username to the argument "`un`" \
\
If you wish to remove a list of users from the database, you can use:
`db.rem_by_list(list_, shout_errors=True)` - Pass the list of users to remove to "`list_`".
Note: Use `shout_errors` to prevent an `IndexError` being raised when a username in the removal list is invalid.

## Technical ⚙️

> Warning! Using some of these following features may be potentally dangerous and could risk passwords being compromised.

### Changing/Switching Algorithms

If you wish to use a different hashing algorithm, for example **MD5**, you can pass the algorithm to the `alg` keyword argument. The default for this argument is `hashlib.sha256`, but you can use whatever you want (that has a `hexdigest(...)` method and takes utf-8 bytes as an input for the `__init__` method). An example is shown below, using the **sha-1** algorithm: \
\
`>>> import HashedDB` \
`>>> import hashlib` \
`>>> db = HashedDB.HashedDB(alg=hashlib.sha1)`\
\
And it should work like normal, all except for the fact that you are using a different (and less secure) algorithm. 

### "Compute"

If you wish to compute a hash without adding a user to the database, simple use the following method: \
\
`db.compute(inp)` - Pass the text you want to compute to the "`inp`" argument.
Warning! The text passed to "`inp`" must be in bytes form. An error will be raised if otherwise.

## Credits

The credits for this module go to: ]
Pigeon Nation