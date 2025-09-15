superHeroes = {
    "Batman": {
        "id": 1,
        "aliases": ["Bruce Wayne", "Darkknight"],
        "location": {
            "number": 1007,
            "street": "Mountain Drive ",
            " city ": "Gotham",
        },
    },
    "Superman": {
        "id": 2,
        "aliases": ["Kal-El", "Clark Kent", "The Man of Steel"],
        "location": {
            "number": 344,
            "street": "ClintonStreet",
            "apartment": "3D",
            "city": "Metropolis",
        },
    },
}

print(superHeroes["Superman"]["location"]["city"])