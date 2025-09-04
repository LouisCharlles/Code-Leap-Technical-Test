# Code Leap Backend Test – Readme

## 📌 Overview
This project implements the backend API for the CodeLeap technical test using **Django** and **Django REST Framework (DRF)**. It covers all the required features (CRUD for posts with ownership enforcement) and extends functionality with **likes, comments, pagination, filtering**, and **optional JWT authentication**.

---

## 🚀 Features
- **Posts CRUD** (create, list, update, delete).
- **Ownership protection** via `X-Username` header (per test requirements).
- **Likes** → `/api/posts/{id}/like/` and `/api/posts/{id}/unlike/`.
- **Comments** → nested under posts, with CRUD and ownership rules.
- **Pagination & ordering** → newest posts first, query params supported.
- **Filtering** by `username`.
- **Optional JWT Authentication** as a bonus.

---

## 📂 API Endpoints

### Posts
- `GET /api/posts/` → list posts (with pagination).
- `POST /api/posts/` → create post (`username`, `title`, `content`).
- `PATCH /api/posts/{id}/` → edit own post.
- `DELETE /api/posts/{id}/` → delete own post.

### Likes
- `POST /api/posts/{id}/like/` → like a post.
- `POST /api/posts/{id}/unlike/` → unlike a post.

### Comments
- `GET /api/posts/{id}/comments/` → list comments for a post.
- `POST /api/posts/{id}/comments/` → create comment (`username`, `content`).
- `PATCH /api/comments/{id}/` → edit own comment.
- `DELETE /api/comments/{id}/` → delete own comment.

### Authentication (Bonus)
- Default mode: **`X-Username` header** (required for update/delete).
- Bonus mode: **JWT tokens** (via `djangorestframework-simplejwt`).
  - `POST /api/auth/token/` → obtain access/refresh token.
  - `POST /api/auth/token/refresh/` → refresh token.

If JWT is used, ownership is verified by matching `request.user.username`.

---

## ⚙️ Installation

### Local Setup
```bash
# clone repo
$ git clone https://github.com/LouisCharlles/Code-Leap-Technical-Test
$ cd codeleap_backend

# create virtualenv
$ python -m venv venv
$ source venv/bin/activate  # (Linux/macOS)
$ venv\Scripts\activate    # (Windows)

# install dependencies
$ pip install -r requirements.txt

# run migrations
$ python manage.py migrate

# run server
$ python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

### With Docker
```bash
# build image
docker build -t codeleap-backend .

# run container
docker run -p 8000:8000 codeleap-backend
```

---

## 🧪 Tests
Run all tests with:
```bash
pytest
```

Includes tests for:
- Post CRUD.
- Ownership enforcement.
- Likes.
- Comments.
- JWT authentication flow.

---

## 🌐 Deployment
This project can be deployed on:
- **Heroku** (using Gunicorn).
- **Railway / Render / Fly.io** (simple Docker deploy).
- **AWS EC2/ECS** (bonus if desired).

Environment variables:
```
DJANGO_SECRET_KEY=your-secret
DEBUG=True
ALLOWED_HOSTS=*
```

---

## ✅ Notes for Reviewers
- The core requirement (`X-Username` header ownership) is fully implemented and tested.
- As bonus features, **Likes, Comments, Pagination, and JWT Authentication** are included.
- JWT is **optional** → the system works as required even without it.

---

## 📖 References
- [Django REST Framework](https://www.django-rest-framework.org/)
- [DRF SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Docker](https://docs.docker.com/)

