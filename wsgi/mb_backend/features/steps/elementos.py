from behave import given, when, then
from django.conf import settings



@given(u'eu sou um usuario comum')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given eu sou um usuario comum')

@when(u'eu digito o id da comunidade')
def test_some_view(self):
        url = reverse('core/comunidade/1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

@then(u'eu verei todos os elementos criados na comunidade')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then eu verei todos os elementos criados na comunidade')

@when(u'eu digito o id do elemento')
def step_impl(context):
    raise NotImplementedError(u'STEP: When eu digito o id do elemento')

@then(u'eu serei capaz de ver as informacoes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then eu serei capaz de ver as informacoes'
)
