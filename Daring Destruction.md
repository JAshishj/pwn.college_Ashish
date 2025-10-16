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


# **2.<ins>Disk-space doomsday</ins>**:-
   The challenge asks us to :- fill our disk, run `/challenge/check`. It will attempt to create a 1 megabyte temporary file. If that fails, you pass the first stage and the checker will ask you to free the space, delete the file you made (with `rm`) to clear up the space, run `/challenge/check` a second time. If it can now create the temporary file (i.e., you successfully cleaned up your home directory), you’ll receive the flag.
## My solve:-
   **My flag** :-`pwn.college{szjm0qzacg84rFJ6peWyXPtVq3I.0lMyEzNxwCNxAzNzEzW}`

   So, the challenge asked us to fill our disk then run `/challenge/check` and then delete the file that we made and then again run `/challenge/check`, hence i opened the shell and created a file `` and filed it with `y` then i ran `/challenge/check` and then deleted the file using `rm` command and then ran `/challenge/check` and got the flag.
   ```bash
   hacker@destruction~disk-space-doomsday:~$ touch a.txt
   hacker@destruction~disk-space-doomsday:~$ yes | cat > a.txt
   cat: write error: Disk quota exceeded
   hacker@destruction~disk-space-doomsday:~$ /challenge/check
   Well done, you clogged the disk. Now free that space (remove the file you created) and run /challenge/check again to prove you cleaned up!
   hacker@destruction~disk-space-doomsday:~$ rm a.txt
   hacker@destruction~disk-space-doomsday:~$ /challenge/check
   Disk space restored. Here is your flag:
   pwn.college{szjm0qzacg84rFJ6peWyXPtVq3I.0lMyEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the available space in `/home/hacker` in this container is a measly 1 gigabyte.

### Refference :-
   None


# **3.<ins>rm -rf /</ins>**:-
   In this challenge, you will do something that you might never do again: wipe the whole system. We've actually modified things a bit to keep your home directory safe (normally, it would get wiped as well!), but otherwise, all that stands before you and the flag is your willingness to wipe the drive. But before you wipe it all, make sure to start `/challenge/check` so that it can watch the fireworks (and give you the flag)! 
## My solve:-
   **My flag** :-`pwn.college{83LpEAfiWQprzZSYpQuC3rBprP1.0lMzEzNxwCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/check` and then wipe the entier system, hence i opened the shell and ran `/challenge/check` adn the used `rm -rf` command on `/` to wipe the system and got the flag.
   ```bash
   terminal 1:-
   hacker@destruction~rm-rf-:~$ rm -rf --no-preserve-root /
   /bin/rm: skipping '/home/hacker', since it's on a different device
   /bin/rm: cannot remove '/etc/resolv.conf': Device or resource busy
   /bin/rm: cannot remove '/etc/hostname': Device or resource busy
   /bin/rm: cannot remove '/etc/hosts': Device or resource busy
   /bin/rm: skipping '/dev', since it's on a different device
   /bin/rm: cannot remove '/usr/sbin/docker-init': Device or resource busy
   /bin/rm: skipping '/run/dojo/sys', since it's on a different device
   /bin/rm: skipping '/sys', since it's on a different device
   /bin/rm: skipping '/proc', since it's on a different device
   /bin/rm: skipping '/nix', since it's on a different device

   terminal 2:-
   hacker@destruction~rm-rf-:~$ /challenge/check
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   Looks like you haven't wiped the system! We'll check again in 5 seconds...
   YES! You wiped it, you wild hacker! The flag is yours:
   pwn.college{83LpEAfiWQprzZSYpQuC3rBprP1.0lMzEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `-r` (recursive) flag removes directories and all files containing them. The `-f` (force) flag ignores any errors the `rm` command runs into or compulsions that it may have.

### Refference :-
   None


# **4.<ins>Life after rm -rf /</ins>**:-
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
