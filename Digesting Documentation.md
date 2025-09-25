# **1.<ins>Learning from documentation</ins>**:-
   The challenge asks us to get the flag by invoking `/challenge/challenge` properly it also gave us the documentation of the `/challenge/challenge` i.e to properly run this program, you will need to pass it the argument of `--giveflag`.
   
## My solve:-
   **My flag** :-`pwn.college{AH0TLJ2izLlsUif6Ku7qgWXfjEL.QX0ITO0wCNxAzNzEzW}`

   So, the challenge asked us to getthe flag by invoking the `/challenge/challenge` and passing `--giveflag` as an argument to it, hence i opened the shell and invoked the `/challenge/challenge` with `--giveflag` as it's argument and got the flag.
   ```bash
  hacker@man~learning-from-documentation:~$ /challenge/challenge --giveflag
   Correct argument! Here is your flag:
   pwn.college{AH0TLJ2izLlsUif6Ku7qgWXfjEL.QX0ITO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to make proper use of the shell commands we have to pass proper specification of arguments to them.
   
### Refference :-
   None.


# **2.<ins>Learning complex usage</ins>**:-
   The challenge gives us to get the flag by invoking `/challenge/challenge` properly it also gave us the documentation of the `/challenge/challenge` i.e this program allows you to print arbitrary files to the terminal, when given the `--printfile` argument. The argument to the `--printfile` argument is the path of the flag to read. For example, `/challenge/challenge --printfile /challenge/DESCRIPTION.md` will print out the description of the level!.
   
## My solve:-
   **My flag** :-`pwn.college{c13zcS3bWGtWgeGYf6qQ38-reby.QX1ITO0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the `/challenge/challenge` and passing `--printfile` as an argument to it and the path of the file we want to read as an argumrnt to `--printfile`, hence i opened the shell and invoked the `/challenge/challenge` with `--giveflag` as it's argument and `/flag` as it's argument as all the flags of the pwn.college dojo will be in the `/flag` file as told before by the challenge and got the flag.
   ```bash
   hacker@man~learning-complex-usage:~$ /challenge/challenge --printfile /flag
   Correct argument! Here is the /flag file:
   pwn.college{c13zcS3bWGtWgeGYf6qQ38-reby.QX1ITO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that shell commands can take multiple arugments and also that arguments can also take arguments.
   
### Refference :-
   None.


 # **3.<ins>Reading manuals</ins>**:-
   The challenge asks us to read the manual of the `challenge` and invoke the it with a secret option to get the flag.
   
## My solve:-
   **My flag** :-``

   So, the challenge asked us to get the flag by invoking the `/challenge` with a secret option which we have to find in the manual of the `challenge` by using the `man` command, hence i opened the shell and used the `man` command with `challenge` as the 
   ```bash
   
   ```

### What i learned:-
   I learned that shell commands can take multiple arugments and also that arguments can also take arguments.
   
### Refference :-
   None.


 # **3.<ins>Learning complex usage</ins>**:-
   The challenge gives us to read the manual of the `challenge` and invoke the it with a secret option to get the flag.
   
## My solve:-
   **My flag** :-``

   So, the challenge asked us to get the flag by invoking the `/challenge` with a secret option which we have to find in the manual of the `challenge` by using the `man` command, hence  
   ```bash
   
   ```

### What i learned:-
   I learned that shell commands can take multiple arugments and also that arguments can also take arguments.
   
### Refference :-
   None.
