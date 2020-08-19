import re

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ', '.join(cars['Jeep'])

def get_first_model_each_manufacturer(cars=cars):
    """rturn a list of matching models (original ordering)"""
    resultado = []
    for key in cars.keys():
        resultado.append(cars[key][0])
    return resultado



def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    resultado = []
    for key in cars.keys():
        for model in cars[key]:
            print(model)
            if re.search(grep, model, flags=re.IGNORECASE):
                resultado.append(model)
                print('match')
                print('resultado: ' + str(resultado))
            else:
                print('no match')
    resultado.sort()
    return resultado


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    cars_copy = cars.copy()
    for key in cars_copy.keys():
       cars_copy[key].sort()
    return(cars_copy)

def main():
    print(get_all_matching_models(cars, 'o'))

if __name__ == "__main__":
    main()