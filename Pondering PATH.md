# **1.<ins>The PATH variable</ins>**:-
   In this challenge, you will disrupt the operation of the `/challenge/run` program. This program will DELETE the flag file using the `rm` command. However, if it can't find the rm command, the flag will not be deleted, and the challenge will give it to you! Thus, you must make it so that /`challenge/run` also can't find the `rm` command! 
## My solve:-
   **My flag** :-`pwn.college{EQth2SMnfowFUbZkWlINgRLzg7w.QX2cDM1wCNxAzNzEzW}`

   So, the challenge asked us to stop the `/challenge/run` from finding `rm`, hence i opened the shell and made the `PATH` variable blank and then ran `/challenge/run` and got the flag.
   ```bash
  hacker@path~the-path-variable:~$ PATH=""
   hacker@path~the-path-variable:~$ /challenge/run
   Trying to remove /flag...
   /challenge/run: line 4: rm: No such file or directory
   The flag is still there! I might as well give it to you!
   pwn.college{EQth2SMnfowFUbZkWlINgRLzg7w.QX2cDM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that there is a special shell variable, called `PATH`, that stores a bunch of directory paths in which the shell will search for programs corresponding to commands.

### Refference :-
   None


# **2.<ins>Setting PATH</ins>**:-
   In this challenge `/challenge/run` will run the `win` command via its bare name, but this command exists in the `/challenge/more_commands/` directory, which is not initially in the `PATH`. The `win` command is the only thing that `/challenge/run needs`, so you can just overwrite `PATH` with that one directory.  
## My solve:-
   **My flag** :-`pwn.college{gsusKhWLGK4WGTv63h0pl1GnIva.QX1cjM1wCNxAzNzEzW}`

   So, the challenge asked us to add the directory of the `win` command in `PATH` and the run `/challenge/run`, hence i opened the shell and added the directory of the `win` command by overwriting the `PATH` with `/challenge/more_commands/` as suggested by the challenge and the ran `/challenge/run` and got the flag.
   ```bash
   hacker@path~setting-path:~$ PATH=/challenge/more_commands/
   hacker@path~setting-path:~$ /challenge/run
   Invoking 'win'....
   Congratulations! You properly set the flag and 'win' has launched!
   pwn.college{gsusKhWLGK4WGTv63h0pl1GnIva.QX1cjM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that by adding directories to or replacing directories in the list of the `PATH`, we can expose these programs to be launched using their bare name.

### Refference :-
   None


# **3.<ins>Finding ommands</ins>**:-
   In this challenge, we added a `win` command somewhere in your `$PATH`, but it won't give you the flag. Instead, it's in the same directory as a `flag` file that we made readable by you! You must find `win` with the `which` command, and `cat` the flag out of that directory.
## My solve:-
   **My flag** :-`pwn.college{ogcyyFqj7BgmIvT5ij3M3KMJvTq.01NzEzNxwCNxAzNzEzW}`

   So, the challenge asked us to find the directory of the `win` command and the `cat` the flag from that directory, hence i opened the shell and used the `which` command and passed `win` as it's argument to find it's directory i.e `/challenge/paths/188/win`, then i used `ls` on `/challenge/paths/188` to check if there was a file named `flag`, then i catted the flag from there.
   ```bash
   hacker@path~finding-commands:~$ which win
   /challenge/paths/188/win
   hacker@path~finding-commands:~$ ls /challenge/paths/188
   flag  win
   hacker@path~finding-commands:~$ cat /challenge/paths/188/flag
   pwn.college{ogcyyFqj7BgmIvT5ij3M3KMJvTq.01NzEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that when you type the name of a command, something inside one of the many directories listed in our `$PATH` variable is what actually gets executed unless the command is a builtin, and that we can  find out which directory it is with the aptly-named `which` command which mirrors what the shell does when searching for commands, which looks at each directory in `$PATH` in order and prints the first file it finds whose name matches the argument you passed.

### Refference :-
   None


# **4.<ins>Adding commands</ins>**:-
   The challenge asks us to make a shell script called `win`, add its location to the `PATH`, and enable `/challenge/run` to find it!
   Hint: `/challenge/run` runs as root and will call `win`. Thus, win can simply `cat` the flag file. Again, the win command is the only thing that `/challenge/run` needs, so you can just overwrite `PATH` with that one directory. But remember, if you do that, your win command won't be able to find `cat`.
You have three options to avoid that:
1.Figure out where the cat program is on the filesystem. It must be in a directory that lives in the `PATH` variable, so you can print the variable out (refer to Shell Variables to remember how!), and go through the directories in it (recall that the different entries are separated by :), find which one has cat in it, and invoke cat by its absolute path.
2.Set a `PATH` that has the old directories plus a new entry for wherever you create `win`.
3.Use `read` (again, refer to Shell Variables) to read /flag. Since `read` is a builtin functionality of bash, it is unaffected by `PATH` shenanigans.
## My solve:-
   **My flag** :-`pwn.college{MoIAXONDpYrVi6F5AQmspPtaKM9.QX2cjM1wCNxAzNzEzW}`

   So, the challenge asked us to make a shell script called `win`, add its location to the `PATH`, and enable `/challenge/run` to find it hence i opened the shell and foud the directory of the `cat` and then i created a shell script `win` which catted the `/flag` by invoking the `cat` by it's absolute path i.e `/run/dojo/bin/cat`, and then made it executable for the  then i overwrited the `PATH` with the directory of `win` and the ran `/challenge/run` and got the flag.
   ```bash
   hacker@path~adding-commands:~$ which cat
   /run/dojo/bin/cat
   hacker@path~adding-commands:~$ nano win
   hacker@path~adding-commands:~$ chmod +x win
   hacker@path~adding-commands:~$ PATH=/home/hacker
   hacker@path~adding-commands:~$ /challenge/run
   Invoking 'win'....
   pwn.college{MoIAXONDpYrVi6F5AQmspPtaKM9.QX2cjM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we the users can create our own commands and add their location to the `PATH` and then run them directly.

### Refference :-
   None


# **5.<ins>Hijacking commands</ins>**:-
   This challenge will delete the flag using the `rm` command. But unlike before, it will not print anything out for you.
## My solve:-
   **My flag** :-`pwn.college{ouakiX_MZxe6EJe-PLgli-FPDIm.QX3cjM1wCNxAzNzEzW}`

   So, the challenge asked us to get the flag but invoking `/challenge/run` would not print anythig and inturn delete the flag using the `rm` command, hence i opened the shell and created a script shell `rm` which catted the `/flag`, then i added the directory of this `rm` before the orginal one in the `PATH` as it runs the first command it finds in the `PATH` and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@path~hijacking-commands:~$ nano rm
   hacker@path~hijacking-commands:~$ chmod +x rm
   hacker@path~hijacking-commands:~$ PATH=/home/hacker:$PATH
   hacker@path~hijacking-commands:~$ /challenge/run
   Trying to remove /flag...
   Found 'rm' command at /home/hacker/rm. Executing!
   pwn.college{ouakiX_MZxe6EJe-PLgli-FPDIm.QX3cjM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we the users can create our own commands and add their location to the `PATH` and then run them directly and that we can add new directories to it without disturbing the other directories present in it by using `PATH=[DIRECTORY]:$PATH` to add it in the front or `PATH=$PATH:[DIRECTORY]` to add it in the back.

### Refference :-
   None
