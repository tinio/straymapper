from django.test import TestCase
from animals.forms import AnimalSearchForm


class AnimalSearchFormTestCase(TestCase):
    def test_form_initialization(self):
        """Test that the form initializes with the correct fields and defaults"""
        form = AnimalSearchForm()
        
        # Check that all expected fields are present
        self.assertIn('animal_type', form.fields)
        self.assertIn('sex', form.fields)
        self.assertIn('intake_date_start', form.fields)
        self.assertIn('intake_date_end', form.fields)
        self.assertIn('intake_condition', form.fields)
        self.assertIn('has_image', form.fields)
        self.assertIn('is_adoptable', form.fields)
        self.assertIn('address', form.fields)
        
        # Check default values
        self.assertTrue(form.fields['has_image'].initial)
        self.assertFalse(form.fields['is_adoptable'].initial)
        
    def test_form_validation_empty(self):
        """Test that an empty form is valid"""
        form = AnimalSearchForm(data={})
        self.assertTrue(form.is_valid())
        
    def test_form_validation_with_data(self):
        """Test form validation with valid data"""
        form_data = {
            'animal_type': 'DOG',
            'sex': 'M',
            'intake_date_start': '2023-01-01',
            'intake_date_end': '2023-01-31',
            'intake_condition': 'NORMAL',
            'has_image': True,
            'is_adoptable': True,
            'address': '123 Test St, Austin, TX'
        }
        form = AnimalSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_form_validation_invalid_date(self):
        """Test form validation with invalid date"""
        form_data = {
            'intake_date_start': 'not-a-date',
        }
        form = AnimalSearchForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('intake_date_start', form.errors)
        
    def test_animal_type_choices(self):
        """Test that animal_type field has the correct choices"""
        form = AnimalSearchForm()
        choices = form.fields['animal_type'].choices
        self.assertEqual(len(choices), 3)
        self.assertEqual(choices[0][0], '')
        self.assertEqual(choices[1][0], 'CAT')
        self.assertEqual(choices[2][0], 'DOG')
        
    def test_sex_choices(self):
        """Test that sex field has the correct choices"""
        form = AnimalSearchForm()
        choices = form.fields['sex'].choices
        self.assertEqual(len(choices), 3)
        self.assertEqual(choices[0][0], '')
        self.assertEqual(choices[1][0], 'M')
        self.assertEqual(choices[2][0], 'F')