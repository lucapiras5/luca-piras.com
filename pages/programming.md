# Simplicity

- programs are meant to be read by humans, prioritize legibility over cleverness
- quote about debugging being twice as hard as writing code
- compilers are probably more clever than you

# Documentation

- your goal is to reduce tribal knowledge as much as possible, any question about how the codebase works should be answerable by just looking at the codebase, you shouldn't have to ask people
- documentation that is unclear, outdated or contradicts the code is harmful
- avoid creating Chesterton's fences
- avoid "TODO" and "FIXME" if fixing that code wouldn't take long, buggy code will fossilize if it's not cleaned up, and people will start depending on the buggy implementation's behavior
- don't just document the code itself, do document its structure and design too, lay out how data is modeled and transformed by the application

# Comments

- don't restate what the code does
- don't summarize what the code does, create a one-off function with a descriptive name instead
- do use comments if what the code does, or how it does it, is not patently obvious
  - did you need to look up a reference on how to do something?
  - did you use a hacky solution?
  - are you relying on behavior that isn't documented properly, or that you found out about by chance, or trial-and-error?
  - did you have to choose between various approaches? Explain and defend why you picked one over the others, especially if the others seem to be good fits too

# Versioning

- all software evolves, it's important to ensure the evolution is orderly
- software doesn't exist in a vacuum, it has to interact with other software, which depends on the behavior of your software, and may or may not be updated
- to the degree that it is reasonable, maintain backwards compatibility: change default behavior sparingly, and offer the option to switch to the previous behaviors
- version numbers should be meaningful, use semantic versioning
- any fixes that don't change the behavior of the program, but improve security should be backported, even if the program is not accessible to the public (security is also the integrity and availability of data, which includes accidental data corruption)

# Version control

- Git is the industry standard, as asinine it may be there's plenty of tutorials out there
- learn to use command-line git, or else you won't understand what other git clients are doing, and when they break, you don't know how to investigate issues
- your git repo has no external dependencies, just copy if if you're afraid you can't roll back a change
- if code isn't checked in, it doesn't exist, commit often and clean up later to reduce the chances of losing work
- distributed version control does not replace backups
- avoid mono-repos if possible
- never mess with history, especially if it's been pushed, a messy repo history is a truthful repo history
- learn how to rebase and use fix-up commits
- avoid long-lived branches, if you must have them then merge the main branch into them regularly so you can ensure a clean merge into main
- if you prefer to have a rolling main branch, don't use branches to mark releases, use tags instead
- set up hooks to format code, run tests, etc.
- have a backup host for your code, preferably self-hosted
- learn how to use the reflog to undo mistakes

# Optimization

- profile before optimizing, hardware is complex
- make sure the optimization is worth it in terms of portability and long-term maintainability
- hardware is usually cheaper than humans, but you should take into account the lost productivity due to poor performance
