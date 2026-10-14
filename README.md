|------------------------|
|   BankAccount          | -> class name
|------------------------|
|   bank_name            |
|   MIN_BALANCE          |  -> class attributes
|   total_accounts       |
|------------------------|
|   owner                |
|   balance              |  -> instance attributes
|   transactions         |
|------------------------|
|   validate_amount()    |
|   format_money()       |  -> staic methods
|   is_valid_owner()     |
|------------------------|
|   deposit()            |
|   withdraw()           |
|   summary()            |  -> instance methods
|   transfer_to()        |
| get_transactions_list()|
|------------------------|

1. BankAccount is class
2. bank_name, MIN_BALANCE, total_accounts are class attributes because they are shared among all objects not particular for any one object.
3. owner, balance, transactions are instance attributes because they are dependent on different objects.
4. validate_amount(), format_money(), is_valid_owner() are static methods because they are not dependent on objects. The work they are doing is all same so it saves memory.
5. Instance methods are needed to work on object like each object has its own data. The methods are as follows:
    i. deposit() -> first amount is check and then add amount to balance of object.
    ii. withdraw() -> amount is check and also check the withdraw amount is not greater than balance and subtract it.
    iii. summary() -> short summary with owner name and salary
    iv. transfer_to() -> is depositing from one user and performing withdraw from another account holder along with that it make sure the consistancy of data. If transaction is failed then recover early data.
    v. get_transcations_list -> it is returning the list of transactions.