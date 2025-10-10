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
