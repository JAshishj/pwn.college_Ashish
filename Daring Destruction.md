# **1.<ins>The fork bomb</ins>**:-
   This challenge contains a `/challenge/check` that'll try to determine if your fork bomb is working (e.g., if it can't launch new processes) and give you the flag if so. Make sure to launch it (in a different terminal) before launching your attack; otherwise you won't be able to launch it!
## My solve:-
   **My flag** :-`pwn.college{U96TQrOygumR_MDvCiIbn-uukfw.0VMyEzNxwCNxAzNzEzW}`

   So, the challenge asked us to create a "fork bomb" and then run `/challenge/check` which ceckes if the "fork bomb" works or not, hence i opened the shell and created a script called `bomb.sh` and made it launch two copies in the background, then i made it executable and then ran it in another terminal and ran `/challenge/check` in the orginal terminal and got the flag.
   ```bash
   hacker@destruction~the-fork-bomb:~$ /challenge/check
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   It looks like the system can still spawn processes. We'll check again in 5 seconds...
   You successfully saturated the process table.  Here is your hard-earned flag:
   pwn.college{U96TQrOygumR_MDvCiIbn-uukfw.0VMyEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that if you create processes faster than the kernel can handle, the process table fills up and everything grinds to a halt. This new process (e.g., of an `ls` invocation) is ``forked'' off of a parent process (e.g., a shell instance). Thus, the induced explosion of processes is called a "Fork Bomb"

### Refference :-
   None


# **2.<ins></ins>**:-
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


# **3.<ins></ins>**:-
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
