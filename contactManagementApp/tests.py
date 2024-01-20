from django.test import TestCase

from .models import User, Contact
from .service import register, login, addContact, viewAContact, viewAllContactBelongingTo, deleteAContact


# Create your tests here.
class ContactManagementTest(TestCase):
    def test_userRegister(self):
        testeduser = register("Delighted", "Adewuyi", "08073203442", "Adewuyi#11", "deborahdelighted@gmail.com")
        self.assertEqual(1, testeduser)

    def test_user_can_login(self):
        testeduser = register("Delighted", "Adewuyi", "08073203442", "Adewuyi#11", "deborahdelighted@gmail.com")
        login("deborahdelighted@gmail.com", "Adewuyi#11")
        self.assertTrue(User.objects.get(email="deborahdelighted@gmail.com").is_Locked)

    def test_that_user_can_add_contact(self):
        testeduser = register("Delighted", "Adewuyi", "08073203442", "Adewuyi#11", "deborahdelighted@gmail.com")
        login("deborahdelighted@gmail.com", "Adewuyi#11")
        self.assertEqual(1, testeduser)
        contact: Contact = addContact("debby", "Jesutofumi", "09065626032", "debbyJesutofumi@gmail.com", "Yaba",
                                      "deborahdelighted@gmail.com", testeduser)
        self.assertEqual(1, contact.pk)

    def test_that_user_can_add_two_contact(self):
        testeduser = register("Delighted", "Adewuyi", "08073203442", "Adewuyi#11", "deborahdelighted@gmail.com")
        login("deborahdelighted@gmail.com", "Adewuyi#11")
        self.assertEqual(1, testeduser)
        contact1: Contact = addContact("debby", "Jesutofumi", "09065626032", "debbyJesutofumi@gmail.com", "Yaba",
                                       "deborahdelighted@gmail.com", testeduser)
        contact2: Contact = addContact("ola", "Jesoph", "070234523", "olaJosoph@gmail.com", "sango",
                                       "deborahdelighted@gmail.com", testeduser)
        self.assertEqual(1, contact1.pk)
        self.assertEqual(2, contact2.pk)

    def test_user_can_viewAContact(self):
        testeduser = register("Delighted", "Adewuyi", "08073203442", "Adewuyi#11", "deborahdelighted@gmail.com")
        login("deborahdelighted@gmail.com", "Adewuyi#11")
        self.assertEqual(1, testeduser)
        addContact("debby", "Jesutofumi", "09065626032", "debbyJesutofumi@gmail.com", "Yaba","deborahdelighted@gmail.com", testeduser)
        addContact("ola", "Jesoph", "070234523", "olaJosoph@gmail.com", "sango","deborahdelighted@gmail.com", testeduser)
        found_contact:Contact = viewAContact("deborahdelighted@gmail.com", "09065626032")
        self.assertEqual("debby", found_contact.firstname)
        self.assertEqual("Jesutofumi", found_contact.surname)

    def test_user_can_viewAllContact(self):
        testeduser = register("Delighted", "Adewuyi", "08073203442", "Adewuyi#11", "deborahdelighted@gmail.com")
        login("deborahdelighted@gmail.com", "Adewuyi#11")
        self.assertEqual(1, testeduser)
        addContact("debby", "Jesutofumi", "09065626032", "debbyJesutofumi@gmail.com", "Yaba","deborahdelighted@gmail.com", testeduser)
        addContact("ola", "Jesoph", "070234523", "olaJosoph@gmail.com", "sango","deborahdelighted@gmail.com", testeduser)
        self.assertEqual(2, len(viewAllContactBelongingTo("deborahdelighted@gmail.com")))

    def test_deleteAContact(self):
        registerUser = register("Blessing","Glory","080345617","Glory@123","blessingGlory@123")
        login("blessingGlory@123","Glory@123")
        addContact("Love","Chief","0702344562","loveChief@gmail.com","Lagos","love@123",registerUser)
        addContact("Peace","June","09045639765","loveChief@gmail.com","Lagos","peace@123",registerUser)
        deleteAContact("Glory@123","0702344562")
        self.assertEqual(1,len(viewAllContactBelongingTo("Glory@123")))