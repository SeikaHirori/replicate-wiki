# from webbrowser import get
# from xml.dom.minidom import parseString
# import pytest
# from pytest_django.asserts import assertTemplateUsed, assertURLEqual, assertContains, assertRedirects # RFER 19

# from django.template import response

# from django.test import Client, RequestFactory


# class Test_create:


#     pass


# class Test_edit:
#     pass

# class Test_entry:
#     pass
    
# class Test_index:
#     pass

# class Test_layout:
#     pass


# class Test_search:
#     Pylenium test (Pylenium will be referred af pyl) # RFER 24
#     def test_pylenium_search_results(self, py):
#         py.visit('http://localhost:8000/create')
#         py.get("[name='q_search']").type('py') # ply types the substring
#         py.get("[name='form_search']").submit() # ply simluates "enter" to submit the search
#         py.get('a[href="/wiki/Python"]').click() # ply finds an element (in this case: attribute's href) that matches test's desired outcome.

#         assert py.should().contain_title('Python')

#     def test_plyenium_redirect_to_entry(self, py):
#         py.visit('http://localhost:8000/create')
#         py.get("[name='q_search']").type('Python') # ply types the substring
#         py.get("[name='form_search']").submit()
        
#         assert py.should().contain_title('Python')
    