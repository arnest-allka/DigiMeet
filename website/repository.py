from pymongo import MongoClient

"""
Δημιουργούμε ένα μοναδικό αντικείμενο για αυτή τη κλάσση. Ο τρόπος που το δημιουργούμε είναι βασισμένος σε ένα pattern που ονομάζεται Singlenton Pattern.
Το πολύ γνωστή βιβλίο Design Patterns: Elements of Reusable Object-Oriented Software (1994) που έχει γραφτεί από τους συγγραφείς  Erich Gamma, Richard Helm, Ralph Johnson, και John Vlissides (γνωστούς και ως Gang of Four) είναι το πρώτο βιβλίο που χρησιμοποιεί design patterns για σχεδιασμό λογισμικού.
"""
class Repository:
    _instance = None  # Repository object


    @classmethod
    def instance(cls):
        """
        Κάθε φορά που θέλουμε να χρησιμοποιήσουμε ένα αντικείμενο τύπου Repository δεν θα φτιάχνουμε καινούργιο, αλλά θα χρησιμοποιείται αυτό που έχει ήδη δημιουργηθεί την πρώτη φορά. Για τον λόγο αυτό θα καλούμε τη συνάρτηση instance() της κλάσης.
        """
        if cls._instance is None:
            cls._instance = cls.__new__(cls)  # Create the object
            client = MongoClient("localhost", 27017)
            cls._instance.db = client["events"]  # Set the db attribute
            cls._instance.users = cls._instance.db["users"]
        return cls._instance


    def __init__(self) -> None:
        """
        Αυτή η υλοποίηση δεν επιτρέπει στον προγραμματιστή να δημιουργήσει νέο αντικείμενο από τον constructor της python.  
        """
        raise RuntimeError('Call instance() instead')

        

