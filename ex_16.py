"""
Завершуємо функціональність класу Contacts.
На цьому етапі ми додамо до класу метод remove_contacts.
Метод винен видаляти контакт по унікальному id у списку contacts.
Якщо словника із зазначеним id у списку contacts не знайдено, метод жодних дій над списком contacts не робить.

Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
"""

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        for item in self.contacts[:]:
            if item["id"] == id:
                self.contacts.remove(item)
        
 
contact = Contacts()

contact.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
contact.add_contacts("Cyrus Jackson", "(501) 472-5218", "nibh@semsempererat.com", False)
contact.add_contacts("Rammstein", "(098) 111-2222", "ramm@semsem.us", True)

print(contact.list_contacts())

contact.remove_contacts(2)

print(contact.list_contacts())