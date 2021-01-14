from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    if country_name == 'American Samoa':
        return 'ws'
    elif country_name == 'Antigua and Barbuda':
        return 'ac'
    elif country_name == 'Venezuela':
        return 've'
    elif country_name == 'Cayman Islands':
        return 'cj'
    elif country_name == 'Bahamas':
        return 'bf'
    elif country_name == 'Aruba':
        return 'aa'
    elif country_name == 'Barbados':
        return 'bb'
    elif country_name == 'Bermuda':
        return 'bd'
    elif country_name == 'Dominica':
        return 'do'
    elif country_name == 'Fiji':
        return 'fj'
    elif country_name == 'Gibraltar':
        return 'gi'
    elif country_name == 'Kiribati':
        return 'kr'
    elif country_name == 'Libya':
        return 'li'
    elif country_name == 'Macedonia':
        return 'mk'
    elif country_name == 'Micronesia':
        return 'fm'
    elif country_name == 'Moldova':
        return 'md'
    elif country_name == 'Caledonia':
        return 'nc'
    elif country_name == 'West Bank':
        return 'we'
    elif country_name == 'Virgin':
        return 'vi'
    elif country_name == 'Vietnam':
        return 'vm'
    elif country_name == 'Vanuatu':
        return 'nh'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Qatar':
        return 'qa'
    elif country_name == 'Bolivia':
        return 'bl'

    # Se o país não foi entrado, devolve None
    return None
