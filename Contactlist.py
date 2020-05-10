class ContactList(list):
    def __init__(self, list_of_names):
        self.list_of_names = list_of_names

    def search_by_name(self, name):
        same_names = []
        for i in self.list_of_names:
            if name in self.list_of_names:
                same_names.append(name)
                return same_names
            else:
                return 'Name is not in the list'
        



all_contacts = ContactList(['Ivan', 'Masha', 'Jenya'])
print(all_contacts.search_by_name('Masha'))