"""
Creating an Application in SalesForce.com using Apex programming
Language.
"""

public class Calculator {

    public static void add(Integer a, Integer b) {
        Integer result = a + b;
        System.debug('Addition = ' + result);
    }

    public static void sub(Integer a, Integer b) {
        Integer result = a - b;
        System.debug('Subtraction = ' + result);
    }

    public static void mul(Integer a, Integer b) {
        Integer result = a * b;
        System.debug('Multiplication = ' + result);
    }

    public static void div(Decimal a, Decimal b) {
        Decimal result = a / b;
        System.debug('Division = ' + result);
    }
}

// Anonymous window, Enter Apex Code
Calculator.add(10, 5);
Calculator.sub(10, 5);
Calculator.mul(10, 5);
Calculator.div(10, 5);


//Directions to execute this practical
/*
1. Visit salesforce.com or search SalesForce org web page
2. Redirect to sign up page, and register yourself
3. Go to login page and login with your credentials
4. Open Developer Console
5. Select File -> New -> Apex Class
6. Initialize class with a suitable name
7. Write code for perform basic calculator operations
8. Inside code include various functions like addition, subtraction etc.
9. Visit the task menu, and click debug
10. Inside new redirected terminal enter the Apex code
11. Save the code files, both the Apex one and Main class one
12. Click on Open Log and then click execute
13. The output is shown in raw inconsistent format
14. Click on debug only checkbox to filter results
15. Required, readable output is displayed
*/