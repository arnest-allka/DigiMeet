
# DigiMeet - Event Management System

## Contents

1. [Additional Assumptions and Deviations from the Statement](#additional-assumptions-and-deviations-from-the-statement)
2. [Technologies Used](#technologies-used)
3. [File Description](#file-description)
4. [System Execution Method](#system-execution-method)
5. [System Usage Guide](#system-usage-guide)
6. [References](#references)

---

## Additional Assumptions and Deviations from the Statement

- Each user must have a unique username and email.
- Each user can create events and participate in all events.
- Each user can delete and update their own events.
- If a user changes their mind, they can change their participation status in the event.
- Each event can have a different participation type (definite attendance, potential attendance).
- The administrator has full management rights over events and users.
- When the administrator deletes a user, the events they created are also deleted.

## Technologies Used

- **Python**: Backend
- **Flask**: Web framework for implementing the API Server
- **Flask-Login**: Authentication and user management
- **PyMongo**: Interaction with MongoDB
- **MongoDB**: Database for storing users and events
- **Bootstrap**: Frontend CSS for responsive design
- **Docker**: Used for creating a container for the system

## File Description

- **/website/**: Contains the application code with the blueprints.
  - **/models/**: Contains the `User` and `Event` models that manage interaction with the database.
  - **/templates/**: Contains the HTML templates for the frontend.
  - **\_\_init\_\_.py**: Application settings and extension initialization.
  - **routes.py**: Contains the application routes for users and events.
  - **auth.py**: Contains the routes related to authentication.
- **Dockerfile**: Describes the image used for the Flask app.
- **docker-compose.yml**: Configures the execution of the system via Docker with MongoDB and Flask.
- **requirements.txt**: File containing all the necessary libraries needed by the application.
- **config.py**: Configuration file with application parameters.
- **main.py**: Main file for running the Flask app.

## System Execution Method

1. Clone the repository:

   ```bash
   git clone https://github.com/arnest-allka/YpoxreotikiErgasiaSept24_e21004_Allka_Arnest.git
   cd YpoxreotikiErgasiaSept24_e21004_Allka_Arnest
   ```

2. Run the system with Docker:

   ```bash
   docker-compose up -d
   ```

3. The application will start at http://localhost:5000.

## System Usage Guide

1. Display All Events

   The "Events" option in the menu displays all available events in the system.

   These are visible to all users of the website, whether they are logged in or not.

   Each event has a "View Details" button, where event information is displayed.
   This is accessible only to logged-in users.

2. Search Events

   A search form with three fields is available on the homepage, allowing users to search for events based on name, location, and type.

   The events found will be displayed, otherwise a "No events found" message appears.

   Each event has a "View Details" button, where event information is displayed.
   This is accessible only to logged-in users.

### User

The user can perform basic functions such as registering or logging in, creating events, participating in events, and viewing and editing their own events.

1.  User Registration

    To register a user in the system:

    The user enters the following information: First Name, Last Name, Email, Username, and Password.
    After registration, the user can log in to the system.

    Example execution:

    The user selects the "Sign up" option from the Menu.

    Fills out the form:

    ```bash
    First Name: Arnest
    Last Name: Allka
    Email: arisallkas@gmail.com
    Username: aris
    Password: ds-e21004
    Confirm Password: ds-e21004
    ```

    Clicks "Submit" and the system displays a success message: "Registration successful. You can now log in.".
    The system redirects them to the login page.

2.  User Login

    After registration, the user can log in to the system using their username and password.

    Example execution:

    The user selects the "Login" option and fills out the form with their username and password.

    Fills out the form:

    ```bash
    Username: aris
    Password: ds-e21004
    ```

    Clicks "Submit" and the system displays a success message: "Logged in successfully!".
    The system redirects them to the homepage.

3.  Create Event

    After logging in, the user can create an event in the system.

    Example execution:

    Selects "Create Event".

    Fills out the event details:

    ```bash
    Event Name: Tech Meetup
    Description: Discussion on new technologies
    Date: 2024-10-10
    Time: 18:00
    Place: Athens
    Type: Meeting
    ```

    Clicks "Submit" and the event is added to the list of events.

4.  Join Event

    The user can choose to participate in any available event.

    Example execution:

    The user selects an event from the list and clicks "View Details".

    Chooses "Definitely Attending" or "Maybe Attending" from the popup.
    They can also select "Not going" if they change their mind.

    The system displays a success message with the choice they made: "Arnest has confirmed attendance." "Successfully joined the event!"

    The user can also update their attendance following the same procedure as above.

5.  View Profile

    The user can view their profile by selecting "Profile" from the menu.
    The profile displays user information, with the events they created on the left and events they are attending on the right.

    For events they created, they have the option to open with "View Details", edit with "Update", or delete with "Delete".

    For events they are attending, they can update their attendance status by selecting "View Details".

### Administrator

The administrator has additional rights and can manage users and events in the system.

The main functions they can perform include deleting and modifying users and events.

1. User Management

   The administrator can view the list of users and delete users from the system.

   Example execution:

   The administrator logs in with username: admin and password: admin321.

   Selects "Users" from the main management menu.

   A list of all users in the system is displayed, including their names, email addresses, and usernames.

   The administrator can choose "Update" to edit a user, and the user is successfully updated in the system.

   The administrator can select "Delete" to remove a user.
   The user is successfully deleted, along with all the events they created.

2. Event Management

   The administrator can delete or modify any event in the system, even those created by other users.

   Example execution:

   The administrator selects "Events" from the main menu.

   A list of all events created in the system is displayed.

   The administrator can select "View Details" to see the event information but cannot participate like a regular user.

   The administrator can choose "Update" to edit an event's details or "Delete" to remove it.

## References

- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/) - Used for implementing the web framework.

- [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/) - Used for session management and user authentication.

- [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/) - Used for connecting to and interacting with the MongoDB database.

- [MongoDB Documentation](https://www.mongodb.com/docs/) - Reference for creating and managing the MongoDB database.

- [Docker Documentation](https://docs.docker.com/) - Used for configuring the system's containers.

- [Bootstrap Documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/) - Used for the frontend's responsive design.
