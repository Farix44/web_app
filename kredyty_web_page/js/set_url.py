new_url = 'http://127.0.0.1:8000/'

def read_file(file_name, replace_text = new_url):
    with open(file_name, 'r') as f:
        file_data = f.read()

    new_data = file_data.replace('${BACKEND_HOST}', "'"+replace_text+"'")

    with open(file_name, 'w') as f:
        f.write(new_data)


# otwieranie i modyfikacja plikow na podany wyzej url
read_file('edit_loan.js')
read_file('loan_list.js')
read_file('new_loan.js')


