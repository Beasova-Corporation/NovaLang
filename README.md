Hindi Programming Language User Guide
Welcome to the Hindi-based programming language! This guide will help you get started with basic arithmetic operations, conditional statements, and loops in your new language. All keywords and syntax are in Hindi to make programming more accessible for Hindi speakers.

1. Getting Started
1.1. Language Structure
    • Keywords: All programming constructs (e.g., variable declaration, conditions, loops) use Hindi keywords.
    • Statements End: Every statement should end with a semicolon (;).
    • Blocks: Blocks of code (for conditions and loops) are enclosed in curly braces { }.

1.2. Running Your Code
    1. First you have to install hindilang module in your system through running this command in your terminal .
Pip install hindilang .
    2. Write your code in a text file using the Hindi keywords.
    3. Use the provided interpreter (or your development environment) to compile and run the code.
    4. The interpreter will tokenize, parse, and execute your program according to the syntax defined.

2. Arithmetic Operations
Arithmetic operations allow you to perform basic mathematical calculations. The following operators are supported:
    • Addition: +
    • Subtraction: -
    • Multiplication: *
    • Division: / (integer division)
    • Modulo: %
2.1. Variable Declaration and Assignment
Declaration Keyword: ank (used for integers)

Syntax:

ank variable_name = expression;

Example:

import hindilang

if __name__ == "__main__":
    code = r"""
    ank a = 10;
    ank b = 5;
    ank sum = a + b;
    chhapna(sum);
    """
    
    hindilang.run_code(code)


    • Explanation:
        ◦ Declares variables a, b, and sum.
        ◦ Calculates a + b and assigns it to sum.
        ◦ Prints the result (15).
2.2. Order of Operations
Expressions follow the usual order of operations:
    1. Multiplication, Division, Modulo
    2. Addition, Subtraction
You can use parentheses ( and ) to group expressions explicitly.
3. Conditional Statements
Conditional statements allow your program to make decisions. The primary keywords are:
    • agar: if
    • warna: else
3.1. If-Else Structure
Syntax:
import hindilang

if __name__ == "__main__":
    code = r'''
        agar (condition) {
            // Code block executed if condition is true
        }
        warna {
            // Code block executed if condition is false
        }
    '''
    
    hindilang.run_code(code)


3.2. Writing Conditions
A condition typically compares two expressions using relational operators:
    • < : less than
    • <= : less-than-or-equal
    • > : greater than
    • >= : greater-than-or-equal
    • == : equals
    • != : not equal
Example:
ank num = 7;
agar (num  == 2) {
    chhapna("Yes");
}
warna {
    chhapna("No");
}

Explanation:
    • Declares variable num.
    • Checks if num is equal.
    • Prints a message based on chhapna whether it will print Yes or No.

4. Loops
Loops allow you to execute a block of code repeatedly.
4.1. While Loop (jabTak)
A while loop continues to execute as long as the condition remains true.
Syntax:
import hindilang

if __name__ == "__main__":
    code = r'''
        jabTak (condition) {
            // Code block to repeat while condition is true
        }
    '''
    
    hindilang.run_code(code)

Example:
import hindilang

if __name__ == "__main__":
    code = r'''
        ank i = 1;
        jabTak (i <= 5) {
            chhapna(i);
            i = i + 1;
        }
    '''
    
    hindilang.run_code(code)

Explanation:
    • Starts with i = 1.
    • Continues printing i and incrementing it until i becomes greater than 5.
Expected Output:
1
2
3
4
5
4.2. For Loop (keLiye)
The for loop combines initialization, a condition check, and an increment expression in one line.
Syntax:
import hindilang

if __name__ == "__main__":
    code = r'''
        keLiye (initialization; condition; increment) {
            // Code block to execute in each iteration
        }
    '''
    
    hindilang.run_code(code)


Example:
import hindilang

if __name__ == "__main__":
    code = r'''
        keLiye (ank j = 1; j <= 5; j = j + 1) {
            chhapna(j);
        }
    '''
    
    hindilang.run_code(code)

Explanation:

    • Declares j with an initial value of 1.
    • The loop continues while j <= 5.
    • Increments j after each iteration.

Expected Output:

1
2
3
4
5
4.3. Do-While Loop (karo ... jabTak)
A do-while loop executes the code block at least once and then checks the condition at the end.

Syntax:
import hindilang

if __name__ == "__main__":
    code = r'''
        karo {
            // Code block to execute at least once
        } jabTak (condition);
    '''
    
    hindilang.run_code(code)



Example:
import hindilang

if __name__ == "__main__":
    code = r'''
        ank k = 1;
        karo {
            chhapna(k);
            k = k + 1;
        } jabTak (k <= 5);
    '''
    
    hindilang.run_code(code)


Explanation:
    • Initializes k with 1.
    • Executes the block, prints k, increments k.
    • After executing the block, checks if k <= 5 to decide whether to repeat.
Expected Output:
1
2
3
4
5
5. Tips for Writing Code in Hindi
    • Consistency:
Always use the prescribed Hindi keywords and maintain the correct syntax (e.g., semicolons after statements, proper block enclosure).
    • Indentation:
Use indentation within blocks to enhance code readability.
    • Testing:
Test your code with simple examples first before building complex logic.
    • Debugging:
If you encounter an error, check that:
        ◦ All blocks are correctly opened and closed with { and }.
        ◦ All statements end with a semicolon (;).
        ◦ The correct Hindi keywords are used.

6. Sample Program
Below is a complete sample program combining arithmetic operations, a conditional statement, and loops:
import hindilang

if __name__ == "__main__":
    code = r'''
        // Arithmetic Example: Calculate and print sum of two numbers
        ank a = 10;
        ank b = 20;
        ank sum = a + b;
        chhapna(sum);


        // Loop Example: Print numbers from 1 to 5 using a while loop
        ank i = 1;
        jabTak (i <= 5) {
            chhapna(i);
            i = i + 1;
        }

        // Loop Example: Print numbers from 1 to 5 using a for loop
        keLiye (ank j = 1; j <= 5; j = j + 1) {
            chhapna(j);
        }

        // Loop Example: Print numbers from 1 to 5 using a do-while loop
        ank k = 1;
        karo {
            chhapna(k);
            k = k + 1;
        } jabTak (k <= 5);
    '''
    
    hindilang.run_code(code)



Expected Output:
30
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5










7. Summary
    • Arithmetic Operations:
Use +, -, *, /, and % for calculations.
    • Conditional Statements:
Use agar (condition) { ... } with an optional warna { ... } to branch execution.
    • Loops:
        ◦ While Loop: jabTak (condition) { ... }
        ◦ For Loop: keLiye (initialization; condition; increment) { ... }
Do-While Loop:

import hindilang

if __name__ == "__main__":
    code = r'''
        ank k = 10;
        karo {
            chhapna(k);
            k = k + 1;
        } jabTak (k <= 5);
    '''
    
    hindilang.run_code(code)

By following this guide, you can start writing and running simple programs in the Hindi-based programming language, covering arithmetic operations, conditionals, and loops. 
