# Eyob's Blog

Welcome to **Eyob's Blog**, a simple yet powerful blog application built with Flask. This project allows users to create posts, like and unlike them, add comments, and manage content with admin privileges—all with a clean, server-side rendered interface. Whether you're a developer looking to explore Flask or a user wanting a personal blog, this app has you covered.

---

## Features

- **User Authentication**: Secure registration, login, and logout using Flask-Login.
- **Post Management**: View a list of posts on the home page and detailed views for each post.
- **Likes**: Toggle likes on posts with a visual color change (gray to blue) via server-side logic.
- **Comments**: Add, edit, and delete comments, with edit/delete options restricted to comment owners or admins.
- **Admin Privileges**: Admins can delete posts and manage comments across the site.
- **Responsive UI**: Styled with custom CSS and Font Awesome icons for a polished look.
- **Server-Side Rendering**: No heavy JavaScript dependencies; all interactions are handled by Flask.

---

## Tech Stack

- **Backend**: Flask (Python), SQLAlchemy (ORM)
- **Frontend**: Jinja2 templates, HTML, CSS, minimal JavaScript
- **Database**: SQLite (default; configurable for PostgreSQL, MySQL, etc.)
- **Authentication**: Flask-Login
- **Database Migrations**: Flask-Migrate
- **Environment Variables**: Managed with `python-dotenv`
- **Styling**: Custom CSS with Font Awesome icons

---

## Installation

Follow these steps to get the blog running locally:

### Prerequisites
- Python 3.8+
- Git
- A terminal or command-line interface

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/eyobs-blog.git
   cd eyobs-blog