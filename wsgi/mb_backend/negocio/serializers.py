from rest_framework import serializers
from .models import Comercio
from core.serializers import BairroSerializer, CategoriaSerializer

# classe utilizada para fazer com que as variacoes das imagens de um elemento possam ser acessadas pelo front end
# a classe cria uma lista a partir do campo com a imagem
class StdImageField(serializers.ImageField):
    """
    Get all the variations of the StdImageField
    """

    def to_native(self, obj):
        return self.get_variations_urls(obj)

    def to_representation(self, obj):
        return self.get_variations_urls(obj)

    def get_variations_urls(self, obj):
        """
        Get all the logo urls.
        """

        # Initiate return object
        return_object = {}

        # Get the field of the object
        field = obj.field

        # A lot of ifs going araound, first check if it has the field variations
        if hasattr(field, 'variations'):
            # Get the variations
            variations = field.variations
            # Go through the variations dict
            for key in variations.keys():
                # Just to be sure if the stdimage object has it stored in the obj
                if hasattr(obj, key):
                    # get the by stdimage properties
                    field_obj = getattr(obj, key, None)
                    if field_obj and hasattr(field_obj, 'url'):
                        # store it, with the name of the variation type into our return object
                        return_object[key] = super(StdImageField, self).to_representation(field_obj)

        # Also include the original (if possible)
        if hasattr(obj, 'url'):
            return_object['original'] = super(StdImageField, self).to_representation(obj)

        return return_object

class ComercioSerializer(serializers.ModelSerializer):
    bairro = BairroSerializer()
    lista_de_categorias =CategoriaSerializer(many = True)
    imagem = StdImageField()

    class Meta:
        model = Comercio
        #fields = ('id', 'bairro', 'nome', 'nome_do_proprietario', 'telefone','endereco_oficial', 'endereco_usual', 'latitude', 'longitude', 'descricao', 'lista_de_categorias', 'imagem')
        fields = '__all__'

class ComercioSerializerBasic(serializers.ModelSerializer):
    imagem = StdImageField()
    class Meta:
        model = Comercio
        fields = ('id', 'nome', 'descricao', 'imagem')
