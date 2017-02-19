# Exception and Error Handling in Python 2 and Python 3
by Alex Martelli

- [Abstract](https://us.pycon.org/2016/schedule/presentation/2093/)
- [Slides](http://www.aleax.it/pycon16.pdf)

The best practices of handling errors & exceptions, and how it changes with Python 3.

---

## Opening Matter

- Seeking feedback on *Python in a Nutshell, 3e* Early Release ([Safari][0], [O'Reilly][1])

## Part 1

- `exc` used in place of exception in the slides to fit on screen
- Using break or return in the finally clause of a try-except will cause your exceptions to be swallowed (there's no good reason to do it anyway, but just a strange thing)
- It's totally reasonable to handle then re-raise to provide additional info where Python would not

## Part 2

- 2 major error handling strategies: LBYL, EAFP
- **Look Before You Leap (LBYL)**: check all preconditions are met else raise exception
- **Easier to Ask Foregiveness than Permission (EAFP)**: just do the thing then recover well if it fails (phrase borrowed from Grace Marie Hopper)
- LBYL is riddled with problems
  - Breaks the principle of never duplicate something Python checks for you
  - Obscures code clarity due to structure
  - Things may change at any time (e.g., a file existed when you checked but another process on your machine deleted it when you go to access)
- EAFP done right
  - Get as deep, narrow, and specific as you can to the code that can throw the exception
- "Any program that shows the user a traceback is broken.  The info a coder needs to fix the problem is never what the user needs.  What error message you show to the user is a core part of your user interface."

[0]: https://www.safaribooksonline.com/library/view/python-in-a/9781491913833/
[1]: http://www.oreilly.com/go/python45
