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


# **4.<ins>Killing misbehaving processes</ins>**:-
   In this challenge, there's a decoy process that's hogging a critical resource - a named pipe (FIFO) at `/tmp/flag_fifo` into which `/challenge/run` wants to write our flag we need to kill this process.
Our general workflow should be:
Check what processes are running.
Find `/challenge/decoy` in the list and figure out its process ID.
kill it.
Run `/challenge/run` to get the flag without being overwhelmed by decoys (you don't need to redirect its output; it'll write to the FIFO on its own).
## My solve:-
   **My flag** :-`pwn.college{80lPzpwSTi0OUgtonctLKGHpfPE.0FNzMDOxwCNxAzNzEzW}`

   So, the challenge asked us to kill the `/challenge/decoy` process which is hogging the FIFO and then run `/challene/run`, hence i opened the shell and used the `ps -ef` command to find the PID of the process and terminated it using the `kill` command by passing the PID and then i ran `/challenge/run` which wrote the flag in the maned pipe `/tmp/flag_fifo`, then i catted it in another terminal and got the flag.
   ```bash
   terminal 1:-
   hacker@processes~killing-misbehaving-processes:~$ ps -ef
   UID          PID    PPID  C STIME TTY          TIME CMD
   root           1       0  0 13:28 ?        00:00:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-workspace/bin/dojo-i
   root           7       1  0 13:28 ?        00:00:00 /run/dojo/bin/sleep 6h
   root         137       1  0 13:28 ?        00:00:00 /bin/bash /challenge/.init
   root         138       1  0 13:28 ?        00:00:00 /bin/bash /challenge/.init
   root         139       1  0 13:28 ?        00:00:00 su -c exec /challenge/decoy > /tmp/flag_fifo hacker
   root         140     138  0 13:28 ?        00:00:00 sleep 6h
   root         141     137  0 13:28 ?        00:00:00 sleep 6h
   hacker       142     139  0 13:28 ?        00:00:00 /usr/bin/python /challenge/decoy
   hacker       144       0  0 13:29 pts/0    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/
   hacker       150     144  0 13:29 pts/0    00:00:00 /run/dojo/bin/bash --login
   hacker       159       0  0 13:29 pts/1    00:00:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-interactive-5.2p37/
   hacker       165     159  0 13:29 pts/1    00:00:00 /run/dojo/bin/bash --login
   hacker       174     150  0 13:29 pts/0    00:00:00 ps -ef
   hacker@processes~killing-misbehaving-processes:~$ kill 142
   hacker@processes~killing-misbehaving-processes:~$ /challenge/run
   Sending the flag to /tmp/flag_fifo!

   terminal 2:-
   hacker@processes~killing-misbehaving-processes:~$ cat /tmp/flag_fifo
   pwn.college{80lPzpwSTi0OUgtonctLKGHpfPE.0FNzMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that sometimes, misbehaving processes can interfere with our work and these processes might need to be killed.

### Refference :-
   None


# **5.<ins>Suspending processes</ins>**:-
   This challeng's `run` wants to see another copy of itself running and using the same terminal. Use the terminal to launch it, then suspend it, then launch another copy while the first is suspended! 
## My solve:-
   **My flag** :-`pwn.college{8Rt7MOxebEhQFNsyXIqd3MzWHPW.QX1QDO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` and then suspend it and then again run `/challenge/run`, hence i opened he shell and ran `/challenge/run` and suspended it using the hotkey `Ctrl-Z` and then ran `/chllenge/run` again and got the flag.
   ```bash
   hacker@processes~suspending-processes:~$ /challenge/run
   I'll only give you the flag if there's already another copy of me running in
   this terminal... Let's check!

   UID          PID    PPID  C STIME TTY          TIME CMD
   root         138     129  0 17:02 pts/0    00:00:00 bash /challenge/run
   root         140     138  0 17:02 pts/0    00:00:00 ps -f

   I don't see a second me!

   To pass this level, you need to suspend me and launch me again! You can
   background me with Ctrl-Z or, if you're not ready to do that for whatever
   reason, just hit Enter and I'll exit!
   ^Z
   [1]+  Stopped                 /challenge/run
   hacker@processes~suspending-processes:~$ /challenge/run
   I'll only give you the flag if there's already another copy of me running in
   this terminal... Let's check!
   
   UID          PID    PPID  C STIME TTY          TIME CMD
   root         138     129  0 17:02 pts/0    00:00:00 bash /challenge/run
   root         145     129  0 17:02 pts/0    00:00:00 bash /challenge/run
   root         147     145  0 17:02 pts/0    00:00:00 ps -f

   Yay, I found another version of me! Here is the flag:
   pwn.college{8Rt7MOxebEhQFNsyXIqd3MzWHPW.QX1QDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can suspend processes to the background with the hotkey `Ctrl-Z`.

### Refference :-
   None


# **6.<ins>Resuming processes</ins>**:-
   This challenge's run needs you to suspend it, then resume it to get the flag.
## My solve:-
   **My flag** :-`pwn.college{4OvuIpmO_7eYkHnrUdZvcQqlCv8.QX2QDO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` and then suspend it and then resume it, hence i opened the shell and ran the `/challenge/run` and then suspended it by using the hotkey `Ctrl-Z` and the resumed it using the `fg` command and got the flag.
   ```bash
   hacker@processes~resuming-processes:~$ /challenge/run
   Let's practice resuming processes! Suspend me with Ctrl-Z, then resume me with
   the 'fg' command! Or just press Enter to quit me!
   ^Z
   [1]+  Stopped                 /challenge/run
   hacker@processes~resuming-processes:~$ fg
   /challenge/run
   I'm back! Here's your flag:
   pwn.college{4OvuIpmO_7eYkHnrUdZvcQqlCv8.QX2QDO0wCNxAzNzEzW}
   Don't forget to press Enter to quit me!

   Goodbye!
   ```

### What i learned:-
   I learned that to resume processes, our shell provides the `fg` command, a builtin that takes the suspended process, resumes it, and puts it back in the foreground of our terminal.

### Refference :-
   None


# **7.<ins>Backgrounding processes</ins>**:-
   This challenge's `run` wants to see another copy of itself running, not suspended, and using the same terminal. Use the terminal to launch it, then suspend it, then background it with `bg` and launch another copy while the first is running in the background! 
## My solve:-
   **My flag** :-`pwn.college{obUdlbKalw8a5IQ_IK6LLft0sfl.QX3QDO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run`, suspend it, then background it, and then run it again, hence i opened the shell and ran `/challenge/run` and suspended it using by using the hotkey `Ctrl-Z` and the backgrounded it using the `bg` command and then ran `/challenge/run` again and got the flag.
   ```bash
   hacker@processes~backgrounding-processes:~$ /challenge/run
   I'll only give you the flag if there's already another copy of me running *and
   not suspended* in this terminal... Let's check!

   UID          PID STAT CMD
   root         138 S+   bash /challenge/run
   root         140 R+   ps -o user=UID,pid,stat,cmd

   I don't see a second me!

   To pass this level, you need to suspend me, resume the suspended process in the
   background, and then launch a new version of me! You can background me with
   Ctrl-Z (and resume me in the background with 'bg') or, if you're not ready to
   do that for whatever reason, just hit Enter and I'll exit!
   ^Z
   [1]+  Stopped                 /challenge/run
   hacker@processes~backgrounding-processes:~$ bg
   [1]+ /challenge/run &
   hacker@processes~backgrounding-processes:~$


   Yay, I'm now running the background! Because of that, this text will probably
   overlap weirdly with the shell prompt. Don't panic; just hit Enter a few times
   to scroll this text out.

   hacker@processes~backgrounding-processes:~$ /challenge/run
   I'll only give you the flag if there's already another copy of me running *and
   not suspended* in this terminal... Let's check!

   UID          PID STAT CMD
   root         138 S    bash /challenge/run
   root         148 S    sleep 6h
   root         149 S+   bash /challenge/run
   root         151 R+   ps -o user=UID,pid,stat,cmd

   Yay, I found another version of me running in the background! Here is the flag:
   pwn.college{obUdlbKalw8a5IQ_IK6LLft0sfl.QX3QDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can also resume processes in the background with the `bg` command which will allow the process to keep running, while giving us our shell back to invoke more commands in the meantime.

### Refference :-
   None


# **8.<ins>Forgrounding processes</ins>**:-
   we can foreground a backgrounded process with fg just like you foreground a suspended process! This level will walk you through that!
## My solve:-
   **My flag** :-`pwn.college{cthYxMKGOcA0VQGEgXtO6jRyAqN.QX4QDO0wCNxAzNzEzW}`

   So, the challenge did not have a definate description but looking at the other challenges in this module which gave instructions when i ran `/challenge/run`, hence i opened the shell and ran `/challenge/run` then it gave me the instructions for this challenge that i had to suspend it, resume the suspended process in the background, and then foreground it without re-suspending it, hence i suspended it using by using the hotkey `Ctrl-Z` and the backgrounded it using the `bg` command and then forgrounded it by using `fg` command and got the flag.   
   ```bash
   hacker@processes~foregrounding-processes:~$ /challenge/run
   To pass this level, you need to suspend me, resume the suspended process in the
   background, and *then* foreground it without re-suspending it! You can
   background me with Ctrl-Z (and resume me in the background with 'bg') or, if
   you're not ready to do that for whatever reason, just hit Enter and I'll exit!
   ^Z
   [1]+  Stopped                 /challenge/run
   hacker@processes~foregrounding-processes:~$ bg
   [1]+ /challenge/run &
   hacker@processes~foregrounding-processes:~$


   Yay, I'm now running the background! Because of that, this text will probably
   overlap weirdly with the shell prompt. Don't panic; just hit Enter a few times
   to scroll this text out. After that, resume me into the foreground with 'fg';
   I'll wait.

   hacker@processes~foregrounding-processes:~$ fg
   /challenge/run
   YES! Great job! I'm now running in the foreground. Hit Enter for your flag!

   pwn.college{cthYxMKGOcA0VQGEgXtO6jRyAqN.QX4QDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can foreground a backgrounded process with `fg` just like you foreground a suspended process.

### Refference :-
   None


# **9.<ins>Starting backgrounded processes</ins>**:-
   The challenge asks us to launch `/challenge/run` backgrounded for the flag.
## My solve:-
   **My flag** :-`pwn.college{4sx5LPoWkEUAvwnsATDr4nvymMJ.QX5QDO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` in the background, hence i opened the shell and ran `/challenge/run` directly in the background by appending a `&` to it and got the flag.
   ```bash
   hacker@processes~starting-backgrounded-processes:~$ /challenge/run &
   [1] 138
   hacker@processes~starting-backgrounded-processes:~$


   Yay, you started me in the background! Because of that, this text will probably
   overlap weirdly with the shell prompt, but you're used to that by now...

   Anyways! Here is your flag!
   pwn.college{4sx5LPoWkEUAvwnsATDr4nvymMJ.QX5QDO0wCNxAzNzEzW}

   [1]+  Done                    /challenge/run
   ```

### What i learned:-
   I learned that we don't have to suspend processes to background them we can start them backgrounded right off the bat appending a `&` to the command.

### Refference :-
   None


# **10.<ins>Process exit codes</ins>**:-
   The challenge asks us to retrieve the exit code returned by `/challenge/get-code` and then run `/challenge/submit-code` with that error code as an argument.
## My solve:-
   **My flag** :-`pwn.college{INi-jzYPnS4lQEk0pHrb97e1afx.QX5YDO1wCNxAzNzEzW}`

   So, the challenge asked us to get the exit code of `/challenge/get-code` and then run `/challenge/submit-code` with that error code as an argument, hence i opened the shell and ran `/challenge/get-code` and then accessed it's exit code by using the special `?` variable  and echoed it and then ran `/challenge/submit-code` and passed the exit code as an argument and got the flag.
   ```bash
   hacker@processes~process-exit-codes:~$ /challenge/get-code
   Exiting with an error code!
   hacker@processes~process-exit-codes:~$ echo $?
   32
   hacker@processes~process-exit-codes:~$ /challenge/submit-code 32
   CORRECT! Here is your flag:
   pwn.college{INi-jzYPnS4lQEk0pHrb97e1afx.QX5YDO1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that every shell command, including every program and every builtin, exits with an exit code when it finishes running and terminates and that this can be used by the shell, or the user of the shell to check if the process succeeded in its functionality.I also learned that we can access the exit code of the most recently-terminated command using the special `?` variable, and that commands that succeed typically return `0` and commands that fail typically return a non-zero value, most commonly `1` but sometimes an error code that identifies a specific failure mode.

### Refference :-
   None
