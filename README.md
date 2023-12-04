# LittleLemon Restaurant

<h2>API Endpoints</h2>

<h3>Credentials</h3>

#### Adminuser
- Login: admindjango
- Password: employee@123!

#### Testuser
- Username: testuser
- Password: 12345lemon
- Token for testuser: 1f92f268aa896cd7570bcc993ef339c5dcf10ca6

<h3>Test with Insomnia</h3>


<p>http://127.0.0.1:8000/restaurant/</p>
<p>http://127.0.0.1:8000/restaurant/api-token-auth/</p>
<p>http://127.0.0.1:8000/restaurant/booking/</p>
<p>http://127.0.0.1:8000/restaurant/booking/tables/</p> 
<p>http://127.0.0.1:8000/restaurant/menu-items/</p>
<p>http://127.0.0.1:8000/restaurant/menu-items/1</p>
<p>http://127.0.0.1:8000/auth/users/</p>
<p>http://127.0.0.1:8000/auth/token/login</p>


<h3>Unit testing</h3>

Run command:

    python manage.py test

Don't forget change settings for your mysql db.