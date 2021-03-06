DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_python_dev = list(filter(lambda worker: worker["language"]=="python",DATA))
    all_python_dev = list(map(lambda worker:worker["name"],all_python_dev))

    # all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    all_platzi_workers = list(filter(lambda worker: worker["organization"]=="Platzi",DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"],all_platzi_workers))
    
    adults = [worker["name"] for worker in DATA if worker["age"]>18]
    # adults = list(filter(lambda worker: worker["age"] >18,DATA))
    # adults = list(map(lambda worker: worker["name"],adults))

    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    
    new_people = [{**worker, **{'intern':worker["age"] < 18}} for worker in DATA]
    new_people = list(filter(lambda worker: worker["intern"] == True,new_people))
    new_people = list(map(lambda worker: worker["name"],new_people))
    # old_people = list(map(lambda worker: worker | {"old": worker["age"]>70},DATA))

    for worker in new_people:
        print(worker)

if __name__ == "__main__":
    run()