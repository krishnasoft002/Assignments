
1. Why are functions advantageous to have in your programs?

Ans: It helps to divide the large programs into small groups so that we can read the code, and debug the program faster and better. Python Functions stop us from writing the same logic various times. We can bind the logic in one function and then call the same over and over.

2. When does the code in a function run: when it's specified or when it's called?

Ans: A function is a block of code that only runs when it is called. Functions return a value using a return statement, if one is specified. A function can be called anywhere after the function has been declared. By itself, a function does nothing.

3. What statement creates a function?
Ans: A function is a block of code that performs some specific task and returns back to the caller. It has a unique name.

To create function def keyword is use in Python. Define a unique name for the function and in parenthesis, you can specify your parameters.

Function block starts with colon(:) symbol.

Syntax –

def function-name(paramenter):
  # statement

Example:def callMe():
  print("Function is called")     
 
4. What is the difference between a function and a function call?

Ans:  Function is a part of program defined seperately outside the program whereas function call is calling of the function. taking an anology of bread and jam,jam is the function defined by you and application of jam to bread is function call.

5. How many global scopes are there in a Python program? How many local scopes?

Ans: Global Variable in Python – Variables created outside the function are called global variables. Anyone can access the global variable, both inside and outside of a function. 
only one global Python scope per program execution. This scope remains in existence until the program terminates and all its names are forgotten.

An unqualified name inside a function, Python searches three scopes—the local (L), then the global (G), and then the built-in (B)—and stops at the first place the name is found.


6.What happens to variables in a local scope when the function call returns?

When a function returns, the local scope is destroyed, and all the variables in it are forgotten.

7. What is the concept of a return value? Is it possible to have a return value in an expression?

Ans: The specific value returned from a function is called the return value. When the return statement is executed, the return value is copied from the function back to the caller. This process is called return by value.

If a return statement is followed by an expression list, that expression list is evaluated and the value is returned: If a return statement is reached during the execution of a function, the current function call is left at that point: If there is no return statement the function returns None when it reaches the end:


8.If a function does not have a return statement, what is the return value of a call to that function?

Ans: If a function doesn't specify a return value, it returns None. In an if/then conditional statement, None evaluates to False.


9. How do you make a function variable refer to the global variable?

Ans: function variable refer to a global variable in a function, you can use the global keyword to declare which variables are global.


10. What is the data type of None?

Ans: None keyword is an object and is a data type of none type class ans None keyword is used to define a null variable or object.


11.What does the sentence import areallyourpetsnamederic do?

Ans: That import statement imports a module named areallyourpetsnamederic. 

12.If you had a bacon() feature in a spam module, what would you call it after importing spam?

Ans: this function is called with spam.bacon()


13. What can you do to save a programme from crashing if it encounters an error?

Ans: To exclude the possibility that a certain program or application sparkles the PC crashing consecutively issue, you can try booting in safe mode and then configuring applications to uninstall. If your computer can run normally after booting in safe mode, the program or application is the fault. In this case, you can uninstall it.

14. What is the purpose of the try clause? What is the purpose of the except clause?

Ans: e try-except clause is to handle exceptions (errors at runtime). The syntax of the try-except block is: try: the code with the exception (s) to catch. If an exception is raised, it jumps straight into the except block. except: this code is only executed if an exception occured in the try block.







