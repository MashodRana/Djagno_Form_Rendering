 # How to Render Django Form

 This repo contains the multiple way to work with django form. 
 You will find code for
 - raw dajngo raw form into html page
 - Using Custom HTML Attributes  on form class with widgets
 - Using Custom HTML Attributes on form class with widgets and bootstrap class name

 The actual article is [here](https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html#working-example) written by **Vitor Freitas**.

 Here is few short notes from the original article.
 
 #### _html_output private method defined in the BaseForm is the responsible for html output.

 what the _html_output does with the form:
- Aggregate the errors that are not attached to specific fields (non field errors) and errors from hidden fields;
- Place the non field errors and hidden field errors on top of the form;
- Iterate through all the form fields;
- Render the form fields one by one;
- Render the field name in a label tag;
- If there are field errors, render a HTML list with errors first;
- Render the HTML input for the field;
- If there is a help text, render it after the field.

### Form rendering 

- form.non_field_errors (list)
- form.hidden_fields (list)
    - hidden_field
        - hidden_field.errors (list)
        - hidden_field.name
- form.visible_fields (list)
    - field
        - field.label_tag
        - field.errors (list)
        - field.help_text

## Dependencies
- django==2.2
- python==3.6.9