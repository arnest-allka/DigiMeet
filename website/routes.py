from datetime import datetime
from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user

from .models.event import Event
from .models.user import User

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
@login_required
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
@login_required
def events():
    events = Event.get_events()
    return render_template('events.html', user=current_user, events=events)

@routes.route('/event-detail', methods=['GET', 'POST'])
@login_required
def event_detail():
    event_id = request.args.get('event_id')
    event = Event.find_by_id(event_id)
    
    if request.method == 'POST':
        if Event.add_participant(event.id, current_user.id):
            flash("Successfully joined the event!", category="success")
            event = Event.find_by_id(event.id)
        else:
            flash("You are already participating in this event.", category="info")

    participants = [] 

    for participant in event.participants:
        participants.append(User.find_by_id(participant))

    return render_template('event_detail.html', user=current_user, event=event, participants=participants)

@routes.route('/delete-event', methods=['GET', 'POST'])
@login_required
def delete_event():
    event_id = request.args.get('event_id')
    if Event.delete_event(event_id):
        flash("Event deleted successfully.", category='success')
    else:
        flash("Could not delete event.", category='danger')
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
            flash("Event updated successfully!", "success")
            return redirect(url_for('routes.profile'))
        else:
            flash("No changes were made.", "info")

    
    return render_template('update_event.html', user=current_user, event=event)
    