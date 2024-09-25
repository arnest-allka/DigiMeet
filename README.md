# DigiMeet - Event Management System

## Περιεχόμενα

1. [Επιπλέων Παραδοχές και Παρεκκλίσεις από την Εκφώνηση](#επιπλέων-παραδοχές-και-παρεκκλίσεις-από-την-εκφώνηση)
2. [Τεχνολογίες που Χρησιμοποιήθηκαν](#τεχνολογίες-που-χρησιμοποιήθηκαν)
3. [Περιγραφή Αρχείων](#περιγραφή-αρχείων)
4. [Τρόπος Εκτέλεσης Συστήματος](#τρόπος-εκτέλεσης-συστήματος)
5. [Τρόπος Χρήσης Συστήματος](#τρόπος-χρήσης-συστήματος)
6. [Αναφορές](#αναφορές)

---

## Επιπλέων Παραδοχές και Παρεκκλίσεις από την Εκφώνηση

- Κάθε χρήστης πρέπει να έχει μοναδικό username και email.
- Κάθε χρήστης μπορεί να δημιουργήσει εκδηλώσεις και να συμμετάσχει σε όλες τις εκδηλώσεις.
- Κάθε χρήστης μπορεί να διαγράψει και να ενημερώσει τις δικές του εκδηλώσεις.
- Αν ο χρήστης αλλάξει γνώμη μπορεί να αλλάξει την συμμετοχή του στην εκδηλωση.
- Κάθε εκδήλωση μπορεί να έχει διαφορετικό τύπο συμμετοχής (σίγουρη συμμετοχή, ενδεχόμενη συμμετοχή).
- Ο διαχειριστής έχει πλήρη δικαιώματα διαχείρισης των εκδηλώσεων και χρηστών.
- Όταν ο διαχειριστής διαγράφει έναν χρήστη, διαγράφονται και οι εκφηλώσεις που είχε δημιουργήσει.

## Τεχνολογίες που Χρησιμοποιήθηκαν

- **Python**: Backend
- **Flask**: Web framework για την υλοποίηση του API Server
- **Flask-Login**: Authentication και διαχείριση χρήστη
- **PyMongo**: Αλληλεπίδραση με MongoDB
- **MongoDB**: Βάση δεδομένων για την αποθήκευση χρηστών και εκδηλώσεων
- **Bootstrap**: Frontend CSS για responsive design
- **Docker**: Για την δημιουργία container του συστήματος

## Περιγραφή Αρχείων

- **/website/**: Περιέχει τον κώδικα της εφαρμογής με τα blueprints.
  - **/models/**: Περιέχει τα μοντέλα `User` και `Event` που διαχειρίζονται την αλληλεπίδραση με τη βάση δεδομένων.
  - **/templates/**: Περιέχει τα HTML templates για το frontend.
  - **\_\_init\_\_.py**: Ρυθμίσεις της εφαρμογής και αρχικοποίηση των extensions.
  - **routes.py**: Περιέχει τα routes της εφαρμογής για τους χρήστες και εκδηλώσεις.
  - **auth.py**: Περιέχει τα routes που σχετίζονται με την αυθεντικοποίηση.
- **Dockerfile**: Περιγράφει το image που χρησιμοποιείται για το Flask app.
- **docker-compose.yml**: Ρυθμίζει την εκτέλεση του συστήματος μέσω Docker με MongoDB και Flask.
- **requirements.txt**: Αρχείο που περιέχει ολα τις απαραίτητες βιβλιοθήκες που χρειάζεται η εφαρμογή.
- **config.py**: Αρχείο ρυθμίσεων με τις παραμέτρους της εφαρμογής.
- **main.py**: Το κεντρικό αρχείο για την εκτέλεση του Flask app.

## Τρόπος Εκτέλεσης Συστήματος

1. Κλώνο το repository:

   ```bash
   git clone https://github.com/arnest-allka/YpoxreotikiErgasiaSept24_e21004_Allka_Arnest.git
   cd YpoxreotikiErgasiaSept24_e21004_Allka_Arnest
   ```

2. Εκτέλεση του συστήματος με Docker:

   ```bash
   docker-compose up -d
   ```

3. Η εφαρμογή θα εκκινήσει στο http://localhost:5000.

## Τρόπος Χρήσης Συστήματος

1. Εμφάνιση ολων των Εκδηλώσεων

   Η επιλογή "Events" στο μενού εμφανίζει όλες τις διαθέσιμες εκδηλώσεις που ύπαρχουν στο σύστημα.

   Αυτές εμφανίζονται σε όλους τους χρήστες που χρησιμοποιούν την ιστοσελίδα, ανεξαρτήτως αν είναι συνδεδεμένοι ή οχι.

   Σε κάθε εκδήλωση υπάρχει ενα κουμπί "View Details", όπου εμφανίζονται οι πληροφορίες της εκδήλωσης.
   Σε αυτό έχουν δυνατότητα μονο συνδεδεμένοι χρήστες.

2. Αναζήτηση Εκδηλώσεων

   Στην αρχική σελιδά εμφανίζεται μια φόρμα απο τρία πεδία όπου ο χρήστης μπορεί να αναζητήσει εκδηλώσεις με βάση το όνομα, την τοποθεσία και τον τύπο της εκδήλωσης το οποιο τον ενδιαφέρει.

   Στην συνέχεια εμφανίζονται οι εκδηλώσεις που βρέθηκαν, αλλιώς εμφανίζεται μήνυμα "No events found."

   Σε κάθε εκδήλωση υπάρχει ενα κουμπί "View Details", όπου εμφανίζονται οι πληροφορίες της εκδήλωσης.
   Σε αυτό έχουν δυνατότητα μονο συνδεδεμένοι χρήστες.

### Χρήστης

Ο χρήστης έχει τη δυνατότητα να εκτελέσει βασικές λειτουργίες όπως η εγγραφή ή σύνδεση, η δημιουργία εκδηλώσεων, η συμμετοχή σε εκδηλώσεις και προβολή και επεξεργασία των εκδηλώσεων που του ανήκουν.

1.  Εγγραφή Χρήστη

    Για την εγγραφή του χρήστη στο σύστημα:

    Ο χρήστης εισάγει τα εξής στοιχεία: Όνομα, Επώνυμο, Email, Username και Κωδικό πρόσβασης.
    Μετά την εγγραφή, ο χρήστης μπορεί να συνδεθεί στο σύστημα.

    Παράδειγμα εκτέλεσης:

    Ο χρήστης επιλέγει την επιλογή "Sign up" από τo Μενού.

    Συμπληρώνει τη φόρμα:

    ```bash
    Όνομα: Arnest
    Επώνυμο: Allka
    Email: arisallkas@gmail.com
    Username: aris
    Κωδικός: ds-e21004
    Επαλήθευση Κωδικού: ds-e21004
    ```

    Πατάει "Submit" και το σύστημα εμφανίζει μήνυμα επιτυχίας: "Registration successful. You can now log in.".
    Το σύστημα τον ανεκατευθυνει στην σελίδα συνδεσης.

2.  Σύνδεση Χρήστη

    Μετά την εγγραφή, ο χρήστης μπορεί να συνδεθεί στο σύστημα με το username και password του.

    Παράδειγμα εκτέλεσης:

    Ο χρήστης επιλέγει την επιλογή "Login" και συμπληρώνει τη φόρμα με το username και τον κωδικό του.

    Συμπληρώνει τη φόρμα:

    ```bash
    Username: aris
    Κωδικός: ds-e21004
    ```

    Πατάει "Submit" και το σύστημα εμφανίζει μήνυμα επιτυχίας: "Logged in successfully!".
    Το σύστημα τον ανεκατευθυνει στην αρχική σελίδα.

3.  Δημιουργία Εκδήλωσης

    Αφού συνδεθεί, ο χρήστης μπορεί να δημιουργήσει εκδήλωση στο σύστημα.

    Παράδειγμα εκτέλεσης:

    Επιλέγει "Create Event".

    Συμπληρώνει τα στοιχεία της εκδήλωσης:

    ```bash
    Event Name: Tech Meetup
    Description: Συζήτηση για τις νέες τεχνολογίες
    Date: 2024-10-10
    Time: 18:00
    Place: Αθήνα
    Type: Συνάντηση
    ```

    Πατάει "Submit" και η εκδήλωση προστίθεται στη λίστα εκδηλώσεων.

4.  Συμμετοχή σε Εκδήλωση

    Ο χρήστης μπορεί να επιλέξει συμμετοχή σε οποιαδήποτε εκδήλωση είναι διαθέσιμη.

    Παράδειγμα εκτέλεσης:

    Ο χρήστης επιλέγει μια εκδήλωση από τη λίστα και πατάει "View Details".

    Επιλέγει "Definately Attending" ή "Maybe Attending" από το αναδυόμενο παράθυρο.
    Μπορεί να επιλέξει και την επιλογή "Not going" σε περίπτωση που το μετανιώσει.

    Το σύστημα εμφανίζει μήνυμα επιτυχίας και τη επιλογη που απάντησε:"Arnest has confirmed attendance." "Successfully joined the event!"

    Ο χρήστης μπορεί επίσης να ενημερώσει την συμμετοχή του ακολουθώντας την ιδια διαδικασία με πάνω.

5.  Προβολή Προφίλ

    Ο χρήστης μπορεί να δεί το προφίλ του επιλέγοντας την επιλογή "Profile" στο μενού.
    Το προφίλ του κάθε χρήστη εμφανίζει τις πληροφορίες του χρήστη, απο κάτω στα αριστερά εμφανίζει τις εκδηλώσεις που ο ιδιος έχει δημιουργήσει και δεξία τις εκδηλώσεις όπου εχει δηλώσει συμμετοχή.

    Στις Εκδηλώσεις που έχει δημιουργήσει, σε κάθε εκδήλωση έχει την δυνατότητα να το ανοίξει με το κουμπί "View Details", να το επεξεργαστεί με το κουμπί "Update" και να το διαγράψει με το κουμπί "Delete".

    Στις Εκδηλώσεις που συμμετέχει, με το κουμπί "View Details" μπορεί να ενημερώσει την συμμετοχή του στην εκδήλωση σε περίπτωση που αλλάξει γνώμη.

### Διαχειριστής

Ο διαχειριστής έχει επιπλέον δικαιώματα και μπορεί να διαχειρίζεται τους χρήστες και τις εκδηλώσεις στο σύστημα.

Οι βασικές λειτουργίες που μπορεί να εκτελέσει περιλαμβάνουν τη διαγραφή και τροποποίηση χρηστών και εκδηλώσεων.

1. Διαχείριση Χρηστών

   Ο διαχειριστής μπορεί να προβάλει τη λίστα των χρηστών και να διαγράψει χρήστες από το σύστημα.

   Παράδειγμα εκτέλεσης:

   Ο διαχειριστής συνδέεται στο σύστημα μέσω της φόρμας σύνδεσης με username: admin και password: admin321.

   Επιλέγει την επιλογή "Users" από το κύριο μενού διαχείρισης.

   Εμφανίζεται μια λίστα με όλους τους χρήστες του συστήματος, συμπεριλαμβανομένων του ονόματος, του email και του username τους.

   Ο διαχειριστής μπορεί να επιλέξει "Update" για να επεξεργαστεί κάποιον χρήστη και χρήστης ενημερώνεται επιτυχώς από το σύστημα.

   Ο διαχειριστής μπορεί να επιλέξει "Delete" για να διαγράψει κάποιον χρήστη.
   O χρήστης διαγράφεται επιτυχώς από το σύστημα και όλες οι εκδηλώσεις που έχει δημιουργήσει διαγράφονται επίσης.

2. Διαχείριση Εκδηλώσεων

   Ο διαχειριστής έχει τη δυνατότητα να διαγράψει ή να τροποποιήσει οποιαδήποτε εκδήλωση στο σύστημα, ακόμα και αυτές που έχουν δημιουργήσει άλλοι χρήστες.

   Παράδειγμα εκτέλεσης:

   Ο διαχειριστής επιλέγει "Events" από το κύριο μενού.

   Εμφανίζεται μια λίστα με όλες τις εκδηλώσεις που έχουν δημιουργηθεί στο σύστημα.

   Ο διαχειριστής μπορεί να επιλέξει "View Details" για να δει τις πληροφορίες της εκδήλωσης, όμως δεν μπορεί να συμμετάσχει όπως έναν συνδεδεμένο χρήστη.

   Ο διαχειριστής μπορεί να επιλέξει "Update" για να τροποποιήσει τα στοιχεία μιας εκδήλωσης ή "Delete" για να τη διαγράψει.
