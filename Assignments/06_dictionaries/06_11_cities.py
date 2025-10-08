cities = {'Reading': { 'Country': 'United States', 'Population': 2934648, 'Fact': 'Reading is trash.'}, 
          'Philly': {'Country': 'United States', 'Population': 3553, 'Fact': 'Its worse than Reading.'},
          'Allentown': {'Country': 'United States', 'Population': 4345545, 'Fact': 'Its close to Reading.'}  }


for city, info in cities.items():

    print(f"\nCity:{city}")
    print(f"\nCountry:{info['Country']}")
    print(f"\nPopulation:{info['Population']}")
    print(f"\nFact:{info['Fact']}")
    print('.............')