# Tokyo Westerns CTF 4th 2018: vimshell

![date](https://img.shields.io/badge/date-01.09.2018-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-126-blue.svg)
![solves](https://img.shields.io/badge/solves-113-brightgreen.svg)

## Description
Can you escape from [jail](http://vimshell.chal.ctf.westerns.tokyo/)?

## Summary
Go to flag file, **./flag**, with **(CTRL+W, F)** shortcut in *vim* connected app

## Flag
```
TWCTF{the_man_with_the_vim}
```

## Detailed solution
Opening the given web application in default browser(*Vivaldi*, in my case), we observe that it is a **xterm.js** app, connected with **terminado** to a server terminal, where is opened vim app.  
It is showed the `git diff` command’s output for a configuration file in Vim(*normal.c*, that realize the keymapping). So the *nv_colon*(":"), *nv_exmode*("Q"), *nv_g_cmd*("g") keys are simply unfunctional, by commenting the coresponding lines.  

```
diff --git a/src/normal.c b/src/normal.c
index 41c762332..0011afb77 100644
--- a/src/normal.c
+++ b/src/normal.c
[...]
-    {':',      nv_colon,       0,                      0},
+    // {':',   nv_colon,       0,                      0},
[...]
-    {'Q',      nv_exmode,      NV_NCW,                 0},
+    // {'Q',   nv_exmode,      NV_NCW,                 0},
[...]
-    {'g',      nv_g_cmd,       NV_NCH_ALW,             FALSE},
+    // {'g',   nv_g_cmd,       NV_NCH_ALW,             FALSE},
[...]
"/vimshell.patch" [readonly] 31 lines, 1124 characters
```

We try to use *ZZ* shortcut, but it doesn’t close vim, but the connection with server. Another shortcut that can be used is **(CTRL+W, F)** to open a file in split-screen mode. We delete the *CTRL+W* shortcut from browser close tab shortcut’s list(in *Vivaldi*, *Setting->Keyboard->Tabs*).  
After that, we return to application and press **i** key multiple time. Passing some swap errors, we enter to insert mode and type `./flag`. We exit this mode with *ESC* key and test the *(CTRL+W, F)*, which show the flag file.

## Another solutions
We can type **K** on diff keyword to enter the *man mode of vim* and then **!** for *command mode in man*. So that we have hash, we can simply `cat /flag`.
