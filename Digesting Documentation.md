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
   **My flag** :-`pwn.college{A_xlqRk7RORAaBR4g5LdCeuCpCU.QX0EDO0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the `/challenge` with a secret option which we have to find in the manual of the `challenge` by using the `man` command, hence i opened the shell and used the `man` command with `challenge` as it's argument and read through it and found the secret option is `--xlqkag NUM` with the description that it would give the flag if the NUM was 745, hecne i invoked `/challenge/challenge` which was the name given in he manual and provided it with the option `--xlqkag 745` and got the flag. 
   ```bash
   hacker@man~reading-manuals:~$ man challenge
   hacker@man~reading-manuals:~$ /challenge/challenge --xlqkag 745
   Correct usage! Your flag: pwn.college{A_xlqRk7RORAaBR4g5LdCeuCpCU.QX0EDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `man` commands invoked with the name of the command we want the manual of as an argument provides the full manual of that command in the shell, i also learned that it only works if we provide the name and not the path and that we can scroll through the manual using the up/dowm arrow key and use `q` to quit.
   
### Refference :-
   None.


 # **4.<ins>Searching manuals</ins>**:-
   The challenge asks us to find the option that will give us the flag by reading the `challenge` manual page.
   
## My solve:-
   **My flag** :-`pwn.college{8os_oXfAAvQAmOK0ckhjKs75JzH.QX1EDO0wCNxAzNzEzW}`

   So, the challenge asked us to find the option that would give the flag by reading the manual of the `challenge`, hence i opened the shell and used the `man` command along with the `challenge` as the argument to get the manual of the `challenge` and then used `/` to search word `flag` in the manual as the description of the correct option should have the word `flag` in it and then got the option `--ko` in the second result which i got by hitting `n` whose description said that it would give the flag hence i invoked `/challenge/challenge` with the `--ko` argument and gor the flag.
   ```bash
   hacker@man~searching-manuals:~$ man challenge
   hacker@man~searching-manuals:~$ /challenge/challenge  --ko
   Initializing...
   Correct usage! Your flag: pwn.college{8os_oXfAAvQAmOK0ckhjKs75JzH.QX1EDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can scroll through the manual using the up/dowm arrow key and use `q` to quit and use the `/` to search and `?` to search backwards and hit `n` to go to the next result and `N` to go to the previous result.
   
### Refference :-
   None.


# **5.<ins>Searching for manuals</ins>**:-
   The challenge asks us to find the hidden challenge man page which will tell us how to use `/challenge/challenge` by reading the `man` page manual by doing: `man man` then get the flag.
   
## My solve:-
   **My flag** :-`pwn.college{kC0jL8gk9q9ZtaWJrw7H8gZbG9a.QX2EDO0wCNxAzNzEzW}`

   So, the challenge asked us to find the hidden challenge man page by reading the `man` manual page  by using the `man man` command which would tell me how to ues the `/challenge/challenge` to get the flag hence i opened the shell and used the `man man` command where i found a option `-k` which would take a word or phrase and print out all the manual which contain that word or phrase in it's name or description hence i gave it the string `challenge` by looking at the hint provided by the challenge and found that `kjgkqtarwg` is the name of the hidden man page hence i read it using the `man` command and got the by using `-- kjgkqt NUM` with the description that it would give the flag if the NUM was 089, hecne i invoked `/challenge/challenge` which was the name given in he manual and provided it with the option `--kjgkqt 089` and got the flag.
   ```bash
   hacker@man~searching-for-manuals:~$ man man
   hacker@man~searching-for-manuals:~$ man -k challenge
   kjgkqtarwg (1)       - print the flag!
   hacker@man~searching-for-manuals:~$ man kjgkqtarwg
   hacker@man~searching-for-manuals:~$ /challenge/challenge --kjgkqt 089
   Correct usage! Your flag: pwn.college{kC0jL8gk9q9ZtaWJrw7H8gZbG9a.QX2EDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can read the manual page of `man` by using `man man` command which would teach us advanced usage of the `man` command itself, i also learned that `man` command has many options as arguments which can help us get the required manual very easily.
   
### Refference :-
   None.


 # **6.<ins>Helpful programs</ins>**:-
   The challenge asks us to use the `--help` option to get the programs documentation and then get the flag.
   
## My solve:-
   **My flag** :-`pwn.college{gBLq72whpFAEECboebB_u4FionX.QX3IDO0wCNxAzNzEzW}`

   So, the challenge asked us to use the `--help` option to get the documentaion of the program, hence i opened the shell and entered the `/challenge/challenge` along with the option `--help` and got it's documentation, there there were two options which were requiered to get the flag those are `-g` which would give the flag if provided with correct value and `-p` which would print the the value requiered by the `-g` option to print the flag, hence i first used the `-p` option which gave me the value 724 and then i used the `-g` option and provided it with this value and got the flag.
   ```bash
   hacker@man~helpful-programs:~$ /challenge/challenge --help
   usage: a challenge to make you ask for help [-h] [--fortune] [-v] [-g GIVE_THE_FLAG] [-p]
   optional arguments:
      -h, --help            show this help message and exit
      --fortune             read your fortune
      -v, --version         get the version number
      -g GIVE_THE_FLAG, --give-the-flag GIVE_THE_FLAG, get the flag, if given the correct value
      -p, --print-value     print the value that will cause the -g option to give you the flag}
   hacker@man~helpful-programs:~$ /challenge/challenge -p
   The secret value is: 724
   hacker@man~helpful-programs:~$ /challenge/challenge -g 724
   Correct usage! Your flag: pwn.college{gBLq72whpFAEECboebB_u4FionX.QX3IDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we could also get the documentation of a program by using the `--help` option along with it.
   
### Refference :-
   None.

