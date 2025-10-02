# **1.<ins>Translating characters</ins>**:-
   The challenge asks us to run `/challenge/run` which will print the flag but will swap the casing of all characters (e.g., A will become a and vice-versa) and asks us to get the flag by swapping them using the `tr` command.
## My solve:-
   **My flag** :-`pwn.college{Ic7a5KqdvwDqugSed3eXdBW8sUK.01MxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` which will print the flag but will swap the casing of all characters and asks us to reverse it using `tr`, hence i opened the shell and an ran `/challenge/run` and piped it's output to the `tr` command as it's input and changed all the lower letters to upper and upper to lower and got the flag. 
   ```bash
   hacker@data~translating-characters:~$ /challenge/run | tr '[:upper:][:lower:]' '[:lower:][:upper:]'
   yOUR CASE-SWAPPED FLAG:
   pwn.college{Ic7a5KqdvwDqugSed3eXdBW8sUK.01MxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `tr` command translates characters it receives over standard input and prints them to standard output, i alo came to know that in basic usage, `tr` translates the character provided in its first argument to the character provided in its second argument.

### Refference :-
   None


# **2.<ins>Deleting characters</ins>**:-
   The challenge will intersperse some decoy characters (specifically: `^` and `%`) among the flag characters and asks us to use `tr -d` to remove them.
## My solve:-
   **My flag** :-`pwn.college{I-2dLPo4NQsjE6n-tQKkzhJwKd1.0FNxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to use `tr -d` to remove the interspersed decoy characters (specifically: `^` and `%`) among the flag characters, hence i opened the shell and ran `/challenge/run` and piped it's output to `tr` command and used the `-d` option on `^` to delete it and then piped it's output as the input of another `tr` command because `tr` can only take one arrgument for deleting and used `-d` option on `%` to delete it and got the flag. 
   ```bash
   hacker@data~deleting-characters:~$ /challenge/run | tr -d ^ | tr -d %
   Your character-stuffed flag:
   pwn.college{I-2dLPo4NQsjE6n-tQKkzhJwKd1.0FNxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `-d` option in the `tr` command is used to delete the characters provided to it as the argument.

### Refference :-
   None


# **3.<ins>Deleting newlines</ins>**:-
   The challenge will inject a bunch of newlines into the flag and asks us to delete them with `tr`'s `-d` flag and the escaped newline specification to get the flag.
## My solve:-
   **My flag** :-`pwn.college{Ir5RLBO5jVAPbX37suJiLfozwk0.0VNxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to use the `tr` commands `-d` option to delete the newline characters i.e `"\n"`, hence i opened the shell and ran `/challenge/run` and piped it's output to `tr` and used the `-d` option on `"\n"` to delete them and got the flag.
   ```bash
   hacker@data~deleting-newlines:~$ /challenge/run | tr -d "\n"
   Your line-split flag: pwn.college{Ir5RLBO5jVAPbX37suJiLfozwk0.0VNxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to add new line we have to use `"\n"` character.

### Refference :-
   None


# **4.<ins></ins>**:-
   The challenge asks us to 
## My solve:-
   **My flag** :-``

   So, the challenge asked us to
   ```bash
  
   ```

### What i learned:-
   I learned that 

### Refference :-
   None
