
<h1 align="center">
   <br>
  <a href="https://s.dou.ua/CACHE/images/img/static/companies/develops-logo/"><img src="https://s.dou.ua/CACHE/images/img/static/companies/develops-logo/ff10e32a80991c6a634119ccc795c174.png" alt="DevelopersToday" width="250"></a>
  <br>
  <br>
  Forum core
  <br>
</h1>

<h4 align="center">Hacker News like forum</h4>

### Fast start

To clone and run this application, you'll need [Git](https://git-scm.com). 
From your command line:

```bash
# Clone this repository
$ git clone https://github.com/HryhorenkoVitalii/Django-Haker-news-core.git

# Go into the repository
$ cd Django-API-TestTask


```
### Request
####   For requests to deployed server you're need use url `http://127.0.0.1:8000`
#### You can use `curl` or [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/907f4883dc56d8162103#?env%5Bcollections_for_developstoday%5D=W3sia2V5IjoibG9jYWwiLCJ2YWx1ZSI6ImxvY2FsIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6InRleHQifSx7ImtleSI6InNlcnZlciIsInZhbHVlIjoic2VydmVyIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6InRleHQifV0=)
* To create new item in database you're need:

### Endpoints
```bash
# GET to view all users, POST to creae new.
/api/v1/user/

# GET to view users id=pk, PUT to update user, DELETE to delete user.
api/v1/user/<int:pk>

# GET to view all posts, POST to creae post.
api/v1/post/

# GET to view post id=pk, PUT to update post, DELETE to delete post.
api/v1/user/<int:pk>

# GET to view all comments, POST to creae comment.
api/v1/comment/

# GET to view comment id=pk, PUT to update comment, DELETE to delete pomment.
api/v1/comment/<int:pk>
```

## Credits

This software uses the following open source packages:

- [Django](https://www.djangoproject.com/)
- [djangorestframework](https://www.django-rest-framework.org/)
