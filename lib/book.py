#!/usr/bin/env python3

# class Book:
#     def __init__(self, title, page_count):
#         # if self.valid_page_count(page_count):
#         #     self.page_count = page_count
#         #     self.title = title
#         # else:
#         #     print("page_count must be an integer")
#         if isinstance(page_count, int):
#             self.title = title
#             self.page_count = page_count
#         else:
#             raise ValueError("page_count must be an integer")      

#     def turn_page(self):
#         print("Flipping the page...wow, you read fast!")
    
#     # def valid_page_count(self, page_count):
#     #     if type(page_count) == int:
#     #         self.page_count = page_count

# class Book:
#     def __init__(self, title, page_count):
#         if isinstance(page_count, int):
#             self.title = title
#             self.page_count = page_count
#         else:
#             try:
#                 int(page_count)  # Try to convert page_count to an integer
#             except ValueError:
#                 print("page_count must be an integer")
#             else:
#                 self.title = title
#                 self.page_count = int(page_count)

#     def turn_page(self):
#         print("Flipping the page...wow, you read fast!")

class Book:
    
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")