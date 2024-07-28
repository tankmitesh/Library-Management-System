# Inbuild Packages
import os
import uuid
import warnings
import logging
warnings.filterwarnings("ignore")
from datetime import datetime
database_dir = os.path.join(os.getcwd(), "database")

# Third Party Packages
from pandas import read_csv, DataFrame, concat

#############################################################################################

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("library_management.log"),
                              logging.StreamHandler()])

logger = logging.getLogger(__name__)

#############################################################################################

class BookManager:
    def add_book(self, title: str, author: str, isbn: int,
                 genre: str = None, lang: str = None) -> None:
        """
        Adds a book to the database.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (int): The ISBN of the book.
            genre (str, optional): The genre of the book. Defaults to None.
            lang (str, optional): The language of the book. Defaults to None.

        Raises:
            ValueError: If Title, Author, or ISBN is empty.
            ValueError: If the book is already present in the database.
            Exception: If any other error occurs.
        """
        try:
            # mandatory fields validation
            if not title or not author or not isbn:
                raise ValueError("Title, Author, and ISBN should not be empty")

            # get the current date, book added date
            current_date = datetime.now().date()
            formatted_date = current_date.strftime("%d-%m-%Y")
            # unique id generation
            id = str(uuid.uuid4())

            # book data path
            book_data_path = os.path.join(database_dir, "book_data.csv")

            # data file exist
            if os.path.exists(book_data_path):

                # load book managment data
                book_data = read_csv(os.path.join(database_dir, "book_data.csv"))

                # when book not in database
                if isbn in book_data['isbn'].values:
                    raise ValueError("Book already present in database.")

                # add new data in dataframe
                new_data = DataFrame([{"id": id,
                                       "title": title,
                                       "author": author,
                                       "isbn": isbn,
                                       "genre": genre,
                                       "lang": lang,
                                       "added_date": formatted_date,
                                       "availability": True,
                                       "delete": False,
                                       "delete_at": None}])

                book_data = concat([book_data, new_data], axis=0)
                book_data.reset_index(drop=True, inplace=True)

            # data file not exist
            else:
                # load book managment data
                book_data = DataFrame()

                book_data['id'] = id
                book_data['title'] = title,
                book_data["author"] = author,
                book_data["isbn"] = isbn,
                book_data["genre"] = genre,
                book_data["lang"] = lang,
                book_data["added_date"] = formatted_date,
                book_data["availability"] = True
                book_data["delete"] = False
                book_data["delete_at"] = None

            # save data
            book_data.to_csv(os.path.join(database_dir, "book_data.csv"), index=False)
            logger.info(f"Book Added: {id} {title}, {author}, {isbn}")

        except Exception as e:
            logger.error(f"Failed to add book: {e}")
            raise e

#################################################################################################################

    def update_book(self, id: str = None, isbn: int = None, title: str = None,
                    author: str = None, genre: str = None, lang: str = None) -> None:
        """
        Updates book information in the database.

        Args:
            id (str, optional): The unique ID of the book. Defaults to None.
            isbn (int, optional): The ISBN of the book. Defaults to None.
            title (str, optional): The title of the book. Defaults to None.
            author (str, optional): The author of the book. Defaults to None.
            genre (str, optional): The genre of the book. Defaults to None.
            lang (str, optional): The language of the book. Defaults to None.

        Raises:
            ValueError: If both ID and ISBN are empty.
            FileNotFoundError: If the database file is not found.
            ValueError: If the book entry is deleted from the database.
            Exception: If any other error occurs.
        """
        try:

            # mandatory fields validation
            if (id == None) and (isbn == None):
                raise ValueError("ID and ISBN both should not be Emtpy")

            # book data path
            book_data_path = os.path.join(database_dir, "book_data.csv")

            # data file exist
            if os.path.exists(book_data_path):

                # when ISBN value is valid
                if isbn:
                    updated_data = {"title": title,
                                    "author": author,
                                    "genre": genre,
                                    "lang": lang}
                # when ID is valid
                else:
                    updated_data = {"title": title,
                                    "isbn": isbn,
                                    "author": author,
                                    "genre": genre,
                                    "lang": lang}

                # extract field which are fill up
                updated_data = {k: v for k, v in updated_data.items() if v}
                fetch_columns = list(updated_data.keys())
                fetch_values = list(updated_data.values())

                # load book managment data
                book_data = read_csv(os.path.join(database_dir, "book_data.csv"))

                # choose filter based from ISBN or ID
                filter_field, filter_head = (id, "id") if id else (isbn, "isbn")

                # check data is in delete bucket
                delete_data = book_data[book_data[filter_head] == filter_field]['delete'].values[0]

                # when book entry not deleted from database
                if delete_data == False:
                    book_data.loc[book_data[filter_head] == filter_field, fetch_columns] = fetch_values

                # when book entry deleted from database
                else:
                    raise ValueError("Updating Book is deleted from database.")

            else:
                raise FileNotFoundError("Database file not found, Please add books in database.")

            # save data
            book_data.to_csv(os.path.join(database_dir, "book_data.csv"), index=False)
            logger.info(f"Book Updated: {id} {title}, {author}, {isbn}")

        except Exception as e:
            logger.error(f"Failed to update book: {e}")
            raise e

#################################################################################################################

    def delete_book(self, id: str = None, isbn: int = None, title: str = None) -> None:
        """
        Deletes a book from the database.

        Args:
            id (str, optional): The unique ID of the book. Defaults to None.
            isbn (int, optional): The ISBN of the book. Defaults to None.
            title (str, optional): The title of the book. Defaults to None.

        Raises:
            ValueError: If all ID, Title, and ISBN are empty.
            FileNotFoundError: If the database file is not found.
            Exception: If any other error occurs.
        """
        try:
            # mandatory fields validation
            if id is None and title is None and isbn is None:
                raise ValueError("ID, Title, and ISBN should not all be empty. At least one field must be provided.")

            # book data path
            book_data_path = os.path.join(database_dir, "book_data.csv")

            # data file exist
            if os.path.exists(book_data_path):

                # load book managment data
                book_data = read_csv(os.path.join(database_dir, "book_data.csv"))

                if title:
                    book_data.loc[book_data['title'] == title, "delete"] = True
                elif id:
                    book_data.loc[book_data['id'] == id, "delete"] = True
                elif isbn:
                    book_data.loc[book_data['isbn'] == isbn, "delete"] = True

            else:
                raise FileNotFoundError("Database file not found, Please add books in database.")

            # save data
            book_data.to_csv(os.path.join(database_dir, "book_data.csv"), index=False)
            logger.info(f"Book Updated: {id} {title}, {isbn}")

        except Exception as e:
            logger.error(f"Failed to delete book: {e}")
            raise e

#################################################################################################################

    def list_book(self, id: str = None, isbn: int = None, title: str = None, author: str = None) -> None:
        """
        Lists books from the database based on provided filters.

        Args:
            id (str, optional): The unique ID of the book. Defaults to None.
            isbn (int, optional): The ISBN of the book. Defaults to None.
            title (str, optional): The title of the book. Defaults to None.
            author (str, optional): The author of the book. Defaults to None.

        Returns:
            DataFrame: A DataFrame containing the filtered book data.

        Raises:
            FileNotFoundError: If the database file is not found.
            Exception: If any other error occurs.
        """
        try:
            # book data path
            book_data_path = os.path.join(database_dir, "book_data.csv")

            # data file exist
            if os.path.exists(book_data_path):

                # load book managment data
                book_data = read_csv(os.path.join(database_dir, "book_data.csv"))

                # fetch data based on field
                if id:
                    data = book_data[book_data['id'] == id]

                elif isbn:
                    data = book_data[book_data['isbn'] == isbn]

                elif title:
                    data = book_data[book_data['title'] == title]

                elif author:
                    data = book_data[book_data['author'] == author]

                # when data is not deleted and available
                data = data[(data['delete'] == False) & (data['availability'] == True)][['id',
                                                                                        "title",
                                                                                        "isbn",
                                                                                        "author",
                                                                                        "genre",
                                                                                        "lang",
                                                                                        "availability"]]

                logger.info("Book list retrieved")

                return data

            else:
                raise FileNotFoundError("Database file not found, Please add books in database.")

        except Exception as e:
            logger.error(f"Failed to list book: {e}")
            raise e

#################################################################################################################

    def search_book(self, id: str = None, isbn: int = None, title: str = None, author: str = None) -> None:
        """
        Searches books in the database based on provided filters.

        Args:
            id (str, optional): The unique ID of the book. Defaults to None.
            isbn (int, optional): The ISBN of the book. Defaults to None.
            title (str, optional): The title of the book. Defaults to None.
            author (str, optional): The author of the book. Defaults to None.

        Returns:
            DataFrame: A DataFrame containing the searched book data.

        Raises:
            FileNotFoundError: If the database file is not found.
            Exception: If any other error occurs.
        """
        try:
            # book data path
            book_data_path = os.path.join(database_dir, "book_data.csv")

            # data file exist
            if os.path.exists(book_data_path):

                # load book managment data
                book_data = read_csv(os.path.join(database_dir, "book_data.csv"))

                # fetch data based on field
                if id:
                    data = book_data[book_data['id'].str.contains(id, case=False, na=False, regex=True)]

                elif isbn:
                    data = book_data[book_data['isbn'].str.contains(isbn, case=False, na=False, regex=True)]

                elif title:
                    data = book_data[book_data['title'].str.contains(title, case=False, na=False, regex=True)]

                elif author:
                    data = book_data[book_data['author'].str.contains(author, case=False, na=False, regex=True)]

                # when data is not deleted and available
                data = data[(data['delete'] == False) & (data['availability'] == True)][['id',
                                                                                        "title",
                                                                                        "isbn",
                                                                                        "author",
                                                                                        "genre",
                                                                                        "lang",
                                                                                        "availability"]]

                logger.info("Book search completed")

                return data

            else:
                raise FileNotFoundError("Database file not found, Please add books in database.")

        except Exception as e:
            logger.error(f"Failed to search book: {e}")
            raise e
