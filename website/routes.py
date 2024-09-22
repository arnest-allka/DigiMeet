from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user

from .models.event import Event
from .models.user import User

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def home():
    return render_template("home.html", user=current_user)

@routes.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    if request.method == "POST":
        name = request.form.get('event_name')
        description = request.form.get('description')
        date = request.form.get('date')
        time = request.form.get('time')
        place = request.form.get('place')
        type = request.form.get('type')
        user_id = current_user.id

        now = str(datetime.now())
        
        if not name or not description or not date or not time or not place or not type:
            flash("All fields are required to created en event.", category='danger')  
        elif Event.find_by_name(name):
            flash("This event name is taken. Choose a different one.", category='danger')
        elif date < now:
            flash("Choose a valid date for the event.", category='danger')
        else:
            Event.create_event(name, description, date, time, place, type, user_id)
            flash('Event created successfully!', category='success')
            return redirect(url_for('routes.home'))
    return render_template("create_event.html", user=current_user)

@routes.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    created_events = Event.find_by_user_id(current_user.id)
    participating_events = Event.find_by_participant(current_user.id)
    return render_template('profile.html', user=current_user, created_events=created_events, participating_events=participating_events)

@routes.route('/events', methods=['GET', 'POST'])
def events():
    events = Event.get_events()
    return render_template('events.html', user=current_user, events=events)

@routes.route('/event-detail', methods=['GET', 'POST'])
@login_required
def event_detail():
    event_id = request.args.get('event_id')
    event = Event.find_by_id(event_id)

    if not event:
        flash("Event not found.", category="danger")
        return redirect(url_for('events'))
    
    if request.method == 'POST':
        participation_status = request.form.get('participation')

        if participation_status == "definitely":
            flash(f"{current_user.first_name} has confirmed attendance.", category="success")
        elif participation_status == "maybe":
            flash(f"{current_user.first_name} is not sure but may attend.", category="success")
        elif participation_status == "not":
            flash(f"{current_user.first_name} is not going to the event.", category="success")
        else:
            flash("Invalid participation status.", category="warning")
            return redirect(url_for('routes.event_detail', event_id=event_id))
        
        if Event.add_participant(event.id, current_user, participation_status):
            if participation_status != "not":
                flash("Successfully joined the event!", category="success")
            event = Event.find_by_id(event.id)
        else:
            flash("You are already participating in this event. No changes were made.", category="info")
    
    return render_template('event_detail.html', user=current_user, event=event)

@routes.route('/delete-event', methods=['GET', 'POST'])
@login_required
def delete_event():
    event_id = request.args.get('event_id')
    if Event.delete_event(event_id):
        flash("Event deleted successfully.", category='success')
    else:
        flash("Could not delete event.", category='danger')
    if current_user.is_admin:
        return redirect(url_for('routes.events'))
    return redirect(url_for('routes.profile'))

@routes.route('/update-event', methods=['GET', 'POST'])
@login_required
def update_event():
    event_id = request.args.get('event_id')
    event = Event.find_by_id(event_id)

    if request.method == 'POST':
        name = request.form.get('event_name')
        description = request.form.get('description')
        date = request.form.get('date')
        time = request.form.get('time')
        place = request.form.get('place')
        type = request.form.get('type')
        
        now = str(datetime.now())
        
        updates = {}
        if name:
            if not Event.find_by_name(name):
                updates['name'] = name
            else:
                flash("This name is already taken", category='danger')
                return redirect(url_for("routes.update_event", user=current_user, event_id=event.id))
        if description:
            updates['description'] = description
        if date:
            if date < now:
                flash("Please choose a valid date for the event.", category='danger')
                return redirect(url_for("routes.update_event", user=current_user, event_id=event.id))
            else:
                updates['date'] = date
        if time:
            updates['time'] = time
        if place:
            updates['place'] = place
        if type:
            updates['type'] = type

        if updates:
            event.update_event(event_id, updates)
            flash("Event updated successfully!", category="success")
            if current_user.is_admin:
                return redirect(url_for('routes.events'))    
            return redirect(url_for('routes.profile'))
        else:
            flash("No changes were made.", category="info")

    return render_template('update_event.html', user=current_user, event=event)

@routes.route('/search-events', methods=['GET'])
def search_events():
    title = request.args.get('title', '')
    place = request.args.get('place', '')
    type = request.args.get('type', '')

    events = Event.search_events(title, place, type)
    print(events)

    return render_template('home.html', user=current_user, events=events)

@routes.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    user = User.get_users()
    return render_template('users.html', user=current_user, users=user)

@routes.route('/update-user', methods=['GET', 'POST'])
@login_required
def update_user():
    user_id = request.args.get('user_id')
    user = User.find_by_id(user_id)
    
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        username = request.form.get('username')
        password = request.form.get('password')
        
        updates = {}

        if username:
            if User.find_by_username(username):
                flash('Username already exists. Choose a different one.', category='danger')
                return redirect(url_for('routes.update_user', user=current_user, user_id=user.id))
            elif len(username) < 2:
                flash('Username must be greater than 1 character.', category='danger')
                return redirect(url_for('routes.update_user', user=current_user, user_id=user.id))
            else:
                updates['username'] = username
        if email:
            if User.find_by_email(email):
                flash('Email already exists. Choose a different one.', category='danger')
                return redirect(url_for('routes.update_user', user=current_user, user_id=user.id))
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='danger')
                return redirect(url_for('routes.update_user', user=current_user, user_id=user.id))
            else:
                updates['email']=email
        if first_name:
            if len(first_name) < 2:
                flash('First name must be greater than 1 character.', category='danger')
                return redirect(url_for('routes.update_user', user=current_user, user_id=user.id))
            else:
                updates['first_name']=first_name
        if last_name:
            if len(last_name) < 2:
                flash('Last name must be greater than 1 character.', category='danger')
                return redirect(url_for('routes.update_user', user=current_user, user_id=user.id))
            else:
                updates['last_name']=last_name
        if password:                
            if len(password) < 7:
                flash('Password must be at least 7 characters.', category='danger')
                return redirect(url_for('routes.update_user', user=current_user, user_id=user.id))
            else:
                updates['password']=password
        
        if updates:
            user.update_user(user_id, updates)
            flash("User updated successfully!", category="success")
            return redirect(url_for('routes.users'))    
        else:
            flash("No changes were made.", category="info")

    return render_template("update_user.html", user=current_user, updating_user=user)


@routes.route('/delete-user', methods=['GET', 'POST'])
@login_required
def delete_user():
    if not current_user.is_admin:
        redirect(url_for("routes.home"))
    
    user_id = request.args.get('user_id')
    user = User.find_by_id(user_id)
    
    if user:
        Event.remove_participant_from_events(user_id)

        Event.delete_events_by_owner(user_id)
        
        User.delete_user(user_id)
        flash("User deleted successfully.", category='success')
    else:
        flash("Could not delete user.", category='danger')
    return redirect(url_for('routes.users'))