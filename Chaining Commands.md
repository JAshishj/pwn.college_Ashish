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
   For this challenge, you need to write a script at `/home/hacker/solve.sh` that: Takes two arguments and Outputs them in REVERSE order (second argument first, then the first argument), and once your script works correctly, run `/challenge/run` to get your flag
## My solve:-
   **My flag** :-`pwn.college{Ukw0TKqklZw6ZTPJSPisxpm-GKO.0VNzMDOxwCNxAzNzEzW}`

   So, the challenge asked us to write a script at `/home/hacker/solve.sh` that: Takes two arguments and Outputs them in REVERSE order and then run `/challenge/run`, hence i opened the shell and created `solve.sh` shell script which takes two arguments and outputs them in reverse order using `nano` command and ran it using `bash` and passed the arguments `college` and `pwn` to check if the script was proper and got the output `pwn college` and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@chaining~scripting-with-arguments:~$ nano solve.sh
   hacker@chaining~scripting-with-arguments:~$ bash solve.sh college pwn
   pwn college
   hacker@chaining~scripting-with-arguments:~$ /challenge/run
   Correct! Your script properly reversed the arguments.
   Here's your flag:
   pwn.college{Ukw0TKqklZw6ZTPJSPisxpm-GKO.0VNzMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that scripts can accept arguments and that the script can access these arguments using special variables: `$1` contains the first argument ("hello"), `$2` contains the second argument ("world"), `$3` would contain the third argument (if there had been one)...and so on.

### Refference :-
   None


# **9.<ins>Scripting with conditionals</ins>**:-
   For this challenge, write a script at `/home/hacker/solve.sh` that: takes one argument and if the argument is "pwn", output "college" and for any other input, output nothing, once your script works correctly, run `/challenge/run` to get your flag!
## My solve:-
   **My flag** :-`pwn.college{wUFsPiujhTDC2nnMKU3RzeE9G8u.0lNzMDOxwCNxAzNzEzW}`

   So, the challenge asked us to write a script at `/home/hacker/solve.sh` that: takes one argument and if the argument is "pwn", output "college" and for any other input output nothing and then run `/challenge/run`, hence i opened the shell and created `solve.sh` shell script which takes one arguments and outputs `college` if the argument is `pwn` and outputs nothing if it is not, using `nano` command and ran it using `bash` and passed the arguments `pwn` to check if the script was proper and got the output `college` and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@chaining~scripting-with-conditionals:~$ nano solve.sh
   hacker@chaining~scripting-with-conditionals:~$ bash solve.sh pwn
   college
   hacker@chaining~scripting-with-conditionals:~$ /challenge/run
   Correct! Your script properly handles all the conditions.
   Here's your flag:
   pwn.college{wUFsPiujhTDC2nnMKU3RzeE9G8u.0lNzMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that in bash, you can use `if` statements to make decisions: The syntax is somewhat unforgiving for a few reasons. First, you must have spaces after `if` (if you're used to a language like C, this is different), after `[`, and before `]`. Second, if, then, and fi must all be on different lines (or separated by semicolons); you can't lump them into the same statement. It's also a bit weird: instead of `endif` or `end` or something like that, the terminator of the `if` statement is `fi` (if backwards). Just something you have to remember.

### Refference :-
   None


# **10.<ins>Scripting with default cases</ins>**:-
   For this challenge, write a script at `/home/hacker/solve.sh` that: takes one argument, if the argument is "pwn", output "college", for any other input, output "nope", once your script works correctly, run `/challenge/run` to get your flag!
## My solve:-
   **My flag** :-`pwn.college{Urpj5KhiHKXNgWJqFilJ3ju18i7.01NzMDOxwCNxAzNzEzW}`

   So, the challenge asked us to write script at `/home/hacker/solve.sh` that: takes one argument and if the argument is "pwn", output "college" and for any other input output `nope` and then run `/challenge/run`, hence i opened the shell and created `solve.sh` shell script which takes one arguments and outputs `college` if the argument is `pwn` and outputs `nope` if it is not, using `nano` command and ran it using `bash` and passed the arguments `pwn` to check if the script was proper and got the output `college` and again ran it and this time passed it the argument `college` and got the output `nope` and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@chaining~scripting-with-default-cases:~$ nano solve.sh
   hacker@chaining~scripting-with-default-cases:~$ bash solve.sh pwn
   college
   hacker@chaining~scripting-with-default-cases:~$ bash solve.sh college
   nope
   hacker@chaining~scripting-with-default-cases:~$ /challenge/run
   Correct! Your script properly handles the if/else conditions.
   Here's your flag:
   pwn.college{Urpj5KhiHKXNgWJqFilJ3ju18i7.01NzMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `else` clause executes when the `if` condition is false and that the `else` doesn't have a condition --- it catches everything that didn't match previously. It also doesn't have a `then` statement. Finally, the `fi` goes after the `else` block to denote the end of the whole complex statement.

### Refference :-
   None


# **11.<ins>Scripting with multiple conditions</ins>**:-
   For this challenge, write a script at `/home/hacker/solve.sh` that: takes one argument, if the argument is "hack", output "the planet", if the argument is "pwn", output "college", if the argument is "learn", output "linux", for any other input, output "unknown" once your script works correctly, run `/challenge/run` to get your flag.
## My solve:-
   **My flag** :-`pwn.college{gu0PK6SiWu00V8IRD28U5WSXfL8.0FOzMDOxwCNxAzNzEzW}`

   So, the challenge asked us to  write script at `/home/hacker/solve.sh` that: takes one argument and if the argument is "hack", output "the planet", if the argument is "pwn", output "college", if the argument is "learn", output "linux",and for any other input, output "unknown"  and then run `/challenge/run`, hence i opened the shell and created `solve.sh` shell script which takes one arguments and outputs `the planet` if the argument is `hack` and outputs `college` if the argument is `pwn` and outputs `linux` if the argument is `learn` and outputs `unknown` for any other argument, using `nano` command and ran it using `bash` and passed the arguments `hack` to check if the script was proper and got the output `the planet` and did the same for other conditions and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@chaining~scripting-with-multiple-conditions:~$ nano solve.sh
   hacker@chaining~scripting-with-multiple-conditions:~$ bash solve.sh hack
   the planet
   hacker@chaining~scripting-with-multiple-conditions:~$ bash solve.sh pwn
   college
   hacker@chaining~scripting-with-multiple-conditions:~$ bash solve.sh learn
   linux
   hacker@chaining~scripting-with-multiple-conditions:~$ bash solve.sh flag
   unknown
   hacker@chaining~scripting-with-multiple-conditions:~$ /challenge/run
   Correct! Your script properly handles all the conditions with elif.
   Here's your flag:
   pwn.college{gu0PK6SiWu00V8IRD28U5WSXfL8.0FOzMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can use `elif` (short for `else if`) if we need to check multiple conditions, and that we do need a `then` after the `elif`, just like the `if`. As before the `else` at the end catches everything that didn't match.

### Refference :-
   None


# **12.<ins>Reading shell scripts</ins>**:-
   In this challenge `/challenge/run` is a shell script that requires you to put in a secret password, but that password is hardcoded into the script iself! Read the script (using, say, `cat`), figure out the password, and get the flag 
## My solve:-
   **My flag** :-`pwn.college{cybRHPJC0xPwxZKNfvWmBd-0eX6.0lMwgDOxwCNxAzNzEzW}`

   So, the challenge asked us to read the `/challenge/run` shell script and findd the secret password and the run the program by paassing it, hence i opened the shell and used the `cat` command and read the shell script of `/challenge/run` and found out that the secret password is `hack the PLANET`, then i ran `/challenge/run` and passed it as argument and got the flag. 
   ```bash
   hacker@chaining~reading-shell-scripts:~$ cat /challenge/run
   #!/opt/pwn.college/bash

   read GUESS
   if [ "$GUESS" == "hack the PLANET" ]
   then
           echo "CORRECT! Your flag:"
           cat /flag
   else
           echo "Read the /challenge/run file to figure out the correct password!"
   fi
   hacker@chaining~reading-shell-scripts:~$ /challenge/run
   hack the PLANET
   CORRECT! Your flag:
   pwn.college{cybRHPJC0xPwxZKNfvWmBd-0eX6.0lMwgDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we're not the only one who writes shell scripts, and that they are very handy for doing simple "system-level" tasks, and are a common tool that developers and sysadmins reach for in fact, a surprising fraction of the programs on a typical Linux machine are shell scripts, and that we can read these scripts.

### Refference :-
   None
