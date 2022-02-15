from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired, ValidationError

def positive_value(form, field):
    if field.data <= 0:
        raise ValidationError('La cantidad debe ser mayor que cero!')

opciones = ("Ingreso", 
            "Egreso")

class MovimentClass(FlaskForm):
    cantidad = FloatField('Cantidad', [DataRequired(), positive_value], default = 0)
    tipo = SelectField('Tipo', [DataRequired()], choices = opciones)
    concepto = StringField('Concepto', [DataRequired()], default = '')
    fecha = DateField('Fecha', [DataRequired()], default ='')
    agregar = SubmitField('Agregar')