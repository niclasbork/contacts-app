import json, math, os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, '../data', 'contacts.json')


# print(f'Path to contacts.json: {file_path}')


class App:
	def __init__(self, text, size):
		self.text = text
		self.size = size

	def prettyPrint(self):
		"""
		Prints a text inside a box.
		:param text: - str: Input converted to string for inside the box
		:param size: - int: width of the box: number of '-'
		:return: None
		"""
		text = str(self.text)
		size = int(self.size)
		spaces = size - len(text) - 2
		spaces_l = math.floor(spaces / 2)
		spaces_r = math.ceil(spaces / 2)

		print('=' + (size - 2) * '=' + '=')
		print('|' + spaces_l * ' ' + text + spaces_r * ' ' + '|')
		print('=' + (size - 2) * '=' + '=')

	def importFile(self):
		"""
		JSON data is fetched and processed
		:return: JSON data
		"""
		try:
			with open(file_path, 'r') as file:
				self.data = json.load(file)
		except FileNotFoundError:
			print('The file was not found.')
		except json.JSONDecodeError:
			print('Error decoding the JSON file.')

	def writeFile(self):
		"""
		Writes the data stored in the `self.data` attribute to a JSON file.
		:return: None
		"""
		with open(file_path, 'w') as output:
			json.dump(self.data, output)

	def displayMenu(self):
		"""
		The user is prompted to complete the next steps or exit the app
		:return: None
		"""
		print('1. Show contact')
		print('2. Change contact')
		print('3. Add contact')
		print('4. Delete contact')
		print('5. Search contact')
		print('6. Exit')

		self.userSelection()

	def userSelection(self):
		"""
		The user has 1-6 choices of functions
		:return: User input
		"""
		option = input('Choose[1-6]: ⚡️ >> ').strip()
		if option == '':
			print('Please choose a number. 👽')
			self.userSelection()
		else:
			try:
				option = int(option)
				print('›››', option, '‹‹‹')
				if option == 1:
					self.displayContacts()
					self.displayMenu()
				elif option == 2:
					print('Change contact: 🌍')
					self.changeContact()
				elif option == 3:
					print('Add contact: 👽')
					self.addContact()
					self.displayMenu()
				elif option == 4:
					self.deleteContact()
				elif option == 5:
					self.searchContact()
				elif option == 6:
					print('Good bye! 🖖')
					exit()
				else:
					print('Option unavailable. 🪐')
					self.displayMenu()
			except ValueError:
				print('Wrong value! Please enter a number between 1 and 6. 👽')
				self.userSelection()

	def displayContacts(self):
		"""
		This method will iterate over the loaded JSON data and display user information.
		:return: None
		"""
		if self.data:
			print('=' * 122)
			print(f'| ID:{'':<1}| Name:{'':<10} | Email:{'':<19} | Number:{'':<8} | Address:{'':<22} | City:{'':<10} |')
			print('=' * 122)
			for contact in self.data['contacts']:
				print(
					f'| {contact['id']:<3} | {contact['name']:<15} | {contact['email']:<25} | {contact['number']:<15} | {contact['address']:<30} | {contact['city']:<15} |')
			print('=' * 122)
			print()
		else:
			print('No data to display.')

	def addContact(self):
		"""
		Adds a new contact to the contact list. Once the contact is added
		successfully, the new contact data is saved to a JSON file.
		:return: None
		"""
		count = len(self.data['contacts'])
		while True:
			try:
				while True:
					name = input('Enter contact name: ').strip()
					if name:
						break
					else:
						print('Name cannot be empty. Please enter a valid name.')

				while True:
					email = str(input('Enter contact email: ')).strip()
					if email:
						break
					else:
						print('Email cannot be empty. Please enter a valid email.')

				while True:
					check_number = input('Enter contact number: ').strip()
					if check_number:
						if check_number.isdigit():
							number = int(check_number)
							break
						else:
							print('Number must be numeric. Please enter a valid number.')
					else:
						print('Number cannot be empty. Please enter a valid number.')

				while True:
					address = str(input('Enter contact address: ')).strip()
					if address:
						break
					else:
						print('Address cannot be empty. Please enter a valid address.')

				while True:
					city = str(input('Enter contact city: ')).strip()
					if city:
						break
					else:
						print('City cannot be empty. Please enter a valid city.')

				print('Contact: ' + name + ' added successfully!\n')
				print(f'Some next steps {name}?')

				new_contact = {
					"id": count + 1,
					"name": name,
					"email": email,
					"number": number,
					"address": address,
					"city": city
				}

				self.data['contacts'].append(new_contact)

				self.writeFile()
				break
			except ValueError:
				print('Wrong input. Please enter a correct format.')
				continue

	def changeContact(self):
		"""
		Updates an existing contact. The updated contact information is then saved to a JSON file.
		:return: None
		"""
		is_update = False
		self.displayContacts()

		selected_user = str(input('Enter the contact name you want to change: '))

		for contact in self.data['contacts']:
			if contact['name'] == selected_user:
				print(f'Contact {selected_user} found!')
				try:
					new_name = str(input('Enter NEW contact name: '))
					if new_name:
						contact['name'] = new_name
						print('Updated!')
					else:
						print('Skipped!')
					new_email = str(input('Enter NEW contact email: '))
					if new_email:
						contact['email'] = new_email
						print('Updated!')
					else:
						print('Skipped!')
					new_number = str(input('Enter NEW contact number: '))
					if new_number:
						contact['number'] = new_number
						print('Updated!')
					else:
						print('Skipped!')
					new_address = str(input('Enter NEW contact address: '))
					if new_address:
						contact['address'] = new_address
						print('Updated!')
					else:
						print('Skipped!')
					new_city = str(input('Enter NEW contact city: '))
					if new_city:
						contact['city'] = new_city
						print('Updated!')
					else:
						print('Skipped!')
					is_update = True
					print(f'Data {selected_user} successfully changed to {new_name}.\n')
					self.writeFile()
					print(f'Some next steps {new_name}?')
					print('Update complete! 🛰️')
					self.displayMenu()
				except ValueError:
					print('Wrong input! Please enter a valid name.')
				break
		if not is_update:
			print(f'Contact with the name {selected_user} was not found.\n')
			self.displayMenu()

	def deleteContact(self):
		"""
		Deletes a contact from the stored contact list based on the name provided by the user.
		:return: None
		"""
		self.displayContacts()

		selected_user = str(input('Enter the contact\'s name you want to delete: ')).strip()
		is_delete = False

		for i, contact in enumerate(self.data['contacts']):
			if contact['name'] == selected_user:
				print(f'Contact {selected_user} found!')

				del self.data['contacts'][i]

				self.writeFile()

				print(f'Contact {selected_user} deleted successfully!\n')
				is_delete = True
				break
		if not is_delete:
			print(f'Contact with the name {selected_user} was not found.\n\n')
		self.displayMenu()

	def searchContact(self):
		"""
		Prompts the user to enter a search term to find a contact by name.
		If a contacts name contains the search term, it prints the contacts name.
		:return: None
		"""
		find_user = str(input('Enter something to find a contact: ')).lower()
		is_found = False
		print(f'Contact found:')
		for contact in self.data.get('contacts'):
			if find_user in contact.get('name', '').lower():
				print(contact['name'])
				is_found = True
		print()
		if not is_found:
			print(f'No contact found matching your search: {find_user}.\n')
		self.displayMenu()
