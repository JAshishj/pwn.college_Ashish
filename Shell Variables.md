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
   I learned that if we want to give space in between the values, then we have to enter the whole value in double quotes `" "`.

### Refference :-
   None


# **4.<ins>Exploring variables</ins>**:-
   The challenge asks us to invoke `/challenge/run` with the `PWN` variable exported and set to the value `COLLEGE`, and the `COLLEGE` variable set to the value `PWN` but not exported to get the flag.
## My solve:-
   **My flag** :-`pwn.college{8JrVbbpX5vUwBlKl2RbSEn5Z32w.QXyYTN0wCNxAzNzEzW}`

   So, the challenge asked us to invoke `/challenge/run` with the `PWN` variable exported and set to the value `COLLEGE`, and the `COLLEGE` variable set to the value `PWN` but not exported, hence i opened the shell and exported the variable `PWN` which had assigned the value `COLLEGE` to it, then i assigned the variable `COLLEGE` with the value `PWN`, then i invoked `/challenge/run` and got the flag.
   ```bash
   hacker@variables~exporting-variables:~$ export PWN=COLLEGE
   You've set the PWN variable to the proper value!
   hacker@variables~exporting-variables:~$ COLLEGE=PWN
   You've set the PWN variable to the proper value!
   You've set the COLLEGE variable to the proper value!
   hacker@variables~exporting-variables:~$ /challenge/run
   CORRECT!
   You have exported PWN=COLLEGE and set, but not exported, COLLEGE=PWN. Great
   job! Here is your flag:
   pwn.college{8JrVbbpX5vUwBlKl2RbSEn5Z32w.QXyYTN0wCNxAzNzEzW}
   You've set the PWN variable to the proper value!
   You've set the COLLEGE variable to the proper value!
   ```

### What i learned:-
   I learned that `export` is used to make the variable useable outside the shell session on which it was assigned, i also learned that when we export our variables, they are passed into the environment variables of child processes.

### Refference :-
   None



# **5.<ins>Printing exported variables</ins>**:-
   The challenge asks us to use the `env` command which will print out every exported variable set in our shell, and we have to look through that output to find the `FLAG` variable!
## My solve:-
   **My flag** :-`pwn.college{oTdQdIrGdqvy6IubtX65VFmSMBy.QX4UTN0wCNxAzNzEzW}`

   So, the challenge asked us to use the `env` command which will print out every exported variable set in our shell, and we have to look through that output to find the `FLAG` variable, hence i opened the shell and used the `env` command and got all the exported variable, and then i found the `FLAG` variable among them and got the flag.
   ```bash
   hacker@variables~printing-exported-variables:~$ env
   SHELL=/run/dojo/bin/bash
   HOSTNAME=variables~printing-exported-variables
   PWD=/home/hacker
   MANPATH=/run/dojo/share/man:
   DOJO_AUTH_TOKEN=bcd1ada7725d6840411d9137359ccc69cdeca4c372cb1a0dc2d4d3a8f54046e4
   HOME=/home/hacker
   LANG=C.UTF-8
   FLAG=pwn.college{oTdQdIrGdqvy6IubtX65VFmSMBy.QX4UTN0wCNxAzNzEzW}
   TERMINFO=/run/dojo/share/terminfo
   TERM=xterm-256color
   SHLVL=2
   LC_CTYPE=C.UTF-8
   SSL_CERT_FILE=/run/dojo/etc/ssl/certs/ca-bundle.crt
   PATH=/run/challenge/bin:/run/dojo/bin:/root/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
   DEBIAN_FRONTEND=noninteractive
   _=/run/dojo/bin/env
   ```

### What i learned:-
   I learned that the `env` command will print out every exported variable set in your shell.

### Refference :-
   None


# **6.<ins>Storing command output</ins>**:-
   The challenge asks us to read the output of the `challenge/run` command directly into a variable called `PWN`, and it will contain the flag.
## My solve:-
   **My flag** :-`pwn.college{MmFIBBUVdEPZtSe3sgF5TZjT6V8.QX1cDN1wCNxAzNzEzW}`

   So, the challenge asked us to read the output of the `/challenge/run` command directly into a variable called `PWN`, and it will contain the flag, hence i opened the shell and used  command substitution to read the output of the `challenge/run` command directly into a variable called `PWN` and the printed the variable `PWN` using the `ecoh` command and got the flag.
   ```bash
   hacker@variables~storing-command-output:~$ PWN=$(/challenge/run)
   Congratulations! You have read the flag into the PWN variable. Now print it out
   and submit it!
   hacker@variables~storing-command-output:~$ echo $PWN
   pwn.college{MmFIBBUVdEPZtSe3sgF5TZjT6V8.QX1cDN1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that command substitution `$()` is often used to store the output of some command into a variable.

### Refference :-
   None


# **7.<ins>Reading input</ins>**:-
   The challenge asks us to to use `read` builtin to set the `PWN` variable to the value `COLLEGE` to get the flag. 
## My solve:-
   **My flag** :-`pwn.college{I2Apt509DBTjmmmgOxrw-BbqqH9.QX4cTN0wCNxAzNzEzW}`

   So, the challenge asked us to to use `read` builtin to set the `PWN` variable to the value `COLLEGE`, hence i opened the shell and used the `read` command and entered the value `COLLEGE` in the standard input and stored that in the variable `PWN` and got the flag. 
   ```bash
   hacker@variables~reading-input:~$ read PWN
   COLLEGE
   You've set the PWN variable properly! As promised, here is the flag:
   pwn.college{I2Apt509DBTjmmmgOxrw-BbqqH9.QX4cTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `read` a builtin command which reads the input provided by the user through the standard input into a variable. 

### Refference :-
   None


# **8.<ins>Reading files</ins>**:-
   The challenge asks us to read `/challenge/read_me` into the `PWN` environment variable in one command to get the flag.
## My solve:-
   **My flag** :-`pwn.college{EanvXit7ktK8J6FBsBTddLh1O6b.QXwIDO0wCNxAzNzEzW}`

   So, the challenge asked us to read `/challenge/read_me` into the `PWN` variable in one command, hence i opened the shell and used the `read` command and redirected `/challenge/read_me`'s input using`<` to `PWN` variable and got the flag.
   ```bash
   hacker@variables~reading-files:~$ read PWN < /challenge/read_me
   You've set the PWN variable properly! As promised, here is the flag:
   pwn.college{EanvXit7ktK8J6FBsBTddLh1O6b.QXwIDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can use `read` command to read a file into an environment variable, using unique ways like redirecting it's input using `<`.

### Refference :-
   None
