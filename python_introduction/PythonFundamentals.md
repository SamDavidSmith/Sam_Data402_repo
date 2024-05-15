![](data_402_python/python_introduction/images/python_fund.png)

### Why use Python?
* Open-source (it's **FREE** to use personally or commercially)
* You can use it on:
  1. Windows
  2. Mac
  3. Linux
* Helpful community: it is quite likely someone has already encountered your problem before.
* **LOTS** of possible applications, such as web development, machine learning, and statistical analysis.

## How to Download Python:

* Head to the [Python downloads page](python.org/downloads/).
* It is **recommended** to use PyCharm (head [here](https://www.jetbrains.com/pycharm/download/?section=windows)  and scroll to download the free Community Edition)  to edit your code. It's a really helpful tool which can even suggest ways to improve your work.![img_2.png](python_introduction/images/img_2.png)
* Open a **NEW** Project in PyCharm.
* Choose Pure Python on the languages tab.
* Press *Create*.
* You're ready to start coding in Python.

You should test that your computer can interpret the language first. It's a formality to use: <br>
```commandline
print("Hello World")
```
Try using the '#' character on the same line (outside the print statement) to **comment** your name, like this: <br>

`print("Hello World") # My name is Sam!`

The output `Hello World` is a string.

## Data Types ##

There are three fundamental data types used within any usual Python file.
1. **Numbers**
   1. `int`: For integers like `23`, `350000` or `0`.
   2. `float`: For decimals like `5.555`.
2. **Strings** like `"Hello World"`.
3. **Boolean** for True or False, or 1 or 0.

Use `print(type("your data type here"))` to check your data type.

## Maths Operators

You can use these with **Numbers**.
* `+`: Add
* `-`: Subtract
* `*`: Multiply
* `/`: Divide

Python is a calculator! <br>
**TASK!** Try dividing by 0 to recognise your first error.

## Booleans

Let's talk about a boolean quickly.<br>
You can use the standard operators: <, > and a range of lesser known ones:
* `==` equal to
* `!=` not equal to
* `<=` less than or equal to
* `>=` more than or equal to

to create a boolean, True or False. For example, `print(2==3)` will return `False`. <br>To combine every data type, we can write the line: <br>
```python
print(15 >= len("Hello World") )
``` 
which equals `True`. <br>**TASK!** Can you figure out what this boolean is calculating?
<br>***BONUS TASK!*** If you can slice strings with the square brackets, can you figure out what the boolean would be for:
```python
print("o" == "Hello World"[4])
```
*Hint*: The index number line starts at 0 in Python, not 1!

## Variables

You don't want to write everything in the print statement all the time. You can store pretty much anything as a variable, which is usually a lowercase character or name without quotes. Now we set:
```python
welcome_test = "Hello World"
```
So, try running: `print(welcome_test[4])` to help you with the bonus task.
<br> We have entered a world of possibilities here:
```python
firstname = "Sarah"
lastname = "Connor"

print('I am looking for: ' + firstname + " " + lastname)
```
The `+` character binds strings together, but you need to include spaces manually. If you want to write ```print('I'm looking for: "``` then you have used the apostrophe twice, and the `I` is your only string!
```python
print('I'm looking for: ' + firstname + " " + lastname)
```
This means Python will think the unquoted letters are variables, but they are not here. Here are your options:
* Use double quotes: `"I'm looking for"`
* Use the character `'\'` before the issue: 
```python
print('I\'m looking for: ')
 ```
The functions int() and str() are very useful. This is so we can bind a number and a string together:
```python
print(str(3) + " " + "Sarah Connors") # is right.
# str() is turning the integer into a string.
print(3 + " " + "Sarah Connors") # is wrong!
```

## Control Flow

You want to start looking at making Python functions soon, like making a number guessing minigame. Now, these next three bullet points will be very special to your Python functions. <br>Let's set:
`fullname = firstname + " " + lastname`
* ### If statement
  * `if firstname == 'Sarah' and lastname == 'Connor':`  
    * `     print(fullname)`
  * This executes the operation after the semicolon if the boolean is true. You would want a space of four spacebar touches to start the operation.
* ### Elif statement
  * `elif firstname == 'Sarah' or lastname == 'Connor':`
    * `print(fullname + ": Worth a look")`
  * This will process when the if statement isn't true, as it stands for else if.
* ### Else statement
    * `else:`
      * `print('Not her')`
    * This performs when your if statements haven't captured any True values. 

## Lists

Let's use a list to combine the three bullet points so that we can turn it into our own Terminator function.

Our list will be a Yellow Pages book: <br>
`fullnames = ['Gwyneth O\'Hara', 'Eleanor Connor', 'Sarah Blake', 'Sarah Connor'] # Remember your '\' character.` 

So, here we go:
```python
firstname = fullname.split(" ")[0]
lastname = fullname.split(" ")[1] 
# What are these lines doing to the full names?

if firstname == 'Sarah' and lastname == 'Connor':
    print(fullname)
elif firstname == 'Sarah' or lastname == 'Connor':
    print(fullname + ": Worth a look")
else:
    print('Not her')
```
It's best to look at Python and try to read out what each line is doing. It's really useful to start off with something which you can build on. Just to warn you, we will be using a 'for loop' in the next section. Try to understand what each line in the function is doing, and why we're using each name in the phone book.

## Functions
![terminator](data_402_python/python_introduction/images/Terminator-2-judgement-day.jpg)<br>
The best way to learn is with an example. Previously, we had the Yellow Pages we will be using, and we'll assign it to the variable `area_phone_book`.
<br> 
```
area_phone_book = ['Gwyneth O\'Hara', 'Eleanor Connor', 'Sarah Blake', 'Sarah Connor']
``` 
Remember your `'\'` character.
Now, our for loop will consist of:
```python
for full_name in phone_book:
```
which cycles over each name in our address book. After the semicolon, we will be performing operations on each name we have chosen from the fullnames. Firstly, we have Gwyneth, then secondly, we would have Eleanor etc. <br> How are we going to find Sarah Connor? With our function we're calling `terminator()`:

```python
def terminator(phone_book):
    for full_name in phone_book:
        # We are performing the following over the first name, then the second, then etc.
        firstname = full_name.split(" ")[0]
        lastname = full_name.split(" ")[1]

        if firstname == 'Sarah' and lastname == 'Connor':
            print(full_name + ' is the one I\'m looking for')
        elif firstname == 'Sarah' or lastname == 'Connor':
            print(full_name + ": Worth a look")
        else:
            print('Not her')
```
When we run the single line `terminator(area_phone_book)` we get:
```
Not her
Eleanor Connor: Worth a look
Sarah Blake: Worth a look
Sarah Connor is the one I'm looking for
```
based on the order of the names in the area's phone book. <Br><br> Everytime we pick a name from the phone book with the for loop, we decide to split up the name, analyse the first and last names, and then print the Terminator's calculations. <br><br> The function only stops when there are no more names in the phone book to pick. <Br> <br>
**TASK!** Can you think of any ways to make the function better? <br>
*Hint:* Maybe try listing the name every time, even if it's not Sarah Connor at all?

## Thanks for reading!
### You'll be a Python legend in no time!

