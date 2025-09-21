"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = [0] * number

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

    # Comparison methods based on student name
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

def main():
    """Test comparison and sorting of Student objects."""

    # Create several Student objects
    students = [
        Student("Ken", 3),
        Student("Abby", 3),
        Student("Zoe", 3),
        Student("Liam", 3),
        Student("Mia", 3)
    ]

    # Set random scores
    for student in students:
        for i in range(1, 4):
            student.setScore(i, random.randint(70, 100))

    # Shuffle the list
    random.shuffle(students)

    print("Shuffled students:")
    for student in students:
        print(student)
        print()

    # Sort the list
    students.sort()

    print("Sorted students by name:")
    for student in students:
        print(student)
        print()

    # Test comparison operators
    print("Comparison tests:")
    print(f"{students[0].getName()} == {students[1].getName()}? {students[0] == students[1]}")
    print(f"{students[0].getName()} < {students[1].getName()}? {students[0] < students[1]}")
    print(f"{students[0].getName()} >= {students[1].getName()}? {students[0] >= students[1]}")

if __name__ == "__main__":
    main()
