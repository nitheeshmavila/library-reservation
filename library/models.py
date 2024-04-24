from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(null=True, blank=True)
    no_of_copies = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.book_id

class Member(models.Model):
    member_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(null=True, blank=True)


class Circulation:

    @classmethod
    def checkout(cls, book_id, member_id):
        book = Book.objects.filter(book_id=book_id)
        if not book:
            return {
                "status": "BOOK_NOT_FOUND",
                "message": "Book not found"
            }
        book = book[0]
        no_of_copies = book.no_of_copies
        # check if there are any existing reservations for this book
        reservations = Reservation.objects.filter(book_id=book_id, status__in=["OPEN", "AVAILABLE"])
        if no_of_copies > len(reservations):      
            # Book is available
            book.no_of_copies = no_of_copies - 1
            book.save()
            return {
                "status": "BOOK_GRANTED",
                "message": "Book granted"
            }
        else:
            # reserve the book
            reservation_id = Reservation.create(book_id, member_id)
            return {
                "status": "BOOK_RESERVED",
                "reservation_id": reservation_id,
                "message": "Book reserverd"
            }

    @classmethod
    def return_book(cls, book_id, member_id):
        book = Book.objects.filter(book_id=book_id)
        if not book:
            return {
                "status": "BOOK_NOT_FOUND",
                "message": "Trying to return a wrong book"
            }
        book = book[0]polls
            book.save()

            # check if there are any reservations for this book
            reservations = Reservation.objects.filter(book_id=book_id, status="OPEN", order_by="date_time")
            
            if reservations:
                reservation = reservation[0]
                reservations.status = 'AVAILABLE'
                reservations.save()


            return {
                "status": "BOOK_RETURED",
                "message": "Book returned successfully"
            }
        return {
            "status": False,
            "message": "Tring to return a wrong book" 
        }

    @classmethod
    def fulfill(cls, book_id, member_id):
        # Check the reservation fot that user is fulfilled
        reservations = Reservation.objects.filter(book_id=book_id, member_id=member_id, status="AVAILABLE")
        if reservations:
            reservation = reservations[0]
            book = reservation.book
            no_of_copies = book.no_of_copies
            book.no_of_copies = no_of_copies - 1
            book.save()
            reservation.status = "CLOSED"
            reservation.save()
            return {
                "status": "BOOK_GRANTED",
            }
        return {
            "status": "NO_RESERVATION_FOUND/ NOT FULFILLED"
        }
        
class Reservation(models.Model):
    book = models.ForeignKey("Book", null=True, blank=True)
    status = models.CharField(max_length="10", null=True, blank=True)
    member = models.ForeignKey("Member", null=True, blank=True)
    resevervation_token = models.CharField(max_length="255", null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def create(cls, book_id, member_id):
        reservation = cls(book_id=book_id, member_id=member_id, status="OPEN")
        reservation.save()
        reservation_id = reservation.get_id()
        return reservation_id

    def get_id(self):
        return self.id + self.book.name 



            



