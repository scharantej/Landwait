## Flask Application Design

### HTML Files

**1. landing.html:**

- This is the landing page of the application.
- It should include the following:
  - A heading with the app name, "GetBoard".
  - A brief description of the app.
  - A form for users to enter their email addresses to join the waitlist.
  - A button labeled "Join the Waitlist" that submits the form.

### Routes

**1. @app.route('/', methods=['GET', 'POST'])**

- This route handles both GET and POST requests to the root URL ('/').
- On a GET request, it renders the landing.html template.
- On a POST request, it extracts the email address from the submitted form and saves it to a database or email list. It should also send a confirmation message to the user.

**2. @app.route('/success')**

- This route handles GET requests to the '/success' URL.
- It displays a confirmation page informing the user that they have successfully joined the waitlist.