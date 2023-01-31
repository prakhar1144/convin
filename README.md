# Convin

### Demo Video

[screen-capture.webm](https://user-images.githubusercontent.com/56781761/215750506-86717897-e353-4f13-82d8-99892dd3a27a.webm)


### Deployed at [convin.pythonanywhere.com](http://convin.pythonanywhere.com/)

### Extras
* I have followed the git **rebase oriented** workflow.
* Each [commit](https://github.com/prakhar1144/convin/commits/main) has been created with a **meaningful commit message**.
* [Helper functions](https://github.com/prakhar1144/convin/tree/main/helpers) are used instead of putting everything inside views. **DRY**
* Only Google's provided **standard libraries** are used.
* [URL configurations](https://github.com/prakhar1144/convin/blob/main/convin/urls.py#L20) keeping **extensiblity** (v2, v3) in mind.
* Exception handling with appropriate status codes.
* `rest/v1/calendar/init`
  > returns the auth_url.

  > now depending on the client e.g. mobile, desktop, etc. we can open (prompt) the url in a new browser tab.
* `rest/v1/calendar/redirect`
  > serves as a redirect URI.

  > It fetches auth_code and then exchanges the code for 'access_token' and 'refresh_token' from the google' server.
* **We can use any client to access the api endpoints**

### Important Note:
* If the status of our app is set to **Production** (i.e. everyone can use it)
  * Then our app needs verification from Google to use the scope (which is not possible in 48 hours)
* Currently the status of our app is set to **Testing**
  * A whitelisted set of users can use the scope without verfification (Which is our case)
* Hence, If you want to test this via [convin.pythonanywhere.com](https://convin.pythonanywhere.com)
  * Login using this Google account (I have whitelisted this as test user)
  * Account: testnith0@gmail.com , Password: TestAccount@1144

* Another option is to setting this up locally and configuring your own `client_secret.json` and test users.
