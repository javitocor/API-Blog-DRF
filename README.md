# README
<!--
This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to c<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url] 
[![Forks][forks-shield]][forks-url] 
[![Stargazers][stars-shield]][stars-url] 
[![Issues][issues-shield]][issues-url] 
![Hireable](https://cdn.rawgit.com/hiendv/hireable/master/styles/default/yes.svg) 

# Blog Django Rest Framework with Auth Token

>  An API where user can register/login and get a Token that allow them to make CRUD operations with blogs and comments, without token users have permissions ReadOnly.

Additional description about the project and its features.


## Built With

- DJANGO
- DJANGO REST FRAMEWORK
- DJANGO REST AUTH
- GITHUB ACTIONS
- VSCODE

## Getting Started
### Usage
To have this app on your pc, you need to:
* [download](https://github.com/javitocor/API-Blog-DRF/archive/main.zip) or clone this repo:
  - Clone with SSH:
  ```
    git@github.com:javitocor/API-Blog-DRF.git
  ```
  - Clone with HTTPS
  ```
    https://github.com/javitocor/API-Blog-DRF.git
  ```

* In the project directory, you can run:

Create virtual enviroment with:

``` bash
   py -m venv project-name
   project-name\Scripts\activate.bat
```

Run migrations:

``` bash
   py manage.py migrate
```
Run server:

``` bash
   py manage.py runserver
```

Endpoints (visitors without Token Key have ReadOnly permissions):
``` bash
  http://127.0.0.1:8000/rest-auth/registration/
  http://127.0.0.1:8000/rest-auth/login/
  http://127.0.0.1:8000/posts/ (POST,GET)
  http://127.0.0.1:8000/posts/:pk (GET, PUT, DELETE)
  http://127.0.0.1:8000/posts/:pk/comments (GET,POST)
  http://127.0.0.1:8000/posts/:pk/comments/:comment_id (DELETE)
  http://127.0.0.1:8000/users/ (POST,GET)
  http://127.0.0.1:8000/users/:pk (GET, PUT, DELETE)
```

## Author

👤 Javier Oriol Correas Sanchez Cuesta 
- Github: [@javitocor](https://github.com/javitocor) 
- Twitter: [@JavierCorreas4](https://twitter.com/JavierCorreas4) 
- Linkedin: [Javier Oriol Correas Sanchez Cuesta](https://www.linkedin.com/in/javier-correas-sanchez-cuesta-15289482/) 

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](https://github.com/javitocor/API-Blog-DRF/issues).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments 🚀

- [Django Docs](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework Docs](https://www.django-rest-framework.org/)
- [Django Rest Auth](https://django-rest-auth.readthedocs.io/)

## 📝 License

This project is [MIT](lic.url) licensed.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/javitocor/API-Blog-DRF.svg?style=flat-square
[contributors-url]: https://github.com/javitocor/API-Blog-DRF/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/javitocor/API-Blog-DRF.svg?style=flat-square
[forks-url]: https://github.com/javitocor/API-Blog-DRF/network/members
[stars-shield]: https://img.shields.io/github/stars/javitocor/API-Blog-DRF.svg?style=flat-square
[stars-url]: https://github.com/javitocor/API-Blog-DRF/stargazers
[issues-shield]: https://img.shields.io/github/issues/javitocor/API-Blog-DRF.svg?style=flat-square
[issues-url]: https://github.com/javitocor/API-Blog-DRF/issuesover:
