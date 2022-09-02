from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util

from django import forms

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

import random

class create_form(forms.Form):
    title = forms.CharField(
        label='Title',
    )

    body = forms.CharField(
        label='',
        widget=forms.Textarea(
        ),
    )

class edit_form(forms.Form): # RFER 17
    # title = forms.CharField(label = 'Title')
    error_initalize:str = 'ERROR: Placeholder. Within code please call variable and place proper existing information.'

    body = forms.CharField(
        label = 'Body', 
        widget = forms.Textarea(
            attrs={'style': "width:100%;"}
        ),
        initial=error_initalize
    )


def index(request:HttpRequest):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        
    })

def entry(request:HttpRequest, entry = None, message = None):
    accepted_args:list[str] = ['success',]
    if message not in accepted_args:
        message = None

    if entry == None:
        entry = random.choice(util.list_entries())

    entry_location = util.get_entry(entry)

    if entry_location == None:
        return render(request, "encyclopedia/404.html", {
            'entry_name':entry,
            
            }
        )

    markdownder = Markdown()
    entry_html = markdownder.convert(str(entry_location))

    return render(request, "encyclopedia/entry.html", {
            'title_info': entry,
            'body_info': entry_html,
            'message': message,
        }
    )

def search(request:HttpRequest): # TODO

    if request.method == 'GET':
        request_get_name_q:str = request.GET.get('q_search')
        # request_get_name_q = request.GET['q'] # RFER 13
        
        # Priority #1 - If there is an exact entry in the list, immediately redirect to the page.
        filtered_class = util.filter_class(request_get_name_q)
        if filtered_class.existence == True: # Rev 2
            return HttpResponseRedirect(reverse('ency:entry', args=[filtered_class.current_entry,]))

                
        # Priority #2 - Regardless if the list has results or is empty, render the search page.
        return render(request, 'encyclopedia/search.html', {
            'search_input': request_get_name_q,
            'similar_results': filtered_class.filtered_list,

            }
        )
            

# Purpose: User exclusively types up a new entry... and then, the user submits it.
def create(request:HttpRequest): 

# This determines what to do after the user submits their 
    # Use util.save_entry() to save info

    if request.method == "POST":
        message:str = "Hello, placeholder handler :3"

        form:create_form = create_form(request.POST)

        if form.is_valid():
            text_title:str = form.cleaned_data['title']
            text_content:str = form.cleaned_data['body']

            """
            Psuedocode:
                - Check if user's new entry exists already (based on title)
                    - If so, redirect to page and have them try again.
                    - This check is being done ahead of time as func 'util.save_entry()' will overwrite pre-existing entries.
                - Use util.save_entry()
                
            """
            """
            - 'if' statement
            - If title already exists in database.
            """
            check_entry = util.filter_class(text_title)

            if check_entry.existence == True:
                message = f"Error: \"{text_title}\" already exists. Try again plwase :'(" 
                # TODO - Figure out how to save user's title and body so they don't need to retype the whole information.

                failed_form = create_form(initial={
                    'title':text_title,
                    'body':text_content
                })
                return render(request, 'encyclopedia/create.html', {
                        'message': message,
                        'previous_title': text_title,
                        'previous_body': text_content,
                        'form':failed_form
                    }
                )

            # If the title was unique and was sucessfully saved!

            # Save entry to a markdown file
            text_content = f'#{text_title}\n' + f'{text_content}' # Have the title be added automatically to the body with '#' for the user
            util.save_entry(text_title, text_content)

            # Revison 2
            return HttpResponseRedirect(reverse('ency:entry', args=[text_title]))

    """
    This is here placed for this scenarios so the user is redirected to the default "create" page:
        - If the link was directly entered
        - If the page was refreshed
            - Current problem is that the user's previous inputs aren't saved.
                - Nevermind, problem only exists if the user timed out? Need to look into this. Unsure what keywords to use to look for information.
    """
    new_form = create_form()
    return render(request, 'encyclopedia/create.html', {
            'form': new_form
        }
    )

def edit(request:HttpRequest, entry:str = None): # TODO # Revison 2
    title_info:str = entry
    body_info = util.get_entry(title_info)

    if request.method == "POST":
        form = edit_form(request.POST)

        if form.is_valid():
            # submission_title = form.cleaned_data['title']
            submission_body = form.cleaned_data['body']

            util.save_entry(entry, submission_body)

            redirect_class = util.filter_class(title_info)
            message = 'success'
            return HttpResponseRedirect(reverse('ency:entry', args=[redirect_class.current_entry,]))

    form = edit_form(initial={'body': body_info})
    return render(request, 'encyclopedia/edit.html', {
            'title_info': title_info,
            # 'body_info': body_info,
            'form': form # RFER 17
        }
    )


# def edit_submission(request:HttpRequest,):
#     if request.method == 'POST':
#         entry = request.POST.get('entry')
#         body_info = request.POST.get('edit_text_area')
#         entry_html = None
#         message = f'Sucessfully edited "{entry}"!'

#         # return render(request, 'encyclopedia/entry.html', {
#         #         'title_info': entry,
#         #         'body_info': entry_html,
#         #         'message': message
#         #     }
#         # ) 


#         output_kwargs = {'entry':'Django','message':'success'}
#         # return HttpResponseRedirect(reverse('ency:entry', args=(),kwargs=output_kwargs))

#         return redirect(f'ency:entry')