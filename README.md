# Welcome to Leamington Spa Adventures Blog

## A Community-Driven Photography and Exploration Blog

Leamington Spa Adventures Blog celebrates the beauty of Leamington Spa and the West Midlands through the lens of our talented community. We offer a platform for photographers and adventurers to share their stories, inspire others, and connect with like-minded individuals.

[Link to Live Site](#)

This project is created to showcase local beauty and foster community engagement through photography and storytelling.

Built by [Suba Suresh]

---

# Table of Contents  
1. [Project Overview](#project-overview)
2.  [ UX ](#ux)
3. [ Agile Methodology for project planning ](#Agile-Methodology-for-project-planning)
3. [Features Implemented](#features-implemented)
4. [Future Features](#future-features)
5. [Technology Stack](#technology-stack)
6. [Testing and Validation](#testing-and-validation)
7. [Known Bugs](#known-bugs)
8. [Deployment](#deployment)
9. [Resources](#resources)
10. [Credits and Acknowledgements](#credits-and-acknowledgements)

---

## Project Overview

### Overview
Leamington Spa Adventures Blog provides a vibrant space for photographers and bloggers to showcase their work and connect with others. Our platform focuses on the natural beauty, landmarks, and hidden gems of Leamington Spa and the West Midlands.

#### Target Audience
Our primary users are local photographers, bloggers, and adventure enthusiasts who are passionate about exploring and documenting the beauty of Leamington Spa and the surrounding areas. They seek a supportive community where they can share their experiences and connect with others who share their interests.

#### Goals
- **Highlight Local Adventures:** Focus on showcasing the natural beauty and landmarks of our region.
- **Foster Community:** Create an environment where members can learn from each other and build connections.
- **Inspire Exploration:** Encourage readers to explore and discover new perspectives.
- **Celebrate Diversity:** Reflect the richness of our community through diverse experiences and viewpoints.

# UX

## Database Planning

I used Lucidchart to create my database entity relationship diagrams. Below you can see how each model relates to eachother. (need to add the database link here)  


## Agile Methodology for project planning

I used agile methodology for the first time when planning full-stack django website with a focus on delivering the basic functionalities. I prioritized features by labeling them as "must-have" or "could-have" and moved some less critical ones to future development. To guide my development process, I created user stories for both the admin user and regular visitors. These stories helped to define the features and functionalities that were most important to project's target audience.

As a solo developer who was learning a lot during development, I faced challenges in estimating the time required for each tasks, bugs and only had a basic concept of what I would create. Therefore, I kept things simple and focused on achievable goals. As the project grew, I was able to add more advanced features and group user stories are meant to mark significant points in time in terms of project completion.

To keep track of progress, I used a kanban board divided into following sections: "to do", "in progress" "done",  and "bugs" that allowed to visualize all tasks and prioritize next steps.

By using agile methodology, I was able to stay organized and focused on delivering the most important features, while also allowing flexibility for future development

### Wireframes
Include wireframes if available.

Description of the wireframes and how they guided the design.

[Back to Top](#table-of-contents)

---


[Back to Top](#table-of-contents)

---

## Features

- **Navbar and Main Menu**:
  - Uses Bootstrap navbar component for fixed top navigation with logo and links.
  - Displays different options for authenticated and admin users.
  - Responsive design with collapsible mobile menus.

- **Footer**:
  - Contains copyright info, quick navigation links, and social media icons.
  - Responsive design adjusts to small devices with a single-column layout.

- **Home Page**:
  - **Carousel**: Showcases images related to Landscape, Nature, Architecture, and Travel with Bootstrap carousel.
  - **Hero Section**: Introduces the site with a welcome message and call-to-action buttons.
  

- **Blog**:
  - Displays a paginated list of posts with featured images, titles, excerpts, and details.
  - Posts can be browsed by tags.

- **Full Post View**:
  - Includes featured image,  info, like and comments section.

- **About Page**:
  - Contains introductory paragraphs about the team, their passion, and mission.
  - Includes a FAQ section using Bootstrap accordion.

- **Contact Page**:
  - Features a contact form and location info with Google Maps integration.
  - Uses Google reCAPTCHA v2 to prevent spam.

- **Admin Panel**:
  - Manages blog posts with details such as title, slug, author, category, tags, status, and creation date.
  - Allows bulk status updates and filtering.

- **User Dashboard**:
  - Provides statistics on the user's posts with CRUD functionality.
  

- **Accounts Templates**:
  - Handles user dashboard's, and Personal details on account management.

- **Add/Edit Post - Form Validation**:
  - Validates post fields with JavaScript and provides user feedback.

- **Messages**:
  - Utilizes Django messages with Bootstrap toast components for user feedback.


## Future Features
- **Enhanced Search Functionality:** Implement a search bar to find specific content.
- **Advanced Filtering:** Improve filtering options for a better user experience.
- **User Profiles:** Add features for users to showcase their most popular content and achievements.
- **Interactive Maps:** Integrate maps to show locations of featured adventures.

[Back to Top](#table-of-contents)

---

## Technology Stack
- **HTML/CSS:** For page structure and styling.
- **JavaScript:** For interactive elements.
- **Python/Django:** Backend framework.
- **Bootstrap:** For responsive design.
- **Cloudinary:** For image hosting.
- **Heroku:** For deployment.
- **Git/GitHub:** For version control and collaboration.

[Back to Top](#table-of-contents)

---

### Software and Libraries
- [Animate On Scroll AOS](https://michalsnik.github.io/aos/)
- [Bootstrap 5](https://blog.getbootstrap.com/2022/11/22/bootstrap-5-2-3/)
- [Cloudinary](https://cloudinary.com/)
- [Django](https://www.djangoproject.com/)
- Postregesql
- [Heroku](https://heroku.com)


### Python Libraries
- [cloudinary](https://pypi.org/project/cloudinary/)
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
- [django-allauth](https://pypi.org/project/django-allauth/)
- [django-social-share](https://pypi.org/project/django-social-share/)
- [django-summernote](https://pypi.org/project/django-summernote/)
- [django-taggit](https://pypi.org/project/django-taggit/)
- [gunicorn](https://pypi.org/project/gunicorn/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [PyJWT](https://pypi.org/project/PyJWT/)
- [pytz](https://pypi.org/project/pytz/)
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/)
- [sqlparse](https://pypi.org/project/sqlparse/)
- [pygraphviz](https://pypi.org/project/pygraphviz/)

## Testing and Validation

### Responsiveness


**Desktop View**

**Mobile View**

### Validation
- **HTML Validation:** W3 HTML Validator
- **CSS Validation:** W3 CSS Validator
- **Python Linter:** CI Python Linter

[Back to Top](#table-of-contents)

---

## Known Bugs
- **Image Upload Issue:** Conflicts with image handling on the Profile page.
- **Comment Moderation:** Occasionally slow to update when delete the comments and likes.
- **Search Functionality:** Not yet implemented as planned.

[Back to Top](#table-of-contents)

---

## Deployment

### Deployment Guide
1. Create and Configure Heroku App
2. Set Up Environment Variables
3. Push Code and Create Procfile
4. Deploy and Monitor

### Cloning the Repository
- **Forking:** [GitHub Repository Link](#)
- **Cloning:** Follow the GitHub instructions to clone the repository.

[Back to Top](#table-of-contents)

---

## Resources
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [Heroku Documentation](https://devcenter.heroku.com/categories/reference)

[Back to Top](#table-of-contents)

---

## Credits and Acknowledgements

- **Code Institute** course content for providing the knowledge and guidance to build the project
- GitHub user **sojourn** for sharing a best practice README structure
- Course Facilitator **David Calikes** for his unwaving support and guidance during the process 
- Tutor **Alexander* for his endless patience and support with trouble shooting issues
- Tutor **Kevin Loughrey** for his helpful SME sessions and constant support
- My fellow **cohort peers** for their support, help with trouble shooting issues and sharing the experience

##### [ Back to Top ](#table-of-contents)
[Back to Top](#table-of-contents)
