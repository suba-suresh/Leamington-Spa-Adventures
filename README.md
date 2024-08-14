# Welcome to Leamington Spa Adventures Blog

## A Community-Driven Photography and Exploration Blog in West Midlands

Leamington Spa Adventures Blog celebrates the beauty of Leamington Spa and the West Midlands through the lens of our talented community. We offer a platform for photographers and adventurers to share their stories, inspire others, and connect with like-minded individuals.

[Link to Live Site](#)



This project is created to showcase local beauty and foster community engagement through photography and storytelling.

Built by [Suba Suresh]

---

# Table of Contents  
1. [Project Overview](#project-overview)
2. [User Experience Design](#user-experience-design)
3. [Agile Methodology for project planning ](#agile-methodology-for-project-planning)
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


## User Experience Design

### As a Site User

- [#1](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/1) As a site user, I can register with my email and verify it so that I can access the platform.
- [#9](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/9) As a site user, I can create, read, update, and delete my own posts to manage my content.
- [#10](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/10) As a site user, I can like and comment on others' posts to engage with the content.
- [#11](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/11) As a site user, I am restricted from liking and commenting on my own posts to prevent self-engagement.
- [#12](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/12) As a site user, I can view a dashboard with my post statuses to track my content's progress.
- [#17](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/17) As a site user, I can manage my profile to keep my information up to date.
- [#20](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/20) As a site user, I can draft posts before submission to refine my content.
- [#21](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/21) As a site user, I can search posts using a search bar to find relevant content easily.
- [#24](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/24) As a site user, I can submit a post for publication so that it can be reviewed by an admin before going live.

### As a Site Admin

- [#2](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/2) As a site admin, I can register and gain access to the admin panel to manage the platform.
- [#3](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/3) As a site admin, I can manage posts to ensure content is appropriate and up-to-date.
- [#13](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/13) As a site admin, I can perform CRUD operations in the admin interface to manage content effectively.
- [#14](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/14) As a site admin, I can delete likes and comments on user posts to maintain content quality.
- [#15](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/15) As a site admin, I can add likes and comments to user posts to manage user engagement.
- [#16](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/16) As a site admin, I can restrict regular users from accessing the admin interface to secure the platform.
- [#18](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/18) As a site admin, I can manage user profiles to ensure users comply with platform standards.
- [#19](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/19) As a site admin, I can view and manage user profiles to oversee user activity and content.
- [#25](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/25) As a site admin, I can review user-submitted posts so that I can approve or reject them based on content guidelines.
- [#26](https://github.com/suba-suresh/Leamington-Spa-Adventures/issues/26) As a site admin, I can approve a user’s post so that it becomes publicly visible on the platform.



### Database Planning

I used Lucidchart to create my database entity relationship diagrams. Below you can see how each model relates to eachother [Database Diagram](static/images/database_digram_for_blog_post.jpg)


## Agile Methodology for project planning

I used agile methodology for the first time when planning full-stack django website with a focus on delivering the basic functionalities. I prioritized features by labeling them as "must-have" or "could-have" and moved some less critical ones to future development. To guide my development process, I created user stories for both the admin user and regular visitors. These stories helped to define the features and functionalities that were most important to project's target audience.

As a solo developer who was learning a lot during development, I faced challenges in estimating the time required for each tasks, bugs and only had a basic concept of what I would create. Therefore, I kept things simple and focused on achievable goals. As the project grew, I was able to add more advanced features and group user stories are meant to mark significant points in time in terms of project completion.

To keep track of progress, I used a kanban board divided into following sections: "to do", "in progress" "done",  and "bugs" that allowed to visualize all tasks and prioritize next steps.[Click here](https://github.com/users/suba-suresh/projects/4/views/1)

By using agile methodology, I was able to stay organized and focused on delivering the most important features, while also allowing flexibility for future development

### Wireframes
Include wireframes if available.

Description of the wireframes and how they guided the design.


## Features Implemented

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

- **Login Page**:
  - Login functionality allows users to log in securely.
  - Successful login redirects users to the home page.

- **Registration Page**:
  - Signup functionality allows users to register securely.
  - Successful registration redirects users to the home page.

- **Logout Page**:
  - Logout functionality allows users to sign out securely.
  - After successful logout, users are redirected to the home page.

- **Profile Page**:
  - Access requires user authentication.
  - Users can edit their profile information (bio, title, and profile images).
  - Profile editing is done through a form toggled by an "Edit Profile" button.
  - Users can create blog posts, including uploading images.
  - After submitting a post, users are redirected to the dashboard page to view their post.
  - After admin approval, the post can be published to the blog list.

- **Blog**:
  - Displays a list of approved blog post details with likes, comments, author name, and creation date.
  - Displays a paginated list of posts with featured images, titles, excerpts, and details.
  - Posts can be browsed by tags.

- **Full Post View**:
  - Includes a featured image, author info, like and comment sections.
  - Users can interact with the post by liking or commenting if authenticated.

- **About Page**:
  - Contains introductory paragraphs about the team, their passion, and mission.
  - Includes a FAQ section using Bootstrap accordion.

- **Contact Page**:
  - Features a contact form and location info with Google Maps integration.

- **Admin Panel**:
  - Manages blog posts with details such as title, slug, author, category, tags, status, and creation date.
  - Allows bulk status updates and filtering.
  - Admins can approve or reject user-submitted posts.
  - Admins can manage user accounts and profiles.

- **User Dashboard**:
  - Provides statistics on the user's posts with CRUD functionality.
  - Allows users to update personal details such as username, bio, and profile images.
  - Displays the status of submitted posts (pending, approved, rejected).

- **Accounts Templates**:
  - Handles user dashboards and personal details for account management.
  - Handles admin dashboards and personal details, such as username, bio, and profile images.

- **Add/Edit Post - Form Validation**:
  - Validates post fields with JavaScript and displays alert messages.
  - Ensures required fields are filled out correctly before submission.

- **Messages**:
  - Utilizes Django messages with Bootstrap toast components for user feedback.
  - Displays success, error, and informational messages in response to user actions.

- **Responsive Design**:
  - Ensures all pages are fully responsive across various screen sizes, including mobile, tablet, and desktop.
  - Navbar collapses to a burger menu on smaller screens.
  - Content stacks vertically instead of horizontally on smaller screens.
  - Blog post cards adjust to display fewer cards on smaller screens.

## Future Features
- **Enhanced Search Functionality:** Implement a search bar to find specific content.
- **Draft Post:** Adding Draft Post, user can save and preview before submission for a better user experience.
- **User Profiles:** Add features for users to showcase their most popular content and achievements.
- **Interactive Maps:** Integrate maps to show locations of featured adventures.


## Technology Stack
- **HTML/CSS:** For page structure and styling.
- **JavaScript:** For interactive elements.
- **Python/Django:** Backend framework.
- **Bootstrap:** For responsive design.
- **Cloudinary:** For image hosting.
- **Heroku:** For deployment.
- **Git/GitHub:** For version control and collaboration.

### Software and Libraries
- [Animate On Scroll AOS](https://michalsnik.github.io/aos/)
- [Bootstrap 5](https://blog.getbootstrap.com/2022/11/22/bootstrap-5-2-3/)
- [Cloudinary](https://cloudinary.com/)
- [Django](https://www.djangoproject.com/)
- [Postgresql](https://www.postgresql.org/)
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
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/)


## Testing and Validation

### Responsiveness

I tested the website for responsiveness using Chrome's Developer Tools. Screenshots were captured to demonstrate how the design adapts across different devices, including mobile, tablet, and laptop. Below are some key features of the responsive design:

- **Navbar**: The navbar collapses into a burger menu on smaller screen sizes to ensure easy navigation.
- **Masthead Image**: The masthead image is hidden on smaller screen sizes to maintain a clean and focused layout.
- **Content Layout**: Content stacks vertically rather than horizontally on smaller screens to optimize readability and usability.
- **Blog Post Cards**: On smaller screens, fewer blog post cards are visible on the homepage to ensure a responsive and accessible design.

Screenshots demonstrating these features can be found in the [Screenshots](static/images/screenshots/) section of the documentation.

**Laptop**
![Screenshot of Home page view on laptop][Screenshots](static/images/screenshots/desktop-view.png)

**Tablet**
![Screenshot of Home page view on tablet][Screenshots](static/images/screenshots/tab-view.png)

**Mobile**
![Screenshot of Home page view on mobile][Screenshots](static/images/screenshots/mobile-view.png)

### Other Examples

**Laptop**
![Screenshot of about page view on laptop][Screenshots](static/images/screenshots/dashboard-desktop-view.png)

**Tablet**
![Screenshot of a blog view on tablet][Screenshots](static/images/screenshots/dashboard-tab-view.png)

**Mobile**
![Screenshot of the home page view on mobile][Screenshots](static/images/screenshots/dashboard-mobile-view.png)

### Validation
- I used the [W3 HTML Validator](https://validator.w3.org/) to check the HTML on each of my site pages by Direct Input. I have resolved the necessary errors.
  ![HTML validation results](/static/images/screenshots/html-validation.png)  
  
- I used the [W3 CSS Validator](https://jigsaw.w3.org/) to check my CSS script by Direct Input. I found no errors! There are 7 warnigns which are just flagging vendor extensions. ![CSS validation results](/static/images/screenshots/css-validation.png)  
  
- I used the [CI Python Linter](https://pep8ci.herokuapp.com/) to check all my python scripts. I found a few small errors like the below - mostly lines were too long or there was a missing blank space line. I have left some of the error messages as they are related to a too long line at the result of a comment. ![Python Linter Result](/static/images/screenshots/Python-validation.png)

## Known Bugs
- **Image Upload Issue:** Conflicts with image handling on the Profile page.
- ** Moderation:**  slow to update when delete the comments and likes.
- **Search Functionality:** Not yet implemented as planned.


## Deployment

#### Creating the Heroku App

- Begin by signing up or logging in to Heroku.
- In the Heroku Dashboard, click on 'New' and then select 'Create New App'.
- Choose a unique name for your project, like "Leamington Spa Adventures".
- Select the EU region.
- Click on "Create App".
- In the "Deploy" tab, choose GitHub as the deployment method.
- Connect your GitHub account and find/connect your GitHub repository.

#### Setting Up Environment Variables

- Create `env.py` in the top level of the Django app.
- Import `os` in `env.py`.
- Set up necessary environment variables in `env.py`, including the secret key and database URL.
- Update `settings.py` to use environment variables for secret key and database.
- Configure environment variables in the Heroku "Settings" tab under "Config Vars".
- Migrate the models to the new database connection in the terminal.
- Configure static files and templates directories in `settings.py`.
- Add Heroku to the `ALLOWED_HOSTS` list.

#### Creating Procfile and Pushing Changes

- Create a `Procfile` in the top level directory.
- Add the command to run the project in the `Procfile`.
- Add, commit, and push the changes to GitHub.

#### Heroku Deployment

- In Heroku, navigate to the Deployment tab and deploy the branch manually.
- Monitor the build logs for any errors.
- Upon successful deployment, Heroku will display a link to the live site.
- Make sure to resolve any deployment errors by adjusting the code as necessary.


## Resources
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [Heroku Documentation](https://devcenter.heroku.com/categories/reference)


## Credits and Acknowledgements

- **Code Institute** course content for providing the knowledge and guidance to build the project
- Course Facilitator **Alexander** for his unwaving support and guidance during the process and his endless patience and support with trouble shooting issues
- Tutor **Kevin** for his helpful SME sessions and constant support
- My fellow **cohort peers** for their support, help with trouble shooting issues and sharing the experience

##### [ Back to Top ](#table-of-contents)

