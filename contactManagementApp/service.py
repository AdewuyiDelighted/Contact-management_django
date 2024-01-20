from .exception import InvalidLoginDetail
from .models import User, Contact


def register(first_name, last_name, phone_number, password, email):
    user = User(firstname=first_name, surname=last_name, phone_number=phone_number, password=password, email=email)
    user.save()
    return user.pk


def login(email, password):
    user: User = findUserByEmail(email)
    validate(password, user.password)
    user.is_Locked = True
    user.save()


def findUserByEmail(email):
    list_user = User.objects.all()
    for user in list_user:
        if user.email == email:
            return user


def validate(newPassword: str, userPassword):
    if newPassword != userPassword:
        raise InvalidLoginDetail('invalid')


def addContact(firstname, surname, phone_number, email, address, userEmail, userId):
    user: User = findUserByEmail(userEmail)
    contact = Contact(firstname=firstname, surname=surname, phone_number=phone_number, email=email, address=address,
                      userEmail=userEmail, userId=user)
    contact.save()
    return contact


def viewAContact(userEmail, phonenumber):
    user: User = findUserByEmail(userEmail)
    list_contact = Contact.objects.all()
    for contact in list_contact:
        if contact.phone_number == phonenumber:
            return contact


def viewAllContactBelongingTo(userEmail):
    contact_list = []
    user: User = findUserByEmail(userEmail)
    list_contact = Contact.objects.all()
    for contact in list_contact:
        if contact.userId == user:
            contact_list.append(contact)
    return contact_list


def deleteAContact(userEmail, phonenumber):
    contact: Contact = viewAContact(userEmail, phonenumber).objects.get()
    contact.delete()

