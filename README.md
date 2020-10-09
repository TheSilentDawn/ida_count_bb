# ida_count_bb

## Brief
This is an IDA pro plugin used to count the basic blocks of each function in a binary file.

## Install
1. Copy `CounterBasicBlock.py` into the directory `plugins` inside where your IDA installed
2. Copy directory `bbcounter` into the directory `python` inside where your IDA installed

## How to use
1. Use IDA pro open your binary file
2. Use hot key `Alt + F6` to active plugin and output the result.

## Note
1. The x86 program will get more basic blocks than we see is due to the fact that gcc enable `Stack Protector` defaulty. So you need to add `-fno-stack-protector` to disable it.

## Ref
1. https://huangzhenyang.github.io/2019/04/20/IDApython%E6%8F%92%E4%BB%B6%E7%BC%96%E5%86%99%E5%8F%8A%E8%84%9A%E6%9C%AC%E6%89%B9%E9%87%8F%E5%88%86%E6%9E%90%E6%95%99%E7%A8%8B/
2. https://stackoverflow.com/questions/2340259/how-to-turn-off-gcc-compiler-optimization-to-enable-buffer-overflow