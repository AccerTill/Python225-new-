import faker
fake = faker.Faker()
for _ in range(500):
    print(fake.unique.random_int())