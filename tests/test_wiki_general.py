from webbrowser import get
import pytest
from pytest_django.asserts import assertTemplateUsed, assertURLEqual, assertContains, assertRedirects # RFER 19

from django.template import response

from django.test import Client, RequestFactory


class Test_create:


    def test_template(self, client:Client):
        response = client.get('/create')
        assertTemplateUsed(response,'encyclopedia/create.html')
    
    # def test_status_code(self, rf:RequestFactory): ### Currently not sure how to write tests for status code
    #     request:RequestFactory = rf.get('/create')
    #     response = views.create(request)
    #     assert response.status_code == 200


class Test_edit:
    def test_template(self, client:Client):
        response = client.get('/edit/Python')
        assertTemplateUsed(response,'encyclopedia/edit.html')

class Test_entry:
    def test_template(self, client:Client):
        response = client.get('/wiki/Python')
        assertTemplateUsed(response,'encyclopedia/entry.html')
    
class Test_index:
    def test_template(self, client:Client):
        response = client.get('/')
        assertTemplateUsed(response,'encyclopedia/index.html')

class Test_layout:
    def test_template(self, client:Client):
        response = client.get('/')
        assertTemplateUsed(response,'encyclopedia/layout.html')


class Test_search:

    def test_template(self, client:Client):
        response = client.get('/search?&q_search=te')
        assertTemplateUsed(response,'encyclopedia/search.html')

    def test_statuscode_302_redirected_to_entry_page(self, client:Client):
        response = Client().get('/search', {'q_search':'Python'}, 
        )

        assert response.status_code == 302, 'The "request.get" should redirect directly to the Python entry page, which code is 302.'

        # RFER 23
        assertRedirects(response, '/wiki/Python', status_code=302, target_status_code=200)

    def test_statuscode_200_search_results_similar_substrings(self, client:Client):
        response = client.get('/search', {'q_search':'Pyth'})

        assert response.status_code == 200, "The response should be 200, which the entry should leads to search results page where the substring is found in the some of the entries."
