======

Welcome My App
======

My app is so great, sometimes it works! Just download the script, add some execute permissions and run it. The results should show you a list of all of the cat pictures on your machine.

`Javascript code block to highlight whats up in my code` 
A single star creates a large heading ** Two stars is less *** Three stars even less **** Four stars looks normal
======

Refer to the Markdown Cheatsheet for examples:

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

You can also look at the source of all of these notes, as they are written in markdown!

Now, add your README to your repo and push.
```
git add . 
git commit -m'added README.md' 
```
At this point we have not done anything to our remote branch. Now, we’ll push all the changes we’ve made to our remote branch so it can be viewable on github.com.

`git push origin main`
Now to add our dev branch, checkout dev and push that too.
```
git checkout dev 
git push origin dev 
```
Verify you can see the Dev branch now as well in your github.com page. You can view your README changes on there as well.

README’s can be very helpful for your users and SHOULD be used to let users (and me) know what you’re doing with your scripts. Hey, you can use it for Project 1!

Branching is a valuable feature in git and will allow you to change files without risking overwriting code or functionality.

Switch back to your main branch since that will be the primary branch we use for this class.

`git checkout origin main` 

If you’re using Windows, open VSCode and open that folder. You’ll notice there is new highlighting and git options in VSCode, because VSCode knows that this is a git repo.

You can actually do most of your Git work within VSCode without using command line. Just click the Github icon on the left. Click the "+" icon to stage your changes. Click the ✓ to commit and add a message. Click the ... and click Push. That's it!