import unittest
"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Domyślamy się, że w pewnym napisie schowany został "shrug", czyli ¯\_(ツ)_/¯. 
Shrug może być ewentualnie podzielony na dwie części, czyli np. "¯\_(ツ....)_/¯" lub
"¯\_#######(ツ)_/¯" też zaliczamy do napisów zawierających shrug-a, ale już nie np
"¯\_###(ツ)###_/¯". Proszę napisać funkcję, która sprawdza czy w podanym napisie `line` zawarty jest shrug. 


"""


def has_hiddden_shrug(line: str) -> bool:
    # Znajdź indeksy początkowe i końcowe kluczowych części "shruga"
    left_arm_start = line.find("¯\\_")
    right_arm_end = line.find("_/¯") + len("_/¯")
    face_start = line.find("(ツ)")
    face_end = face_start + len("(ツ)")

    # Sprawdź, czy wszystkie części są obecne
    if -1 in [left_arm_start, right_arm_end, face_start]:
        return False

    # Sprawdź, czy części są w odpowiedniej kolejności
    if not (left_arm_start <= face_start < face_end <= right_arm_end):
        return False

    # Sprawdź, czy nie ma niedozwolonych znaków przed "shrugiem" i po "shrugu"
    if left_arm_start != 0 or right_arm_end != len(line):
        return False

    return True

    pass


class TestEngine3(unittest.TestCase):

    def test_1(self):
        self.assertEqual(has_hiddden_shrug("¯\_(ツ)_/¯"), True)

    def test_2(self):
        self.assertEqual(has_hiddden_shrug("¯\_##(ツ)_/¯"), True)

    def test_3(self):
        self.assertEqual(has_hiddden_shrug("¯\_(ツ)##_/¯"), True)

    def test_4(self):
        self.assertEqual(has_hiddden_shrug("¯\_##(ツ)##_/¯"), False)

    def test_5(self):
        # Dodatkowe napisy przed shrugiem nie są dozwolone
        self.assertEqual(has_hiddden_shrug("##¯\_##(ツ)_/¯"), False)

    def test_6(self):
        # Shrugi z krótkimi rękoma nie są dozwolone
        self.assertEqual(has_hiddden_shrug("¯\(ツ)/¯"), False)


if __name__ == '__main__':
    unittest.main()