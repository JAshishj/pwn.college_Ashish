# **1.<ins>Listing processes</ins>**:-
   This challenge has renamed `/challenge/run` to a random filename, and this time we cannot `ls` the `/challenge directory`! But it also launched it, so that we  can find it in the running process list, figure out the filename, and relaunch it directly for the flag.
## My solve:-
   **My flag** :-`pwn.college{0JBHKya9Pf8lISSYtJjqbzkqztd.QX4MDO0wCNxAzNzEzW}`

   So, the challenge asked us to find the renamed `/challenge/run` file in the running process list, figure out the filename, and relaunch it, hence i opened the shell and used the `ps` command along with `-ef` option and looker through the running procees and found that `/challenge/12943-run-23472` is running, which is the renamed `/challenge/run` file hence i relaunced it and got the flag.
   ```bash
   hacker@processes~listing-processes:~$ ps -ef
   UID          PID    PPID  C STIME TTY          TIME CMD
   root           1       0  0 15:56 ?        00:00:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-i
  root           8       1  0 15:56 ?        00:00:00 /run/dojo/bin/sleep 6h
  root         133       1  0 15:56 ?        00:00:00 /challenge/12943-run-23472
  root         136     133  0 15:56 ?        00:00:00 sleep 6h
  hacker       138       0  0 15:56 pts/0    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/
  hacker       144     138  0 15:56 pts/0    00:00:00 /run/dojo/bin/bash --login
  hacker       153     144  0 15:56 pts/0    00:00:00 ps -ef
  hacker@processes~listing-processes:~$ /challenge/12943-run-23472
  Yahaha, you found me! Here is your flag:
  pwn.college{0JBHKya9Pf8lISSYtJjqbzkqztd.QX4MDO0wCNxAzNzEzW}
  Now I will sleep for a while (so that you could find me with 'ps').
   ```

### What i learned:-
   I learned that to list running processes using the `ps` command is used where `ps` syands for either "process snapshot" or "process status".I also learned that as ps is a very old utility, its usage is a bit of a mess. There are two ways to specify arguments."Standard" Syntax: in this syntax, you can use -e to list "every" process and -f for a "full format" output, including arguments. These can be combined into a single argument -ef."BSD" Syntax: in this syntax, you can use a to list processes for all users, x to list processes that aren't running in a terminal, and u for a "user-readable" output. These can be combined into a single argument aux.And that there are many commonalities between ps -ef and ps aux: both display the user (USER column), the PID, the TTY, the start time of the process (STIME/START), the total utilized CPU time (TIME), and the command (CMD/COMMAND). ps -ef additionally outputs the Parent Process ID (PPID), which is the PID of the process that launched the one in question, while ps aux outputs the percentage of total system CPU and Memory that the process is utilizing
   
### Refference :-
   None


# **2.<ins>Killing processes</ins>**:-
   In this challenge `/challenge/run` will refuse to run while `/challenge/dont_run` is running! we must find the `dont_run` process and kill it. If we fail, `pwn.college` will disavow all knowledge of your mission.
## My solve:-
   **My flag** :-`pwn.college{8UtQbVwru27THCe8eT57TTDIYhr.QXyQDO0wCNxAzNzEzW}`

   So, the challenge asked us to kill the `/challenge/dont_run` so that we can run `/challenge/run`, hence i opened the shell and used the `ps -ef` command and got it's process identifier(PID) `136` and passed it as an argument to the `kill` command to stop it and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@processes~killing-processes:~$ ps -ef
   UID          PID    PPID  C STIME TTY          TIME CMD
   root           1       0  0 16:06 ?        00:00:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-i
   root           7       1  0 16:06 ?        00:00:00 /run/dojo/bin/sleep 6h
   root         135       1  0 16:06 ?        00:00:00 su -c /challenge/.launcher hacker
   hacker       136     135  0 16:06 ?        00:00:00 /challenge/dont_run
   hacker       137     136  0 16:06 ?        00:00:00 sleep 6h
   hacker       139       0  0 16:07 pts/0    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/
   hacker       145     139  0 16:07 pts/0    00:00:00 /run/dojo/bin/bash --login
   hacker       154     145  0 16:07 pts/0    00:00:00 ps -ef
   hacker@processes~killing-processes:~$ kill 136
   hacker@processes~killing-processes:~$ /challenge/run
   Great job! Here is your payment:
   pwn.college{8UtQbVwru27THCe8eT57TTDIYhr.QXyQDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to terminate the running processes in linux, `kill` command is used by passing the process identifier(PID) of the process that we want to terminate as it's argument.

### Refference :-
   None


# **3.<ins>Interrupting processes</ins>**:-
   The challenge asks us to run `/challenge/run` will refuse to give you the flag until we interrupt it.
## My solve:-
   **My flag** :-`pwn.college{UMGbAWUirwvQMml3upoMofGy_vi.QXzQDO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` and the interrupt it by pressing `crtl-c`, hence i opened the shell and ran `/challenge/run` and the pressed `crtl-c` to interrupt it and got the flag.
   ```bash
   hacker@processes~interrupting-processes:~$ /challenge/run
   I could give you the flag... but I won't, until this process exits. Remember,
   you can force me to exit with Ctrl-C. Try it now!
   ^C
   Good job! You have used Ctrl-C to interrupt this process! Here is your flag:
   pwn.college{UMGbAWUirwvQMml3upoMofGy_vi.QXzQDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the hotkey `ctrl-c is used to interrupt the programs, and that it sends an "interrupt" to whatever application is waiting on input from the terminal and, typically, this causes the application to cleanly exit.

### Refference :-
   None


# **4.<ins></ins>**:-
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
