from behave import given, when, then
from django.conf import settings
#
@when(u'I request to see all neighborhoods')
def step_impl(context):
    context.response = context.get_url('/core/bairros')

@then(u'I will see all avaiable neighborhoods')
def step_impl(context):
    response = context.response
    context.assertEqual(response.status_code, 200)

@when(u'I request to see all categories')
def step_impl(context):
    context.response = context.get_url('/core/categorias')

@then(u'I will see all avaiable categories')
def step_impl(context):
    response = context.response
    context.assertEqual(response.status_code, 200)

@when(u'I request to see all elements from a certain neighborhood')
def step_impl(context):
    context.response = context.get_url('/core/todos/bairro/1')

@then(u'I will see all avaiable elements in that neighborhood')
def step_impl(context):
    response = context.response
    context.assertEqual(response.status_code, 200)

@when(u'I request to see all elements from a certain category')
def step_impl(context):
    context.response = context.get_url('/core/todos/categoria/1')

@then(u'I will see all avaiable elements in that category')
def step_impl(context):
    response = context.response
    context.assertEqual(response.status_code, 200)

@when(u'I request to see all elements from a neighborhood and category')
def step_impl(context):
    context.response = context.get_url('/core/todos/bairro/1/categoria/1')

@then(u'I will see all available elements in that neighborhood and category')
def step_impl(context):
    response = context.response
    context.assertEqual(response.status_code, 200)

@when(u'I request to see all information about an element')
def step_impl(context):
    context.response = context.get_url('/core/elemento/1')

@then(u'I will be able to see that information')
def step_impl(context):
    response = context.response
    context.assertEqual(response.status_code, 200)
