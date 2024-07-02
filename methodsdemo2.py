

def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum1 = sum_nums(2, 8)

sum2 =  sum_nums(3, 3)

#string_add = sum_nums('one', 2)
#print(string_add)

print(sum1)
print("*************")

def isMetro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        return True
    else:
        return False

x = isMetro('boston')
print(x)


How to Resolve Merge Conflicts in Git?
Lesson 7 of 12By Sana Afreen

Last updated on Oct 11, 20231262340
How to Resolve Merge Conflicts in Git?
PreviousNext
Table of Contents
What is a Git Merge Conflict?How to Resolve Merge Conflicts in Git?Git Commands to Resolve ConflictsTypes of Git Merge Conflicts Demo: Resolving Git Merge ConflictsView More
Git is one of the most popular source-control systems that enable software development professionals in all industries, enabling multiple team members to work concurrently on projects. Since many users are simultaneously working from different places on the same file, however, you may end up with a merge conflict. This article explains the basics of Git merge conflicts and one of the advanced operations of Git: resolving a Git merge conflict. 

What is a Git Merge Conflict?
A git merge conflict is an event that takes place when Git is unable to automatically resolve differences in code between two commits. Git can merge the changes automatically only if the commits are on different lines or branches.

The following is an example of how a Git merge conflict works:

pull-push.

Let’s assume there are two developers: Developer A and Developer B. Both of them pull the same code file from the remote repository and try to make various amendments in that file. After making the changes, Developer A pushes the file back to the remote repository from his local repository. Now, when Developer B tries to push that file after making the changes from his end, he is unable to do so, as the file has already been changed in the remote repository.

To prevent such conflicts, developers work in separate isolated branches. The Git merge command combines separate branches and resolves any conflicting edits.

Now that we have gone through the basics of the Git merge conflict, let’s look at the various types of conflicts next.

Get All Your Career Growth Questions Answered!
DevOps Engineer Masters ProgramEXPLORE PROGRAMGet All Your Career Growth Questions Answered!
How to Resolve Merge Conflicts in Git?
There are a few steps that could reduce the steps needed to resolve merge conflicts in Git.

Step 1: The easiest way to resolve a conflicted file is to open it and make any necessary changes.

Step 2: After editing the file, we can use the git add a command to stage the new merged content.

Step 3: The final step is to create a new commit with the help of the git commit command.

Step 4: Git will create a new merge commit to finalize the merge.

Learn from Experienced Industry Experts!
DevOps Engineer Masters ProgramEXPLORE PROGRAMLearn from Experienced Industry Experts!
Let us now look into the Git commands that may play a significant role in resolving conflicts.

