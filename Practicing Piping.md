# **1.<ins>Redirecting output</ins>**:-
   The challenge asks us to use the output redirection to write the word `PWN` to the filename `COLLEGE` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{UvxSts1a6HBlDwgfEUO1KQC_oe6.QX0YTN0wCNxAzNzEzW}`

   So, the challenge asked us to use the output redirection to write the word `PWN` to the filename `COLLEGE`, hence i opened the shell and used the `echo` command and used `>` between the arguments `PWN` and `COLLEGE`, which redirects the `PWN` to the file `COLLEGE` and got the flag.
   ```bash
   hacker@piping~redirecting-output:~$ echo PWN > COLLEGE
   Correct! You successfully redirected 'PWN' to the file 'COLLEGE'! Here is your
   flag:
   pwn.college{UvxSts1a6HBlDwgfEUO1KQC_oe6.QX0YTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `>` is used between the the arguments to redirect the outputs.

### Refference :-
   None


# **2.<ins>Redirecting more output</ins>**:-
   The challenge asks us to redireact the output of `/challenge/run` which will once more give you a flag to the file `myflag` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{kEAVD9iUG2EHgaqD7--BZBOb38r.QX1YTN0wCNxAzNzEzW}`

   So, the challenge asked us to use the output redirection to redirect the output of `/challenge/run` to `myflag`, hence i opened the shell andinvoked the `/challenge/run` command and used `>` between it and `myfile`, which redirects the the output to the file `myflag` and got the flag.
   ```bash
   hacker@piping~redirecting-more-output:~$ /challenge/run > myflag
   [INFO] WELCOME! This challenge makes the following asks of you:
   [INFO] - the challenge will check that output is redirected to a specific file path : myflag
   [INFO] - the challenge will output a reward file if all the tests pass : /flag
   [HYPE] ONWARDS TO GREATNESS!
   [INFO] This challenge will perform a bunch of checks.
   [INFO] If you pass these checks, you will receive the /flag file.
   [TEST] You should have redirected my stdout to a file called myflag. Checking...
   [PASS] The file at the other end of my stdout looks okay!
   [PASS] Success! You have satisfied all execution requirements.
   hacker@piping~redirecting-more-output:~$ cat ./myflag
   [FLAG] Here is your flag:
   [FLAG] pwn.college{kEAVD9iUG2EHgaqD7--BZBOb38r.QX1YTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `>` is used between the the arguments to redirect the outputs of any commands.

### Refference :-
   None
