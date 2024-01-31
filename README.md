# Horse Race - from scraping to analysis
This project is part of a lesson posted in my blog [here](https://imuliterno.netlify.app/) . There we go trough [horse statistics website](http://www.racebase.co.nz/jockthis.htm), [jockeys and trainers statistics website](https://loveracing.nz) and extract info in order to make some analysis.

# to-dos
1. extract runs
   
        how to deal with empty pages (when there's no info about the trainer)
   
        what to do when my list of trainer has <trainerA&trainerB>, when the source of previous races is stored for each trainer alone? R: break the string and isolate search
3. get combination of jockey-horse-trainer for each run
4. feature engineering
5. explore how well can I related the acquired data to race winning
