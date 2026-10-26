from pyscript import display, document


def country_capital(e):

    document.getElementById('result').innerHTML = " "

    user_input = document.getElementById('input1').value.capitalize().strip()
    countries = {
        'Madagascar':'Antananarivo',
        'Mongolia':'Ulaanbaataar',
        'Egypt':'Cairo',
        'Philippines':'Manila',
        'USA':'Washington, D.C.',
        'Denmark':'Copenhagen',
        'Chile':'Santiago'
    }
    country_check = user_input in countries
    country_check2 = (countries[user_input])
    mssg_disp = (f'{user_input} not in the list', f'{country_check2}')

    display(mssg_disp[country_check], target='result')

    # display(countries[user_input], target='result')
