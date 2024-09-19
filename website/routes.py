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
    participants = [] 

    for participant in event.participants:
        participants.append(User.find_by_id(participant))
    
    if not event:
        flash("Event not found.", category='danger')
        redirect(url_for("events"))

    if request.method == 'POST':
        if event.add_participant(event.id, current_user.id):
            flash("Successfully joined the event!", category="success")
        else:
            flash("You are already participating in this event.", category="info")
              
    return render_template('event_detail.html', user=current_user, event=event, participants=participants)
