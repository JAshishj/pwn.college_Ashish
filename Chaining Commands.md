# **1.<ins>Chaining with semicolons</ins>**:-
   In this challenge, you must run `/challenge/pwn` and then `/challenge/college`, chaining them with a semicolon.
## My solve:-
   **My flag** :-`pwn.college{0ctuS4hVp1VFuo77o7PY1G5wZmw.QX1UDO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/pwn` and then `/challenge/college` by chaining them, hence i opened the shell and ran `/challenge/pwn` and then `/challenge/college` by using `;` to chain them and got the flag.
   ```bash
   hacker@chaining~chaining-with-semicolons:~$ /challenge/pwn; /challenge/college
   Yes! You chained /challenge/pwn and /challenge/college! Here is your flag:
   pwn.college{0ctuS4hVp1VFuo77o7PY1G5wZmw.QX1UDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the easiest way to chain commands is `;`. In most contexts, `;` separates commands in a similar way to how Enter separates lines and that when we hit Enter, our shell executes your typed command and, after that command terminates, gives us the prompt to input another command. The semicolon is analogous, just without the prompt and with us entering both commands before anything is executed.

### Refference :-
   None


# **2.<ins>Building on success</ins>**:-
   In this challenge, you need to chain the programs `/challenge/first-success` and `/challenge/second` using the `&&` operator. Try running each command separately first to see what happens (which is that you will not get the flag). But if you chain them with &&, the flag will appear.
## My solve:-
   **My flag** :-`pwn.college{YZho_wkwhPUu7kSvn7DMIx2RL7S.0lM0MDOxwCNxAzNzEzW}`

   So, the challenge asked us to chain the programs `/challenge/first-success` and `/challenge/second` using the `&&` operator, hence i opened the shell and used the `&&` operator and chained `/challenge/first-success` and `/challenge/second` together and got the flag.
   ```bash
   hacker@chaining~building-on-success:~$ /challenge/first-success && /challenge/second
   Nice chaining! Flag: pwn.college{YZho_wkwhPUu7kSvn7DMIx2RL7S.0lM0MDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `&&` operator allows you to run a second command only if the first command succeeds (in Linux convention, this means it exited with code 0). This is called the "AND" operator because both conditions must be true: the first command must succeed AND then the second command will run, and that this is super useful for complex commandline workflows where certain actions depend on the success of other actions, it's syntax is:`hacker@dojo:~$ command1 && command2` and that this means: "Run command1, and IF it succeeds, then run command2.".

### Refference :-
   None


# **3.<ins>Handling failure</ins>**:-
   In this challenge, you need to chain `/challenge/first-failure` and `/challenge/second` using the `||` operator. 
## My solve:-
   **My flag** :-`pwn.college{UyeP4VbuNNzJFdGgHuJU4O8c4N7.01M0MDOxwCNxAzNzEzW}`

   So, the challenge asked us to  chain `/challenge/first-failure` and `/challenge/second` using the `||` operator, hence i opened the shell and used the `||` operator abd chained `/challenge/first-failure` and `/challenge/second` together and got the flag.
   ```bash
   hacker@chaining~handling-failure:~$ /challenge/first-failure || /challenge/second
   Nice chaining! Flag: pwn.college{UyeP4VbuNNzJFdGgHuJU4O8c4N7.01M0MDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `||` operator allows you to run a second command only if the first command fails (exits with a non-zero code). This is called the "OR" operator because either the first command succeeds OR the second command will run, and that it's syntax is: `hacker@dojo:~$ command1 || command2`, this means: "Run command1, and IF it fails, then run command2."

### Refference :-
   None


# **4.<ins>Your first shell script</ins>**:-
   Same as last challenge, run `/challenge/pwn` and then `/challenge/college`, but this time in a shell script called `x.sh`, then run it with `bash`.
## My solve:-
   **My flag** :-`pwn.college{IC9YNkMCZiA4LPvQyQDLgFo8Xez.QXxcDO0wCNxAzNzEzW}`
   
   So, the challenge asked us to  run `/challenge/pwn` and then `/challenge/college` in a shell script called `x.sh`, hence i opened the shell and created `x.sh` shell script which contained `/challenge/pwn` and `/challenge/college` using `nano` command and the ran it with `bash` and got the flag.
   ```bash
   hacker@chaining~your-first-shell-script:~$ nano x.sh
   hacker@chaining~your-first-shell-script:~$ bash x.sh
   Great job, you've written your first shell script! Here is the flag:
   pwn.college{IC9YNkMCZiA4LPvQyQDLgFo8Xez.QXxcDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that as we combine more and more commands to achieve complex effects, the length of the combined prompt quickly gets really annoying to deal with. When this happens, we can put these commands in a file, called a shell script, and run them by executing the file, and that we can execute by passing it as an argument to a new instance of our shell (bash)! and When a shell is invoked like this, rather than taking commands from the user, it reads commands from the file.

### Refference :-
   None


# **5.<ins>Redirecting script output</ins>**:-
   In this challenge, we will practice piping `|` from our script to another program. Like before, you need to create a script that calls the `/challenge/pwn` command followed by the `/challenge/college` command, and pipe the output of the script into a single invocation of the `/challenge/solve` command!
## My solve:-
   **My flag** :-`pwn.college{cijVoG8Yqmg45X9Op53N3Mm8zdo.QX4ETO0wCNxAzNzEzW}`

   So, the challenge asked us to pipe the output of the shell script which invokes `/challenge/pwn` and `/challeneg/college` to `/challenge/solve`, hence i opened the shell and created `x.sh` shell script which contained `/challenge/pwn` and `/challenge/college` using `nano` command and the ran it with `bash` and piped `|` it's output to `/challenge/solve` and got the flag.
   ```bash
   hacker@chaining~your-first-shell-script:~$ nano x.sh
   hacker@chaining~redirecting-script-output:~$ bash x.sh | /challenge/solve
   Correct! Here is your flag:
   pwn.college{cijVoG8Yqmg45X9Op53N3Mm8zdo.QX4ETO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that as far as the shell is concerned, our script is just another command. That means we can redirect its input and output just like we did for commands and that all of the various redirection methods work: i.e `>` for stdout, `2>` for stderr, `<` for stdin, `>>` and `2>>` for append-mode redirection,` >&` for redirecting to other file descriptors, and `|` for piping to another command.

### Refference :-
   None


# **6.<ins>Executable shell scripts</ins>**:-
   The challenge asks us to make a shellscript that will invoke `/challenge/solve`, make it executable, and run it without explicitly invoking `bash`!
## My solve:-
   **My flag** :-`pwn.college{UkdsG1oCyQbpqUsSh89ooS70-x7.QX0cjM1wCNxAzNzEzW}`

   So, the challenge asked us to make a shellscript that will invoke `/challenge/solve` and then make it exeuctable and run it, hence i opened the shell and created `x.sh` shell script which contained `/challenge/solve` using `nano` command and then made it executable by changing it's permission using `chmod` and then ran it and got the flag.
   ```bash
   hacker@chaining~executable-shell-scripts:~$ nano x.sh
   hacker@chaining~executable-shell-scripts:~$ chmod u+x x.sh
   hacker@chaining~executable-shell-scripts:~$ ./x.sh
   Congratulations on your shell script execution! Your flag:
   pwn.college{UkdsG1oCyQbpqUsSh89ooS70-x7.QX0cjM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that when we invoke `bash script.sh`, we are, of course launching the `bash` command with the `script.sh` argument. This tells bash to read its commands from `script.sh` instead of standard input, and thus your shell script is executed and It turns out that we can avoid the need to manually invoke `bash`. If our shell script file is executable, we can simply invoke it via its relative or absolute path.

### Refference :-
   None


# **7.<ins>Understanding shebangs</ins>**:-
   For this challenge, create a script at `/home/hacker/solve.sh` that has a proper `shebang` and outputs "hack the planet". Remember to make it executable, then run `/challenge/run` to verify your script works correctly.
## My solve:-
   **My flag** :-`pwn.college{cUxKFKxeyytqc2jptecaAKyHkZi.0VOzMDOxwCNxAzNzEzW}`

   So, the challenge asked us to create a script at `/home/hacker/solve.sh` that has a proper `shebang` and outputs "hack the planet" make it executable, then run `/challenge/run`, hence i opened the shell and created `solve.sh` shell script which outputs "hack the planet"  using `nano` command and then made it executable by changing it's permission using `chmod` and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@chaining~understanding-shebangs:~$ nano solve.sh
   hacker@chaining~understanding-shebangs:~$ chmod u+x solve.sh
   hacker@chaining~understanding-shebangs:~$ /challenge/run
   Testing your script...
   Perfect! Your flag:
   Flag: pwn.college{cUxKFKxeyytqc2jptecaAKyHkZi.0VOzMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that when a program is invoked in Linux, the Linux kernel first inspects the file to determine how it should be run. This does NOT use the extension (which is why you don't have to name your shell scripts with a .sh extension, or your Python scripts with a .py extension, or so on). Rather, Linux looks at the first few bytes of the file for this information, and that there are a bunch of different types of programs, but if the program file starts with the characters #! (often termed a "shebang"), Linux treats the file as an interpreted program, and the contents of the rest of the line as the path to the interpreter. It then invokes the interpreter with the path to the program file as its only argument.

### Refference :-
   None


# **8.<ins>Scripting with arguments</ins>**:-
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


# **9.<ins></ins>**:-
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
