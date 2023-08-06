import openai
import markdown
from categories import *


class Book:
    """
    This class represents a book.

    Attributes:
        chapter_amount: The amount of chapters the book has.
        words_per_chapter: The amount of words per chapter.
        category: The category of the book.
        topic: The topic of the book.
        title: The title of the book.
        chapter_titles: The titles of the chapters.
        structure: The structure of the book.
    """

    def __init__(self, chapter_amount: int, words_per_chapter: int, topic: str, category: str):
        """
        This is the constructor for the Book class. It initializes the object with the given parameters.
        :param chapter_amount: The number of chapters in the book (int).
        :param words_per_chapter: The number of words per chapter (int).
        :param topic: The topic of the book (str).
        :param category: The category of the book (fiction, non-fiction, etc) (str).
        """

        # Define chapter amount
        self.chapter_amount = chapter_amount

        # Define words per chapter
        self.words_per_chapter = words_per_chapter

        # Define topic
        self.topic = topic

        # Define category
        self.category = category

        print('Initializing..')

        # Get book using `get_category` method
        self.book = self.get_category()

        # Set the title of the book
        self.title = self.get_title()

        # Set the chapter titles
        self.chapter_titles = self.get_chapter_titles()

        # Set the structure of the book
        self.structure = self.get_structure()

        self.packed = None

    @staticmethod
    def __get_edit(input_text, instruction, temperature: float = 0):
        """
        This is a private, static method for getting an edited version of the given input text.
        :param input_text: The text to be edited.
        :param instruction: The instructions for the edit.
        :param temperature: The temperature of the edit (defaults to 0).
        :return: The edited text.
        """

        # Define the engine to use and returning the edited version
        return openai.Edit.create(
            model="text-davinci-edit-001",
            input=input_text,
            instruction=instruction,
            temperature=temperature).choices[0].text

    def get_category(self):

        # Get the category
        self.category = self.category

        # Return the category class
        return globals()[self.category](self.chapter_amount, self.words_per_chapter, self.topic)

    def get_title(self):
        """
        This method returns the title of the book.
        """

        # Get the title of the book and delete the blank lines
        title = self.book.get_title().replace('\n', '')

        # Return the title
        return title

    def get_chapter_titles(self):
        """
        This method returns the chapter titles of the book.
        """

        # Define the chapter titles as the chapter titles of the book
        chapters = self.book.get_chapters(self.title).split('\n')

        # Remove the blank lines
        chapters = [chapter for chapter in chapters if chapter != '']

        # Return the chapter titles
        return chapters

    def get_structure(self):
        """
        This method returns the structure of the book.
        """

        # Get the structure of the book and splitting it by the new lines
        structure = self.book.get_structure(self.title, self.chapter_titles).split('\n')

        # Remove the blank lines
        structure = [chapter for chapter in structure if chapter != '']

        # Create a list of chapters
        chapter_list = []

        # Create a list of paragraphs
        chapter = []

        # Iterate over the lines
        for line in structure:

            # If the line starts with 'Chapter'
            if line.lower().startswith('chapter'):
                # Add the chapter to the list of chapters
                chapter_list.append(chapter)

                # Create a new list of paragraphs
                chapter = []

            # Add the line to the list of paragraphs
            chapter.append(line)

        # Add the last chapter to the list of chapters
        chapter_list.append(chapter)

        # Remove the first chapter
        chapter_list = chapter_list[1:]

        # Remove the first paragraph of each chapter
        chapter_list = [chapter[1:] for chapter in chapter_list]

        # Create a new list of chapters
        chapter_list_new = []

        # Iterate over the chapters
        for chapter in chapter_list:

            # Create a list of paragraphs
            paragraph_list = []

            # Iterate over the paragraphs
            for paragraph in chapter:

                # Get the title of the paragraph
                title = paragraph.split('---')[0]

                # Get the word count of the paragraph
                word_count = paragraph.split('---')[1]

                # If the word count contains the word 'words'
                if 'words' in word_count.lower():
                    # Remove the word 'words'
                    word_count = word_count.split(' ')[0]

                # Add the paragraph to the list of paragraphs
                paragraph_list.append({'title': title, 'word_count': word_count})

            # Add the list of paragraphs to the list of chapters
            chapter_list_new.append(paragraph_list)

        # Return the list of chapters
        return chapter_list_new

    def get_paragraph(self, chapter_index, paragraph_index):
        """
        This method returns the paragraph at the given index in the given chapter.
        :param paragraph_index: The index of the paragraph.
        :param chapter_index: The index of the chapter.
        :return: The paragraph.
        """

        # Get the paragraph at the given index in the given chapter
        return self.book.get_paragraph(self.title, self.chapter_titles, self.structure, paragraph_index, chapter_index)

    def get_chapter(self, chapter_index):
        """
        This method returns the chapter at the given index.
        :param chapter_index: The index of the chapter.
        :return: The chapter.
        """

        # Define empty list for the paragraphs
        chapter = []

        # Iterate over the paragraphs in the chapter
        for i in range(len(self.structure[chapter_index])):

            # Add the paragraph to the list of paragraphs
            chapter.append(self.get_paragraph(chapter_index, i))

        # Return the chapter
        return chapter

    def get_content(self):
        """
        This method returns the book.
        :return: The book.
        """

        # Define empty list for the content of the chapters
        content = []

        # Iterate over the chapters
        for i in range(len(self.structure)):

            # Add the content of the chapter to the list
            content.append(self.get_chapter(i))

        # Return the content
        return content

    def generate(self):
        """
        This method generates the book.
        """

        # Get content
        content = self.get_content()

        # Pack book
        book = {'title': self.title, 'chapters': content, 'chapter_titles': self.chapter_titles, 'structure': self.structure}

        # Return the book
        self.packed = book

    def get_md(self):
        """
        This method returns the book in Markdown format.
        """

        # Check if variable packed is exists
        if self.packed is None:
            print('Book not generated yet. Generating book...')
            self.generate()

        # Get the book
        book = self.packed

        # Define the variables
        content = book['chapters']

        # Build the book

        # Add the title of the book
        book = '# ' + self.title + '\n\n\n'

        # Add the chapter titles and content
        for i in range(len(content)):

            # Add the chapter title in md format
            book += '\n\n## ' + self.chapter_titles[i] + '\n'

            # Iterate through the paragraphs
            for paragraph in content[i]:

                # Check if paragraph ends with a blank line
                if paragraph.endswith('\n'):

                    # Add the paragraph
                    book += paragraph
                else:

                    # Add the paragraph with a blank line
                    book += paragraph + '\n'

        # Return the combined book.
        return book

    def get_html(self):
        """
        This method returns the book in HTML format.
        """

        # Getting Markdown element
        md = markdown.markdown(self.get_md())

        # Return the HTML
        return md
