from django.test import TestCase
from animals.models import Animal


class AnimalModelTestCase(TestCase):
    def setUp(self):
        # Create test animals
        self.dog = Animal.objects.create(
            animal_id="DOG123",
            intake_date="2023-01-01",
            location="Test Location",
            intake_condition="NORMAL",
            animal_type="DOG",
            sex="M",
            spayed=True,
            age=365,
            name="Buddy",
            description="Test dog",
            intake_total=1,
            outcome_type="ADOPTION"
        )
        
        self.cat = Animal.objects.create(
            animal_id="CAT456",
            intake_date="2023-01-01",
            location="Test Location",
            intake_condition="NORMAL",
            animal_type="CAT",
            sex="F",
            spayed=True,
            age=180,
            name="Whiskers",
            description="Test cat",
            intake_total=1,
            outcome_type=""
        )
        
        self.stray = Animal.objects.create(
            animal_id="STRAY789",
            intake_date="2023-01-01",
            location="Test Location",
            intake_condition="NORMAL",
            animal_type="DOG",
            sex="M",
            spayed=False,
            age=730,
            name="Rover",
            description="Test stray",
            intake_total=1,
            outcome_type="TRANSFER"
        )

    def test_str_method(self):
        """Test the __str__ method returns the animal_id"""
        self.assertEqual(str(self.dog), "DOG123")
        self.assertEqual(str(self.cat), "CAT456")
        self.assertEqual(str(self.stray), "STRAY789")

    def test_is_adoptable(self):
        """Test the is_adoptable method correctly identifies adoptable animals"""
        self.assertTrue(self.dog.is_adoptable())
        self.assertFalse(self.cat.is_adoptable())
        self.assertFalse(self.stray.is_adoptable())

    def test_is_dog(self):
        """Test the is_dog method correctly identifies dogs"""
        self.assertTrue(self.dog.is_dog())
        self.assertFalse(self.cat.is_dog())
        self.assertTrue(self.stray.is_dog())