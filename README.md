Mel told me that the melon delivery have been going fine but are deliverers have not been getting tipped properly. He want us to build a tip calculator. He said  for this app we need to build the following pages.

1. Homepage
2. Cost Page
3. Calculated tips page
4. Tip now page
5. Login page

He want you to write a script that can calculate tips.

He want the homepage('/') to have:
- The name of this product "UberMellonTipper"
- a picture of a tipjar
- a login button if the user hasn't logged in
- a get start button if the user has logged in 

He want the login-page('/login') to have:
- a simple form with an email and password field.
- User should recieve a flash message saying the are logged in 
- Should return user to homepage after login.

He want the cost-page('/cost') to have:
- A Heading of Cost
- a form that allows the user to enter the cost
- Only show page to logged in users

He want the calculated-tips-page('/tip/{cost}') to have:
- The pre-Tip cost
- a list of tip amount calculated for 0%, 5%, 10%, 15%, 20% and 25%.
- each amount should have a button that allow the user to tip through our patform by setting a cookie set for tip amount.
- Only show page to logged in users

He want the tip-now-page('/tip/now') to have:
- if there is a cookie set for tip amount the user should be able to view page.
- if no cookie set for tip amount send user to cost page.
- User should see a message about tipping the server that includes the amount and have a button to send payment.
- if user presses button cookie should be remove and user should be redirected 
to homepage.
- User should recieve a flash message with payment info
- Only show page to logged in users

He also want you to write a suite of test.

He also said that we can only devote 2 hours to this project but if we have time to make it look pretty with the ubermelon colors, also add an api endpoint ( GET "/Api/tip?cost={cost}") that returns a json containing pre-tip cost and a list of tip amount calculated for 0%, 5%, 10%, 15%, 20% and 25% and also add an api endpoint ( GET "/Api/tip?cost={cost}&percent={percent}") that returns a json containing pre-tip cost and a list of tip amount calculated for 0%, 5%, 10%, 15%, 20% and 25%. The head
Engineer said something called `json.dumps` might help with this.