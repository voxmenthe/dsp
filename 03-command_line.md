# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  		list files in current directory
`ls -a`  	list all files in current dir including those starting with .
`ls -l`  	list with long listing format
`ls -lh`    long listing format with human readable file sizes 
`ls -lah`   long listing format with human readable file sizes
`ls -t`  	list sorted by modification time, newest first
`ls -Glp`   G = don't print group names -l  -p = indicator-style is slash

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > I like:
ls -G 		because it's a nice clean format
ls -r 		because reverse order is always fun
ls -x 		nice to see things as rows
ls -d 		because sometimes you just want the directories
ls -t 		sorted by freshness is useful
---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is used to execute a command with a constructed argument list

usage:

# find all the ipython notebook files in the "SuperDuper" directory and pass to ls command:

find ./SuperDuper -name "*.ipynb" -print0 | xargs -0 ls

# find all files in SuperDuper folder, pass to grep and search for the string "hello":

find ./SuperDuper -print | xargs grep "hello"




 

