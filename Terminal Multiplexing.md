# **1.<ins>Launching screen</ins>**:-
   For this challenge, we've hooked things up so that just launching `screen` will get you the flag. 
## My solve:-
   **My flag** :-`pwn.college{0uXUsGtQ1i1YGeIsL0mXFdBG9Xd.0VN4IDOxwCNxAzNzEzW}`

   So, the challenge asked us to use the command `screen`, hence i opened the shell and used `screen` and got the flag.
   ```bash
   terminal:-
   hacker@terminal-multiplexing~launching-screen:~$ screen

   screen:-
   Congratulations! You're inside a screen session!
   Here's your flag:
   pwn.college{0uXUsGtQ1i1YGeIsL0mXFdBG9Xd.0VN4IDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `screen` is a program that creates virtual terminals inside your terminal. It's somewhat like having multiple browser tabs, but for your command line!

### Refference :-
   None


# **2.<ins>Detaching and attaching</ins>**:-
   For this challenge, you'll need to: launch `screen`, detach from it, run `/challenge/run` which will secretly send the flag to your detached session, reattach to see your prize.
## My solve:-
   **My flag** :-`pwn.college{kmS77VGYS7qM5bzTkzt4FEwtx29.0lN4IDOxwCNxAzNzEzW}`

   So, the challenge asked us to launch `screen`, detach from it, run `/challenge/run` and reattach, hence i opened the shell and used the `screen` command and then deatached using `Ctrl-A`, followed by `d` and then ran `/challenge/run` in the normal terminal and the reatached by passing `-r` argument to `screen` and got the flag.
   ```bash
   terminal:-
   hacker@terminal-multiplexing~detaching-and-attaching:~$ screen
   [detached from 154.pts-1.terminal-multiplexing~detaching-and-attaching]
   hacker@terminal-multiplexing~detaching-and-attaching:~$ /challenge/run
   Found detached screen session: 154.pts-1.terminal-multiplexing~detaching-and-attaching
   Sending flag to your screen session...

   Flag sent! Now reattach to your screen session with:

     screen -r

   You'll find the flag waiting for you there!
   hacker@terminal-multiplexing~detaching-and-attaching:~$ screen -r
    
   screen:-
   hacker@terminal-multiplexing~detaching-and-attaching:~$
   hacker@terminal-multiplexing~detaching-and-attaching:~$ echo Yes! Flag is: pwn.college{kmS77VGYS7qM5bzTkzt4FEwtx29.0lN4IDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we detach by pressing `Ctrl-A`, followed by `d` (for detach) and that this leaves our session running in the background while you return to your normal terminal.I also learned that to reattach, we can use the `-r` argument to `screen`.

### Refference :-
   None


# **3.<ins>Finding sessions</ins>**:-
   In this challenge, we've created three screen sessions for you. One of them contains the flag. The other two are decoys!, You'll need to check each one until you find it.
## My solve:-
   **My flag** :-`pwn.college{Uv4sGfTv68Ds7dfnCdsrMUEM3Bf.01N4IDOxwCNxAzNzEzW}`

   So, the challenge asked us to look through the three screens that are running and find the flag in one of them, hence i opened the shell and used the command `screen -ls` to list all the screens that are running and then looked through each of them by passing their PID as an arument to `screen -r` and got the flag.
   ```bash
   terminal:-
   hacker@terminal-multiplexing~finding-sessions:~$ screen -ls
   There are screens on:
           144.session_0c39a0c28b1ecc16    (Detached)
           147.session_a09af38e759ae0af    (Detached)
           150.session_a7f19f193258c343    (Detached)
   3 Sockets in /home/hacker/.screen.
   hacker@terminal-multiplexing~finding-sessions:~$ screen -r 144
   [screen is terminating]
   hacker@terminal-multiplexing~finding-sessions:~$ screen -r 147
   [screen is terminating]

   screen 1:-
   hacker@terminal-multiplexing~finding-sessions:~$  echo 'Nothing here! Try another session.'
   Nothing here! Try another session.

   screen 2:-
   hacker@terminal-multiplexing~finding-sessions:~$  echo 'Congratulations! You found the right session!'
   Congratulations! You found the right session!
   hacker@terminal-multiplexing~finding-sessions:~$  echo pwn.college{Uv4sGfTv68Ds7dfnCdsrMUEM3Bf.01N4IDOxwCNxAzNzEzW}
   pwn.college{Uv4sGfTv68Ds7dfnCdsrMUEM3Bf.01N4IDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can list all the screens that are running  by using `screen -ls`, and that the identifiers of the sessions are the PID of each respective screen process, a dot, and the name of the screen session and to attach to a specific one, you use its name or its PID by giving it as an argument to `screen -r`.

### Refference :-
   None


# **4.<ins>Switching windows</ins>**:-
   For this challenge, we've set up a screen session with two windows: Window 0 has... well, you'll have to switch there to find out!, Window 1 has a welcome message.Attach to the session with `screen -r`, then use one of the key combinations above to switch to Window 1. Go get that flag!
## My solve:-
   **My flag** :-`pwn.college{YTC0q9prdJVHy1Euvd131Fk3WgG.0FO4IDOxwCNxAzNzEzW}`

   So, the challenge asked us to attach to the `screen` and then look through the `window 0` of the screen, hence i opened the shell and used the command `screen -r` to attach to the screen which led me to the window 1 and then used `Ctrl-A` follwed by `0` to move to the window 0 and got the flag.
   ```bash
   terminal:-
   hacker@terminal-multiplexing~switching-windows:~$ screen -r

   screen:-
   window 1:-
   cat <<MSG
   Welcome to the window switching challenge!
   You are currently in window 1.
   The flag is hidden in window 0.
   Use Ctrl-A 0 to switch to window 0!
   MSG
   hacker@terminal-multiplexing~switching-windows:~$  cat <<MSG
   > Welcome to the window switching challenge!
   > You are currently in window 1.
   > The flag is hidden in window 0.
   > Use Ctrl-A 0 to switch to window 0!
   > MSG
   Welcome to the window switching challenge!
   You are currently in window 1.
   The flag is hidden in window 0.
   Use Ctrl-A 0 to switch to window 0!
   hacker@terminal-multiplexing~switching-windows:~$
   window 0:-
   hacker@terminal-multiplexing~switching-windows:~$  cat <<MSG
   > Excellent work! You found window 0!
   > Here is your flag: pwn.college{YTC0q9prdJVHy1Euvd131Fk3WgG.0FO4IDOxwCNxAzNzEzW}
   > MSG
   Excellent work! You found window 0!
   Here is your flag: pwn.college{YTC0q9prdJVHy1Euvd131Fk3WgG.0FO4IDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that inside a single screen session, you can have multiple windows, like your browser has multiple tabs. This can be super handy for organizing different tasks!
These windows are handled with different keyboard shortcuts, all starting with `Ctrl-A`:
`Ctrl-A` `c` - Create a new window
`Ctrl-A` `n` - Next window
`Ctrl-A` `p` - Previous window
`Ctrl-A` `0` through `Ctrl-A` `9` - Jump directly to window 0-9
`Ctrl-A` `"` - bring up a selection menu of all of the windows

### Refference :-
   None


# **5.<ins>Detaching and attaching (tmxu)</ins>**:-
   For this challenge: launch `tmux`, detach from it, run `/challenge/run` this will send the flag to your detached session!, reattach to see your prize 
## My solve:-
   **My flag** :-`pwn.college{4_SSlRwPPMSpiWJ8hnvlKha11w-.0VO4IDOxwCNxAzNzEzW}`

   So, the challenge asked us to  launch `tmux`, detach from it, run `/challenge/run` and reattach, hence i opened the shell and used the `tmux` command and then deatached using `Ctrl-B`, followed by `d` and then ran `/challenge/run` in the normal terminal and the reatached by passing `a` argument to `tmux` and got the flag.
   ```bash
   terminal:-
   hacker@terminal-multiplexing~detaching-and-attaching-tmux:~$ tmux
   [detached (from session 0)]
   hacker@terminal-multiplexing~detaching-and-attaching-tmux:~$ /challenge/run
   Found detached tmux session: 0
   Sending flag to your tmux session...
   Flag sent! Now reattach to your tmux session with:
     tmux attach
   You'll find the flag waiting for you there!
   hacker@terminal-multiplexing~detaching-and-attaching-tmux:~$ tmux a

   tmux:-
   hacker@terminal-multiplexing~detaching-and-attaching-tmux:~$  echo Congratulations, here is your flag: pwn.college{4_SSlRwPPMSpiWJ8hnvlKha11w-.0VO4IDOxwCNxAzNzEzW}
   Congratulations, here is your flag: pwn.college{4_SSlRwPPMSpiWJ8hnvlKha11w-.0VO4IDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `tmux` (terminal multiplexer) is screen's younger, more modern cousin and that it does all the same things but with some different key bindings and the biggest difference is that instead of `Ctrl-A`, `tmux` uses `Ctrl-B` as its command prefix, so to detach from `tmux`, you press `Ctrl-B` followed by `d` and that the commands also differ:
`tmux ls` - List sessions
`tmux attach` or `tmux a` - Reattach to session

### Refference :-
   None


# **6.<ins>Switching windows (tmux)</ins>**:-
   For this challenge we've created a `tmux` session with two windows: Window 0 has the flag!, Window 1 has your warm welcome. 
## My solve:-
   **My flag** :-`pwn.college{I12ecdTcw751T8wmVBu0GAMetyT.0FM5IDOxwCNxAzNzEzW}`

   So, the challenge asked us to attach to the `tmux` and then look through the `window 0` of the tmux, hence i opened the shell and used the command `tmux a` to attach to the tmux and used `Ctrl-B` followed by `0` to move to the window 0 and got the flag.
   ```bash
   terminal:-
   hacker@terminal-multiplexing~switching-windows-tmux:~$ tmux a

   tmux:-
   window 1:
    cat <<MSG
   Welcome to the tmux window switching challenge!
   You are currently in window 1.
   The flag is hidden in window 0.
   Use Ctrl-B 0 to switch to window 0!
   MSG
   hacker@terminal-multiplexing~switching-windows-tmux:~$  cat <<MSG
   > Welcome to the tmux window switching challenge!
   > You are currently in window 1.
   > The flag is hidden in window 0.
   > Use Ctrl-B 0 to switch to window 0!
   > MSG
   Welcome to the tmux window switching challenge!
   You are currently in window 1.
   The flag is hidden in window 0.
   Use Ctrl-B 0 to switch to window 0!
   window 0:-
   hacker@terminal-multiplexing~switching-windows-tmux:~$  cat <<MSG
   > Excellent work! You found window 0!
   > Here is your flag: pwn.college{I12ecdTcw751T8wmVBu0GAMetyT.0FM5IDOxwCNxAzNzEzW}
   > MSG
   Excellent work! You found window 0!
   Here is your flag: pwn.college{I12ecdTcw751T8wmVBu0GAMetyT.0FM5IDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that just like `screen`, `tmux` has windows. The key combos are different, but the concept is the same:
`Ctrl-B c` - Create a new window
`Ctrl-B n` - Next window
`Ctrl-B p` - Previous window
`Ctrl-B 0` through `Ctrl-B 9` - Jump to window 0-9
`Ctrl-B w` - See a nice window picker
`Tmux` shows your windows at the bottom in a status bar that looks like:
`[0] 0:bash* 1:bash`
Where the `*` shows your current window, and each entry also shows the process that the window was created to run.

### Refference :-
   None
