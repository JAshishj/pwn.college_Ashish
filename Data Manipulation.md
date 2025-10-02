# **1.<ins></ins>**:-
   The challenge asks us to run `/challenge/run` which will print the flag but will swap the casing of all characters (e.g., A will become a and vice-versa) and asks us to get the flag by swapping them using the `tr` command.
## My solve:-
   **My flag** :-`pwn.college{Ic7a5KqdvwDqugSed3eXdBW8sUK.01MxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` which will print the flag but will swap the casing of all characters and asks us to reverse it using `tr`, hence i opened the shell and an ran `/challenge/run` and piped it's output to the `tr` command as it's input and changed all the lower letters to upper abd upper to lower and got the flag. 
   ```bash
   hacker@data~translating-characters:~$ /challenge/run | tr '[:upper:][:lower:]' '[:lower:][:upper:]'
   yOUR CASE-SWAPPED FLAG:
   pwn.college{Ic7a5KqdvwDqugSed3eXdBW8sUK.01MxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `tr` command translates characters it receives over standard input and prints them to standard output, i alo came to know that in basic usage, `tr` translates the character provided in its first argument to the character provided in its second argument.

### Refference :-
   None


# **2.<ins></ins>**:-
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


# **3.<ins></ins>**:-
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
