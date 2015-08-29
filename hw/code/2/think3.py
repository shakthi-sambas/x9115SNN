import traceback
import sys

def exercise_3_1():
    print "\n#########################"
    print "Solution for Exercise 3.1"
    print "#########################\n"
    
    try: 
        repeat_lyrics()
    
        def print_lyrics():
            print "I'm a lumberjack, and I'm okay."
            print "I sleep all night and I work all day."
            
        def repeat_lyrics():
            print_lyrics()
            print_lyrics()
    
    except:
        print traceback.format_exc()

def exercise_3_2():
    
    print "#########################"
    print "Solution for Exercise 3.2"
    print "#########################\n"
            
    def repeat_lyrics():
        print_lyrics()
        print_lyrics()
    
    def print_lyrics():
        print "I'm a lumberjack, and I'm okay."
        print "I sleep all night and I work all day."

    repeat_lyrics()

def exercise_3_3(s):
    print "\n#########################"
    print "Solution for Exercise 3.3"
    print "#########################\n"
    
    def right_justify(s):
        print s.rjust(70)
    
    right_justify(s)

def exercise_3_4_1():
    print "\n###########################"
    print "Solution for Exercise 3.4.1"
    print "###########################\n"
    
    def do_twice(f):
        f()
        f()
    
    def print_spam():
        print 'spam'
    
    do_twice(print_spam)

def exercise_3_4_2():
    print "\n###########################"
    print "Solution for Exercise 3.4.2"
    print "###########################\n"
    
    def do_twice(f, value):
        f(value)
        f(value)
    
    def print_spam(value):
        print value
    
    do_twice(print_spam, 'Solution for 3.4.2')

def exercise_3_4_3():
    print "\n###########################"
    print "Solution for Exercise 3.4.3"
    print "###########################\n"
    
    def do_twice(f, value):
        f(value)
        f(value)
    
    def print_twice(value):
        print value
        print value
    
    do_twice(print_twice, "Solution for 3.4.3")

def exercise_3_4_4():
    print "\n###########################"
    print "Solution for Exercise 3.4.4"
    print "###########################\n"
    
    def do_twice(f, value):
        f(value)
        f(value)
    
    def print_twice(value):
        print value
        print value
    
    do_twice(print_twice, "spam")



def exercise_3_4_5():
    print "\n###########################"
    print "Solution for Exercise 3.4.5"
    print "###########################\n"
    
    def do_twice(f, value):
        f(value)
        f(value)
        
    def do_four(f, value):
        do_twice(f, value)
        do_twice(f, value)

    def print_twice(value):
        print value
        print value
    
    do_four(print_twice, "spam")

def exercise_3_5_1():
    print "\n###########################"
    print "Solution for Exercise 3.5.1"
    print "###########################\n"
    boxes_in_rows = 2
    rows = boxes_in_rows * 5
    while rows >= 0:
        if rows % 5 == 0:
            for i in range(0, boxes_in_rows):
                print "+ - - - -", 
            print "+"
        else:
            for i in range(0, boxes_in_rows):
                print "|        ",
            print "|"
        rows = rows - 1
    
def exercise_3_5_2(boxes_in_rows):
    print "\n###########################"
    print "Solution for Exercise 3.5.2"
    print "###########################\n"
    rows = boxes_in_rows * 5
    while rows >= 0:
        if rows % 5 == 0:
            for i in range(0, boxes_in_rows):
                print "+ - - - -", 
            print "+"
        else:
            for i in range(0, boxes_in_rows):
                print "|        ",
            print "|"
        rows = rows - 1
            

    
    
exercise_3_1()
exercise_3_2()
exercise_3_3('allen')
exercise_3_4_1()
exercise_3_4_2()
exercise_3_4_3()
exercise_3_4_4()
exercise_3_4_5()
exercise_3_5_1()
exercise_3_5_2(4)