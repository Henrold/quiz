# Quiz program
Despite only having 33 lines this program can turn any .csv file into a quiz
## Making questions file
The file with questions in it must be formatted like this

|Question|Answer|
|--|--|

i.e.
|What is the capital of Australia|canberra|
|--|--|
|Which element has the chemical symbol 'O'|oxygen|

> Note: all answers must be in lowercase

To add custom questions put the file in the same folder as the program and replace `QUESTIONFILE = "questions"` with your files name

`QUESTIONFILE = "file" # file to get questions from`

