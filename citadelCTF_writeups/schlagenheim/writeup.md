# **<ins>Challenge</ins>**:-
Your quest continues, but you feel something odd about this room. The only artifact on this floor is a corrupted file held in the hands of a jet-black statue, frozen in the pose of a band mid-performance. The passcode to the next floor is hidden within this piece of music, but it can’t be played, as if the wrong extension has scrambled it.

You must take the corrupted file and repair it to reveal the true code that will unlock the door forward.

# **<ins>My solve</ins>**:-
  By reading the challenge it was clear that sonthing was corrupted in the file hence i opened it in the `HxD` hex editor provided in the discord, where it was written `M1D1` but the file was had the extention `.wav`, hence i provided the first 4 bytes to the llm `ChatGPT` and asked it if the header was correct or not for the MIDI file formate for which it replied that the bytes were not correct and it provided the correct bytes that should have been present, then i changed the first four bytes as given by it and then played it but did not get anything then i opened it in the software Audacity as it was provided in the discord and viewed the file in it and got the flag.
