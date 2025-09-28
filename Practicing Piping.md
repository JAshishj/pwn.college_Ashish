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

   So, the challenge asked us to use the output redirection to redirect the output of `/challenge/run` to `myflag`, hence i opened the shell and invoked the `/challenge/run` command and used `>` between it and `myfile`, which redirects the the output to the file `myflag` and got the flag.
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


# **3.<ins>Appending output</ins>**:-
   The challenge asks us to run `/challenge/run` with an append-mode redirect `>>` of the output to the file `/home/hacker/the-flag` which will write the first half of the flag to the file, and the second half to stdout if stdout is redirected to the file to get the flag.
## My solve:-
   **My flag** :-`pwn.college{wyBRkuiV46CRT3wvEV_uhiOlVzE.QX3ATO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` with an append-mode redirect `>>` of the output to the file `/home/hacker/the-flag`, hence i opened the shell and ran `/challenge/run` with `>>` and redirected it's output to `/home/hacker/the-flag` and got the flag.
   ```bash
   hacker@piping~appending-output:~$ /challenge/run >> /home/hacker/the-flag
   [INFO] WELCOME! This challenge makes the following asks of you:
   [INFO] - the challenge will check that output is redirected to a specific file path : /home/hacker/the-flag

   [HYPE] ONWARDS TO GREATNESS!
   [INFO] This challenge will perform a bunch of checks.
   [INFO] Good luck!

   [TEST] You should have redirected my stdout to a file called /home/hacker/the-flag. Checking...

   [HINT] File descriptors are inherited from the parent, unless the FD_CLOEXEC is set by the parent on the file descriptor.
   [HINT] For security reasons, some programs, such as python, do this by default in certain cases. Be careful if you are
   [HINT] creating and trying to pass in FDs in python.

   [PASS] The file at the other end of my stdout looks okay!
   [PASS] Success! You have satisfied all execution requirements.
   I will write the flag in two parts to the file /home/hacker/the-flag! I'll do
   the first write directly to the file, and the second write, I'll do to stdout
   (if it's pointing at the file). If you redirect the output in append mode, the
   second write will append to (rather than overwrite) the first write, and you'll
   get the whole flag!

   hacker@piping~appending-output:~$  cat /home/hacker/the-flag
   |
   \|/ This is the first half:
    v
   pwn.college{wyBRkuiV46CRT3wvEV_uhiOlVzE.QX3ATO0wCNxAzNzEzW}
                               ^
      that is the second half /|\
                               |
   If you only see the second half above, you redirected in *truncate* mode (>)
   rather than *append* mode (>>), and so the write of the second half to stdout
   overwrote the initial write of the first half directly to the file. Try append
   mode!
   ```

### What i learned:-
   I learned that `>>` is used between the the arguments to redirect the outputs.

### Refference :-
   None


# **4.<ins>Redirecting errors</ins>**:-
   The challenge asks us to redirect the output of `/challenge/run`, like before, to `myflag`, and the "errors" in our case, the instructions to `instructions`but there will be nothing printed to the terminal, because we have redirected everything and we can find the instructions/feedback in `instructions` and the flag in `myflag`.
## My solve:-
   **My flag** :-`pwn.college{gCJ-T2rvbjCBfJmBmnVLPJtsSWr.QX3YTN0wCNxAzNzEzW}`

   So, the challenge asked us to redirect the output of `/challenge/run` to `myflag`, and the "errors" to `instructions` and get the instructions from `instructions` and the flag from `myflag`, hence i opened the shell and redirected the output and errors of `/challenge/run` to `myflag` and `instructions` respectively using `>` and `2>` respectively, then i read the `myflag` and got the flag.
   ```bash
   hacker@piping~redirecting-errors:~$ /challenge/run > myflag 2> instructions
   hacker@piping~redirecting-errors:~$ cat myflag
   [FLAG] Here is your flag:
   [FLAG] pwn.college{gCJ-T2rvbjCBfJmBmnVLPJtsSWr.QX3YTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that just like standard output, we can also redirect the error channel of commands.I also learened taht a File Descriptor (FD) is a number that describes a communication channel in Linux i.e FD 0: Standard Input, FD 1: Standard Output, FD 2: Standard Error.When we redirect process communication, we do it by FD number, though some FD numbers are implicit. For example, a `>` without a number implies `1>`, which redirects FD 1 (Standard Output). i also came to know that we can redirect multiple file descriptors at the same time.

### Refference :-
   None


# **5.<ins>Redirecting input</ins>**:-
   The challenge asks us to 
## My solve:-
   **My flag** :-`pwn.college{Qr46vuRvValrhVljEIda1cMlgwP.QXwcTN0wCNxAzNzEzW}`

   So, the challenge asked us to use `/challenge/run`, which will require us to redirect the `PWN` file to it and have the `PWN` file contain the value `COLLEGE` and to write that value to the `PWN `file, recall the prior challenge on output redirection from echo, hence i opened the shell and first redirected `COLLEGE` to the `PWN` file and the redirected it to `/challenge/run` using `<` and got the flag.
   ```bash
   hacker@piping~redirecting-input:~$ echo COLLEGE > PWN
   hacker@piping~redirecting-input:~$ /challenge/run < PWN
   Reading from standard input...
   Correct! You have redirected the PWN file into my standard input, and I read
   the value 'COLLEGE' out of it!
   Here is your flag:
   pwn.college{Qr46vuRvValrhVljEIda1cMlgwP.QXwcTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that just like how we can redirect output from programs, we can also redirect input to programs whichis done using `<`. 

### Refference :-
   None


# **6.<ins>Grepping stored results</ins>**:-
   The challenge asks us to redirect the output of `/challenge/run` to `/tmp/data.txt` this will result in a hundred thousand lines of text, with one of them being the flag in `/tmp/data.txt` and then grep that for the flag.
## My solve:-
   **My flag** :-`pwn.college{Q-p-lh76p_4FdNPTb8ndKhNPBUa.QX4EDO0wCNxAzNzEzW}`

   So, the challenge asked us to redirect the output of `/challenge/run` to `/tmp/data.txt` and grep the flag from it, hence i opened the shell and redirected the outpu of `/challenge/run` to `/tmp/data.txt` and then greped all the words containing the string `pwn.college` as all the flag starts from it and got the flag.
   ```bash
   hacker@piping~grepping-stored-results:~$ /challenge/run > /tmp/data.txt
   [INFO] WELCOME! This challenge makes the following asks of you:
   [INFO] - the challenge will check that output is redirected to a specific file path : /tmp/data.txt
   [INFO] - the challenge will output a reward file if all the tests pass : /challenge/.data.txt

   [HYPE] ONWARDS TO GREATNESS!
   [INFO] This challenge will perform a bunch of checks.
   [INFO] If you pass these checks, you will receive the /challenge/.data.txt file.

   [TEST] You should have redirected my stdout to a file called /tmp/data.txt. Checking...

   [HINT] File descriptors are inherited from the parent, unless the FD_CLOEXEC is set by the parent on the file descriptor.
   [HINT] For security reasons, some programs, such as python, do this by default in certain cases. Be careful if you are
   [HINT] creating and trying to pass in FDs in python.

   [PASS] The file at the other end of my stdout looks okay!
   [PASS] Success! You have satisfied all execution requirements.
   hacker@piping~grepping-stored-results:~$ grep pwn.college /tmp/data.txt
   pwn.college{Q-p-lh76p_4FdNPTb8ndKhNPBUa.QX4EDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can use other commands on the file to which we redirected the output to, to performe various programs.

### Refference :-
   None


# **7.<ins>Grepping live output</ins>**:-
   The challenge asks us to run `/challenge/run` which will output a hundred thousand lines of text, including the flag and then grep for the flag using the `|` pipe operator.
## My solve:-
   **My flag** :-`pwn.college{UghwyIWFxZKOX6wOBiaGJRVBvk7.QX5EDO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` which will output a hundred thousand lines of text, including the flag and then grep for the flag using the `|` pipe operator, hence i opened the shell and ran the `/chaallenge/run` along with the `|` operator and used it's output to grep all the words containing the string `pwn.college` as all the flag starts from it and got the flag.
   ```bash
   hacker@piping~grepping-live-output:~$ /challenge/run | grep pwn.college
   [INFO] WELCOME! This challenge makes the following asks of you:
   [INFO] - the challenge checks for a specific process at the other end of stdout : grep
   [INFO] - the challenge will output a reward file if all the tests pass : /challenge/.data.txt

   [HYPE] ONWARDS TO GREATNESS!

   [INFO] This challenge will perform a bunch of checks.
   [INFO] If you pass these checks, you will receive the /challenge/.data.txt file.

   [TEST] You should have redirected my stdout to another process. Checking...
   [TEST] Performing checks on that process!

   [INFO] The process' executable is /nix/store/8b4vn1iyn6kqiisjvlmv67d1c0p3j6wj-gnugrep-3.11/bin/grep.
   [INFO] This might be different than expected because of symbolic links (for example, from /usr/bin/python to /usr/bin/python3 to /usr/bin/python3.8).
   [INFO] To pass the checks, the executable must be grep.

   [PASS] You have passed the checks on the process on the other end of my stdout!
   [PASS] Success! You have satisfied all execution requirements.
   pwn.college{UghwyIWFxZKOX6wOBiaGJRVBvk7.QX5EDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can "cut out the middleman" and avoid the need to store results to a file, like we did before wecan do this by using the `|` (pipe) operator which when used the standard output from the command to the left of the pipe will be connected to (piped into) the standard input of the command to the right of the pipe.

### Refference :-
   None


# **8.<ins>Grepping errors</ins>**:-
   The challenge asks us to run `/challenge/run` which will overwhelm us with output, but this time on standard error and we have to grep through it to find the flag using the `|` and `>&` operators.
## My solve:-
   **My flag** :-`pwn.college{cByYWGb7a8QRM8tXCRHj7M4ZZ2j.QX1ATO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` which will overwhelm us with output, but this time on standard error and we have to grep through it to get the flag using the `|` and `>&` operators, hence i opened the shell and ran `/challenge/run` and redirected it's standard error to standard output using `>&` operator and used `|` operator and used it's output to grep all the words containing the string `pwn.college` as all the flag starts from it and got the flag.
   ```bash
   hacker@piping~grepping-errors:~$ /challenge/run 2>&1 | grep pwn.college
   [INFO] WELCOME! This challenge makes the following asks of you:
   [INFO] - the challenge checks for a specific process at the other end of stderr : grep
   [INFO] - the challenge will output a reward file if all the tests pass : /challenge/.data.txt

   [HYPE] ONWARDS TO GREATNESS!

   [INFO] This challenge will perform a bunch of checks.
   [INFO] If you pass these checks, you will receive the /challenge/.data.txt file.

   [TEST] You should have redirected my stderr to another process. Checking...
   [TEST] Performing checks on that process!

   [INFO] The process' executable is /nix/store/8b4vn1iyn6kqiisjvlmv67d1c0p3j6wj-gnugrep-3.11/bin/grep.
   [INFO] This might be different than expected because of symbolic links (for example, from /usr/bin/python to /usr/bin/python3 to /usr/bin/python3.8).
   [INFO] To pass the checks, the executable must be grep.

   [PASS] You have passed the checks on the process on the other end of my stderr!
   [PASS] Success! You have satisfied all execution requirements.
   pwn.college{cByYWGb7a8QRM8tXCRHj7M4ZZ2j.QX1ATO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `|` operator can only redirect standard output (file descriptor 1), and that the shell has a `>&` operator, which redirects a file descriptor to another file descriptor.

### Refference :-
   None


# **9.<ins>Filtering with grep -v</ins>**:-
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


# **10.<ins></ins>**:-
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
