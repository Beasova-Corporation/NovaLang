   Nepali Programming Language User Guide
Welcome to the Nepali-based programming language! This guide will help you get started with basic arithmetic operations, conditional statements, and loops. All keywords and syntax are in Nepali to make programming more accessible for Nepali speakers.

1. Getting Started
1.1. Language Structure
    • Keywords: All programming constructs (e.g., variable declaration, conditions, loops) use Nepali keywords.
    • Statements End: Every statement should end with a semicolon (;).
    • Blocks: Blocks of code (for conditions and loops) are enclosed in curly braces { }.
1.2. Running Your Code
First, install the nepalilang module in your system by running this command in your terminal:

pip install nepalilang
    • Write your code in a text file using the Nepali keywords.
    • Use the provided interpreter (or your development environment) to compile and run the code.
    • The interpreter will tokenize, parse, and execute your program according to the syntax defined.

2. Arithmetic Operations
Arithmetic operations allow you to perform basic mathematical calculations. The following operators are supported:
    • Addition: +
    • Subtraction: -
    • Multiplication: *
    • Division: / (integer division)
    • Modulo: %
2.1. Variable Declaration and Assignment
    • Declaration Keyword: anka  (used for integers)
Syntax:

anka variable_name = expression;
Example:

import nepalilang

if __name__ == "__main__":
    code = r'''
        anka a = 10;
        anka b = 5;
        anka sum = a + b;
        Dekhau(sum);
    '''
    nepalilang.run_code(code)
Explanation:
    • Declares variables a, b, and sum.
    • Calculates a + b and assigns it to sum.
    • Prints the result (15).
2.2. Order of Operations
Expressions follow the usual order of operations:
    1. Multiplication (*), Division (/), Modulo (%)
    2. Addition (+), Subtraction (-)
    3. You can use parentheses ( ) to group expressions explicitly.

3. Conditional Statements
Conditional statements allow your program to make decisions. The primary keywords are:
    • Yedi →  (for if)
    • Athawa → (for else)

3.1. If-Else Structure
Syntax:
import nepalilang

if __name__ == "__main__":
    code = r'''
        Yedi (condition) {
            // Code block executed if condition is true
        }
        Athawa {
            // Code block executed if condition is false
        }
    '''
    
    nepalilang.run_code(code)


Example:
import nepalilang

if __name__ == "__main__":
    code = r"""
    anka x = 10;
    anka y = 5;
    Yedi (x > y) {
        Dekhau(x);
    } Athawa {
        Dekhau(y);
    }
    """
    
    nepalilang.run_code(code)


Explanation:
    • Declares variable x and y.
    • Check if x > y show x else y.
4. Loops
Loops allow you to execute a block of code repeatedly.
4.1. While Loop (Jabasamma)
A while loop continues to execute as long as the condition remains true.
Syntax:

import nepalilang

if __name__ == "__main__":
    code = r'''
        Jabasamma (condition) {
            // Code block to repeat while condition is true
        }
    '''
    
    nepalilang.run_code(code)

Example:
import nepalilang

if __name__ == "__main__":
    code = r'''
        anka i = 1;
        Jabasamma (i <= 5) {
            Dekhau(i);
            i = i + 1;
        }
    '''
    
    nepalilang.run_code(code)


Explanation:
    • Starts with i = 1.
    • Continues printing i and incrementing it until i becomes greater than 5.
Expected Output
1
2
3
4
5

4.2. For Loop (Kolagi)
The for loop combines initialization, a condition check, and an increment expression in one line.
Syntax:
import nepalilang

if __name__ == "__main__":
    code = r'''
        Ko Lagi (initialization; condition; increment) {
            // Code block to execute in each iteration
        }
    '''
    
    nepalilang.run_code(code)

Example:

import nepalilang

if __name__ == "__main__":
    code = r'''
        Kolagi (anka j = 1; j <= 5; j = j + 1) {
            Dekhau(j);
        }
    '''
    
    nepalilang.run_code(code)
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

4.3. Do-While Loop (Karo-Jabasamma)
A do-while loop executes the code block at least once and then checks the condition at the end.
Syntax:

import nepalilang

if __name__ == "__main__":
    code = r'''
        Karo {
            // Code block to execute at least once
        } Jabasamma (condition);
    '''
    
    nepalilang.run_code(code)

Example:
import nepalilang

if __name__ == "__main__":
    code = r'''
        anka k = 1;
        Karo {
            Dekhau(k);
            k = k + 1;
        } Jabasamma (k <= 5);
    '''
    
    nepalilang.run_code(code)


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


5. Tips for Writing Code in Nepali
Consistency
    • Always use the prescribed Nepali keywords and maintain the correct syntax (e.g., semicolons after statements, proper block enclosure).
Indentation
    • Use indentation within blocks to enhance code readability.

Testing
    • Test your code with simple examples first before building complex logic.
Debugging
If you encounter an error, check that:
    • All blocks are correctly opened and closed with { and }.
    • All statements end with a semicolon (;).
    • The correct Nepali keywords are used.

6. Sample Program
Below is a complete sample program combining arithmetic operations, a conditional statement, and loops:

import nepalilang

if __name__ == "__main__":
    code = r'''
        // Arithmetic Example: Calculate and print sum of two numbers
        anka a = 10;
        anka b = 20;
        anka sum = a + b;
        Dekhau(sum);

        // Loop Example: Print numbers from 1 to 5 using a while loop
        anka i = 1;
        Jabasamma (i <= 5) {
            Dekhau(i);
            i = i + 1;
        }

        // Loop Example: Print numbers from 1 to 5 using a for loop
        Kolagi (anka j = 1; j <= 5; j = j + 1) {
            Dekhau(j);
        }

        // Loop Example: Print numbers from 1 to 5 using a do-while loop
        anka k = 1;
        Karo {
            Dekhau(k);
            k = k + 1;
        } Jabasamma (k <= 5);
    '''
    
    nepalilang.run_code(code)
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
Arithmetic Operations:
    • Use +, -, *, /, and % for calculations.
Conditional Statements:
    • Use Yedi(condition) { ... } with an optional Athawa { ... } to branch execution.
Loops:
    • While Loop: Jabasamma (condition) { ... }
    • For Loop: Kolagi  (initialization; condition; increment) { ... }
    • Do-While Loop:
import nepalilang

if __name__ == "__main__":
    code = r'''
        anka k = 1;
        Karo {
            Dekhau(k);
            k = k + 1;
        } Jabasamma (k <= 5);
    '''
    
    nepalilang.run_code(code)


By following this guide, you can start writing and running simple programs in the Nepali-based programming language, covering arithmetic operations, conditionals, and loops. 
