# One App

Software training.

# Database design.
![image](https://github.com/lizhaoliu-Lec/OneApp/blob/master/assets/database_design.png)

## Getting Started

- Frontend part
    * ...
    ```
    ...
    ```

- Backend part
    * Python 3.6 
    * requirements.txt
    ```
    cd backend
    ```
    ```
    pip install -r requirements.txt
    ```
    ```
    python manage.py makemigrations
    python manage.py migrate
    python insert_data.py # insert some data
    ```
    ```
    inserted user account can be found at main_user.html
    ```
    <table border="1" style="border-collapse:collapse">
    <tr><th>account</th><th>password</th><th>name</th><th>created_datetime</th><th>modified_datetime</th></tr>
    <tr><td>1234567</td><td>1234567</td><td>诸多诱惑</td><td>2019-08-16 14:10:57.908962</td><td>NULL</td></tr>
    <tr><td>098765</td><td>098765</td><td>同学，你狠屌？</td><td>2019-08-16 14:10:57.960825</td><td>NULL</td></tr>
    <tr><td>147qwe</td><td>147qwe</td><td>汤圆.</td><td>2019-08-16 14:10:58.011724</td><td>NULL</td></tr>
    <tr><td>78654ghj</td><td>78654ghj</td><td>七喜先生</td><td>2019-08-16 14:10:58.073522</td><td>NULL</td></tr>
    <tr><td>99999999</td><td>99999999</td><td>同学，你狠屌？</td><td>2019-08-16 14:10:58.142339</td><td>NULL</td></tr>
    <tr><td>6666666666</td><td>6666666666</td><td>全幼儿园最可爱</td><td>2019-08-16 14:10:58.222123</td><td>NULL</td></tr></table>
    ```
    python manage.py runserver
    ```

### Done
- ✅ Init  
- Frontend
    - ✅ ...
- Backend
    - ✅ User register and authentication.
    - ✅ Create user model.
    - ✅ User web API.
    - ✅ Timing record, plan, group.
    - ✅ Create user Timing record, plan, group.
    - ✅ Timing record, plan, group web API.



### TODO
- Frontend
    - ❌ ...

- Backend
    - ❌ wait for demands.
    - ❌ define some models.  
    - ❌ write some apis.
    - ❌ ...

## Built With

* frontend...
* [Django](https://docs.djangoproject.com/en/2.0/) - Web app's backend.
* [DRF](https://www.django-rest-framework.org/) - Web APIs.

## Contributing

Please read [CONTRIBUTING.md](#) for details on our code of conduct, and the process for submitting pull requests to us.

## Version

* **0.0.1** Just start the project.

## Authors
* **lizhao liu** - *backend* - [Github](https://github.com/lizhaoliu-Lec)
* See also the list of [contributors](#) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Not yet.
