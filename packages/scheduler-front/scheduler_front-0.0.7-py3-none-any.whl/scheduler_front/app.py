import webbrowser
from flask import Flask, render_template, request
from scheduler_front.script_template import file as source_file

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        write_scheduler_configuration_file(request)
        write_query(request)
        write_script_configuration_file(request)
        copy_script_template(request)
        return 'done'


def copy_script_template(request):
    output_dir = parse_output_dir(request)
    filename = f"{output_dir}\script.py" if output_dir else 'script.py'

    with open(filename, 'w') as destination_file:
        destination_file.write(source_file)

def parse_destination_email(request):
    return request.form['destination_email']


def parse_kind_of_query(request):
    return request.form['kind_of_query']


def parse_email_subject(request):
    return request.form['subject_email']


def parse_email_body(request):
    return request.form['body_email']


def parse_output_file_format(request):
    return request.form['output_type']


def parse_error_email(request):
    return request.form['error_email']

def parse_output_dir(request):
    return request.form['output_dir']

def write_script_configuration_file(request):
    output_dir = parse_output_dir(request)
    kind_of_query = parse_kind_of_query(request)
    destination_email = parse_destination_email(request)
    email_subject = parse_email_subject(request)
    email_body = parse_email_body(request)
    output_file_format = parse_output_file_format(request)
    email_sender = parse_error_email(request)

    filename = f"{output_dir}\script_config.py" if output_dir else 'script_config.py'

    with open(filename, 'w') as f:
        f.write(f"kind_of_query = '{kind_of_query}'\n")
        f.write(f"output_type = '{output_file_format}'\n")
        f.write(f"destination_email = '{destination_email}'\n")
        f.write(f"email_subject = '{email_subject}'\n")
        f.write(f"email_body = '{email_body}'\n")
        f.write(f"email_sender = '{email_sender}'")


def write_query(request):
    output_dir = parse_output_dir(request)
    filename = f"{output_dir}\query.sql" if output_dir else 'query.sql'

    with open(filename, 'w') as f:
        f.write(request.form['query'])

def parse_days(request):
    # TODO: ADD ASSERTIONS
    return request.form['days']

def parse_weekdays(request):
    weekdays = ""

    days_of_the_week = [
        'sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday'
    ]

    for i, day in enumerate(days_of_the_week):
        try:
            if request.form[day]:
                weekdays += f"{i}, "
        except KeyError:
            pass

    return weekdays

def parse_months(request):
    months = ""
    months_of_the_year = [
        'jan',
        'feb',
        'mar',
        'apr',
        'may',
        'jun',
        'jul',
        'aug',
        'sep',
        'oct',
        'nov',
        'dec'
    ]

    for i, month in enumerate(months_of_the_year):
        try:
            if request.form[month]:
                months += f"{i + 1}, "
        except KeyError:
            pass

    return months


def write_scheduler_configuration_file(request):
    error_email = parse_error_email(request)
    days = parse_days(request)
    weekdays = parse_weekdays(request)
    months = parse_months(request)

    output_dir = parse_output_dir(request)
    filename = f"{output_dir}\config.txt" if output_dir else 'config.txt'

    with open(filename, 'w') as f:
        if not error_email:
            raise ValueError
        else:
            f.write(f"error_email: {error_email}\n")
        if days:
            f.write(f"days: {days}\n")
        if weekdays:
            f.write(f"weekdays: {weekdays}\n")
        if months:
            f.write(f"months: {months}\n")


def start():
    webbrowser.open('http://127.0.0.1:5000')
    app.run()


if __name__ == '__main__':
    start()