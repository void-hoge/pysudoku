# PYSUDOKU
pysudoku: a simple sudoku solver written in Python. Only 9x9 is supported.

## USAGE
```
$ ./main.py < problems/0.txt
+-------------------+
| 3 6       8     5 |
| 5     2           |
|     4       0     |
|             7     |
|   3 7       8 2 6 |
|               3   |
|   2     5   4     |
|     5 3 0   1     |
| 1 8             7 |
+-------------------+
+-------------------+
| 3 6 1 0 7 8 2 4 5 |
| 5 0 8 2 1 4 6 7 3 |
| 2 7 4 5 3 6 0 1 8 |
| 4 5 2 6 8 3 7 0 1 |
| 0 3 7 1 4 5 8 2 6 |
| 8 1 6 7 2 0 5 3 4 |
| 7 2 3 8 5 1 4 6 0 |
| 6 4 5 3 0 7 1 8 2 |
| 1 8 0 4 6 2 3 5 7 |
+-------------------+
node count: 141596
$ cat problems/0.txt
3 6 - - - 8 - - 5 5 - - 2 - - - - - - - 4 - - - 0 - - - - - - - - 7 - - - 3 7 - - - 8 2 6 - - - - - - - 3 - - 2 - - 5 - 4 - - - - 5 3 0 - 1 - - 1 8 - - - - - - 7
```
The input format is same as the output of sudokugen of [bitsudoku](https://github.com/void-hoge/bitsudoku). Ten problems are included in [problems](problems/).
