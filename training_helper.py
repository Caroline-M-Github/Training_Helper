# Work out list of courses
# Pluralsight API a possibility

recommended_courses = {
    "data": {
        "beginner": ["Course 1", "Course 2", "Course 3"],
        "intermediate": ["Course 1", "Course 2", "Course 3"],
        "advanced": ["Course 1", "Course 2", "Course 3"]
    },
    "devsecops": {
        "beginner": ["Course 1", "Course 2", "Course 3"],
        "intermediate": ["Course 1", "Course 2", "Course 3"],
        "advanced": ["Course 1", "Course 2", "Course 3"]
    },
    "aiml": {
        "beginner": ["Course 1", "Course 2", "Course 3"],
        "intermediate": ["Course 1", "Course 2", "Course 3"],
        "advanced": ["Course 1", "Course 2", "Course 3"]
    },
    "cloud": {
        "beginner": ["Course 1", "Course 2", "Course 3"],
        "intermediate": ["Course 1", "Course 2", "Course 3"],
        "advanced": ["Course 1", "Course 2", "Course 3"]
    },
    "general": {
        "beginner": ["Course 1", "Course 2", "Course 3"],
        "intermediate": ["Course 1", "Course 2", "Course 3"],
        "advanced": ["Course 1", "Course 2", "Course 3"]
    },
    "front end": {
        "beginner": ["Course 1", "Course 2", "Course 3"],
        "intermediate": ["Course 1", "Course 2", "Course 3"],
        "advanced": ["Course 1", "Course 2", "Course 3"]
    },
}

def get_user_input():
    name = input("What is your name? ")
    type_of_engineer = input("What type of engineer are you? (e.g., general, data, DevSecOps, Cloud, front end) ").lower()
    proficiency_level = input("What is your proficiency level? (e.g., beginner, intermediate, advanced) ").lower()
    return name, type_of_engineer, proficiency_level

def recommend_courses(type_of_engineer, proficiency_level):
    if type_of_engineer in recommended_courses and proficiency_level in recommended_courses[type_of_engineer]:
        return recommended_courses[type_of_engineer][proficiency_level]
    else:
        return ["No courses found for your input. Please check your type and proficiency."]

def main():
    print("Welcome to the Engineering Course Recommender App!")
    name, type_of_engineer, proficiency_level = get_user_input()

    courses = recommend_courses(type_of_engineer, proficiency_level)

    print("\nHello {}, based on your input here are some recommended courses:".format(name))
    for course in courses:
        print("- " + course)

if __name__ == "__main__":
    main()
