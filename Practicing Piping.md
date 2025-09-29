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
   The challenge asks us to run `/challenge/run` which will output the flag to stdout, but it will also output over 1000 decoy flags containing the word `DECOY` somewhere in the flag which are mixed in with the real flag and we'll need to filter out the decoys while keeping the real flag by using `grep -v` to filter out all the lines containing `DECOY` and get the real flag.
## My solve:-
   **My flag** :-`pwn.college{sqDX0RzenOT1vlEwK8AzclENKSx.0FOxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` which will output the flag to stdout along with over 1000 decoy flags containing the word `DECOY` and we have to use the `grep -v` command to filter out all the lines containing `DECOY` and get the real flag, hence i opened the shell and ran `/challenge/run` and provided it's output to `grep` by using `|` pipe operator and used the `-v` option of grep to fillter out all the lines containing `DECOY` and got the flag.
   ```bash
   hacker@piping~filtering-with-grep-v:~$ /challenge/run | grep -v DECOY
   pwn.college{sqDX0RzenOT1vlEwK8AzclENKSx.0FOxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `grep` has a option `-v` (invert match), which shows lines that do not match a pattern which is the opposite of the normal `grep` command.

### Refference :-
   None


# **10.<ins>Duplicating piped data using tee</ins>**:-
   The challenge asks us to run `/challenge/pwn` which must be piped into `/challenge/college`, but we'll need to intercept the data to see what `pwn` needs from us to get the flag.
## My solve:-
   **My flag** :-`pwn.college{I2B3OdgAu0NHmQ-KzBceFzWuFzY.QXxITO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/pwn` which must be piped into `/challenge/college`, but we'll need to intercept the data to see what `pwn` needs from us to get the flag, hence i opened the shell and ran `/challenge/pwn` and piped and used `tee` command  to `/challenge/challenge` so that i could know what the program needed so that it can present the flag and got `I2B3OdgA` as the option to be passed hence i passed the option and piped it to the `/challenge/college` and got the flag.
   ```bash
   hacker@piping~duplicating-piped-data-with-tee:~$ /challenge/pwn | tee /challenge/challenge | /challenge/college
   Processing...
   The input to 'college' does not contain the correct secret code! This code
   should be provided by the 'pwn' command. HINT: use 'tee' to intercept the
   output of 'pwn' and figure out what the code needs to be.
   hacker@piping~duplicating-piped-data-with-tee:~$ cat /challenge/challenge
   Usage: /challenge/pwn --secret [SECRET_ARG]

   SECRET_ARG should be "I2B3OdgA"
   hacker@piping~duplicating-piped-data-with-tee:~$ /challenge/pwn --secret I2B3OdgA | /challenge/college
   Processing...
   Correct! Passing secret value to /challenge/college...
   Great job! Here is your flag:
   pwn.college{I2B3OdgAu0NHmQ-KzBceFzWuFzY.QXxITO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `tee` command duplicates data flowing through our pipes to any number of files provided on the command line.

### Refference :-
   None


# **11.<ins>Process substitution for input</ins>**:-
   The challenge asks us to `diff` two sets of command outputs: `/challenge/print_decoys`, which will print a bunch of decoy flags, and `/challenge/print_decoys_and_flag` which will print those same decoys plus the real flag use process substitution with `diff` to compare the outputs of these two programs to get the flag.
## My solve:-
   **My flag** :-`pwn.college{YBVR3Rw811al2LvkXeXAJxnBz6U.0lNwMDOxwCNxAzNzEzW}`

   So, the challenge asked us to `diff` two sets of command outputs: `/challenge/print_decoys`, which will print a bunch of decoy flags, and `/challenge/print_decoys_and_flag` which will print those same decoys plus the real flag using process substitution, hence i opened the shell and used the `diff` command and used process substitution `<( )` on `/challeng/print_decoys` and `/challenge/print_decoys_and_flag` to directly provide there output to the `diff` command and got the flag.
   ```bash
   hacker@piping~process-substitution-for-input:~$ diff <(/challenge/print_decoys) <(/challenge/print_decoys_and_flag)
   28a29
   > pwn.college{YBVR3Rw811al2LvkXeXAJxnBz6U.0lNwMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that linux follows the philosophy that "everything is a file". That is, the system strives to provide file-like access to most resources, including the input and output of running programs! The shell follows this philosophy, allowing you to, for example, use any utility that takes file arguments on the command line and hook it up to the output of programs, as you learned in the previous few levels.I also learned that  we can go further, and hook input and output of programs to arguments of commands. This is done using Process Substitution using `<(command)` and  when we write `<(command)`, bash will run the command and hook up its output to a temporary file that it will create and that this isn't a real file, it's what's called a named pipe, in that it has a file name.

### Refference :-
   None


# **12.<ins>Writing to multiple programs</ins>**:-
   In this challenge we have `/challenge/hack`, `/challenge/the`, and `/challenge/planet` and we have to run the `/challenge/hack command`, and duplicate its output as input to both the `/challenge/the` and the `/challenge/planet` commands to get the flag.
## My solve:-
   **My flag** :-`pwn.college{EM-q3meC97e7iQesYRcP57gB-eb.QXwgDN1wCNxAzNzEzW}`

   So, the challenge asked us to run the `/challenge/hack command`, and duplicate its output as input to both the `/challenge/the` and the `/challenge/planet` commands, hence i opened the shell and ran `/challenge/hack command` and provided it's output to both `/challenge/the` and `/challenge/planet` as their inputs using the `tee` command and process substitution for input and got the flag.
   ```bash
   hacker@piping~writing-to-multiple-programs:~$ /challenge/hack | tee >(/challenge/the) >(/challenge/planet)
   This secret data must directly and simultaneously make it to /challenge/the and
   /challenge/planet. Don't try to copy-paste it; it changes too fast.
   2613422961436424292
   Congratulations, you have duplicated data into the input of two programs! Here
   is your flag:
   pwn.college{EM-q3meC97e7iQesYRcP57gB-eb.QXwgDN1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that for writing to a command output process substitution we have to use `>(command)`, i also learned that we can use the `tee` command and process substitution for input to provide the output of one program as the input to many programs.

### Refference :-
   None


# **13.<ins>Split-piping stderr and stdout</ins>**:-
   The challenge asks us to combine our knowledge of `>()`, `2>`, and `|` and provided the following data:- `/challenge/hack`: this produces data on stdout and stderr `/challenge/the`: you must redirect hack's stderr to this program `/challenge/planet`: you must redirect hack's stdout to this program to get the flag.
## My solve:-
   **My flag** :-`pwn.college{sVZlYelMNmiK7R47RyxZRVSstgc.QXxQDM2wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/hack` which gives data on stdout and stderr, and then redirect hack's stderr `/challenge/the`, and redirect hack's stdout to `/challenge/planet`, hence i opened the shell and ran `/challenge/hack` and `|` to provide it's output to both the files and used`2>` and  `>()` to respective file to provide it with stderr of `/challenge/hack` and stdout of `/challenge/hack` respectively and got the flag.
   ```bash
   hacker@piping~split-piping-stderr-and-stdout:~$ /challenge/hack 2> >(/challenge/the) | /challenge/planet
   Congratulations, you have learned a redirection technique that even experts
   struggle with! Here is your flag:
   pwn.college{sVZlYelMNmiK7R47RyxZRVSstgc.QXxQDM2wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that how to redirect the stderr and stout of the same command by using pipe.

### Refference :-
   None


# **14.<ins>Named pipes</ins>**:-
   The challenge asks us to create a `/tmp/flag_fifo` file and redirect the stdout of `/challenge/run` to it and if we're successful, `/challenge/run` will write the flag into the FIFO. 
## My solve:-
   **My flag** :-``

   So, the challenge asked us to create a `/tmp/flag_fifo` file and redirect the stdout of `/challenge/run`, hence i opened the shell and crated the FIFO `/tmp/flag_fifo` using the `mkfifo` command and then redirected the output of `/challenge/run` to it and catted it, and got the flag. 
   ```bash
  
   ```

### What i learned:-
   I learned that we can also create our own persistent named pipes that stick around on the filesystem and that these are called FIFOs, which stands for First (byte) In, First (byte) Out.I also learned that we can create a FIFO using the `mkfifo` command.I also came to know that, we control where FIFOs are created and that, they persist until we delete them, and any process can write to them by path, and that we can see them with `ls` and examine them like files,and that FIFOs pass data directly between processes in memory - nothing is saved to disk meaning that, once data is read from a FIFO, it's gone and also that writers block until the readers are ready, and vice-versa.

### Refference :-
   None
