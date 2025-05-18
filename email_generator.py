
from jinja2 import Template

def generate_email(biz_name, industry):
    with open("templates/email_template.txt", encoding="utf-8") as f:
        tmpl = Template(f.read())

    return tmpl.render(business_name=biz_name, industry=industry)
