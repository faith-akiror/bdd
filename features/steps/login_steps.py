from behave import given, when, then

@given('the user is on the login page')
def step_given(context):
    context.page = "login"

@when('the user enters valid username and password')
def step_when_valid(context):
    context.login_success = True
    context.error_message = ""

@when('the user enters valid username and invalid password')
def step_when_invalid(context):
    context.login_success = False
    context.error_message = "Invalid password"

@when('the user leaves username and password empty')
def step_when_empty(context):
    context.login_success = False
    context.error_message = "Please enter username and password"

@when('the user enters credentials of a locked account')
def step_when_locked(context):
    context.login_success = False
    context.error_message = "Account is locked"

@then('the user should see the dashboard')
def step_then_dashboard(context):
    assert context.login_success == True

@then('the user should see an error message')
def step_then_error(context):
    assert context.error_message == "Invalid password"

@then('the user should see a warning message')
def step_then_warning(context):
    assert context.error_message == "Please enter username and password"

@then('the user should see an account locked message')
def step_then_locked(context):
    assert context.error_message == "Account is locked"