# **1.<ins>Printing variables</ins>**:-
   The challenge asks us to have our shell print out the `FLAG` variable which contains the flag.
## My solve:-
   **My flag** :-`pwn.college{Y02karUUgCfuVUzlw2Fp2hMdk8-.QX3UTN0wCNxAzNzEzW}`

   So, the challenge asked us to print the variable `FLAG` whcih contains the flag, hence i opened the shell and used the `echo` command abd passed `$` along with the variable and got the flag.
   ```bash
   hacker@variables~printing-variables:~$ echo $FLAG
   pwn.college{Y02karUUgCfuVUzlw2Fp2hMdk8-.QX3UTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that shell has variables and we can print them by prepending the variable name with a `$` in the `echo` command.

### Refference :-
   None


# **2.<ins>Setting variables</ins>**:-
   The challenge asks us to set the `PWN` variable to the value `COLLEGE` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{o2F6CCtn29k5bPdYJ6t3oz8aV3x.QX5UTN0wCNxAzNzEzW}`

   So, the challenge asked us to set the `PWN` variable to the value `COLLEGE` to get the flag, hence i opened the shell and used the `=` to assign the value `COLLEGE` to the variable `PWN` and got the flag.
   ```bash
   hacker@variables~setting-variables:~$ PWN=COLLEGE
   You've set the PWN variable properly! As promised, here is the flag:
   pwn.college{o2F6CCtn29k5bPdYJ6t3oz8aV3x.QX5UTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `=` i used to store values in variables without providing space on bothe side of the operator e.g, `VAR=1337`, also `$` is not used here because the `$` is only prepended to access variables, i also learned that the prepending of `$` triggers what is called variable expansion, which is, surprisingly, the source of many potential vulnerabilities.

### Refference :-
   None


# **3.<ins>Multi-word variables</ins>**:-
   The challenge asks us to set the variable `PWN` to `COLLEGE YEAH`.
## My solve:-
   **My flag** :-`pwn.college{UrvqErZCfAhWhp5_z4TmHESXLh7.QXwYTN0wCNxAzNzEzW}`

   So, the challenge asked us to set the variable `PWN` to `COLLEGE YEAH`, hence i opened the shell and assigned the value `COLLEGE YEAH` to the variable `PWN` by quoting the whole value in double quote and got the flag.
   ```bash
   hacker@variables~multi-word-variables:~$ PWN="COLLEGE YEAH"
   You've set the PWN variable properly! As promised, here is the flag:
   pwn.college{UrvqErZCfAhWhp5_z4TmHESXLh7.QXwYTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that if we want to give space in the value that we are assigning to the variable then we have to enter the whole value in double quotes `""`.

### Refference :-
   None


# **4.<ins>Exploring variables</ins>**:-
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



# **5.<ins></ins>**:-
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
