from django.core.exceptions import ValidationError
import re

class ComplexPasswordValidator:
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError('La contraseña debe contener al menos una letra mayúscula.')
        if not re.findall('[a-z]', password):
            raise ValidationError('La contraseña debe contener al menos una letra minúscula.')
        if not re.findall('[0-9]', password):
            raise ValidationError('La contraseña debe contener al menos un número.')
        if not re.findall('[^A-Za-z0-9]', password):
            raise ValidationError('La contraseña debe contener al menos un símbolo.')

    def get_help_text(self):
        return "Tu contraseña debe tener mayúsculas, minúsculas, números y símbolos."