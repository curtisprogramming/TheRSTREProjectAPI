from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(data: str) -> str:
    """
    Hash the input data using bcrypt.

    Parameters:
        data (str): The data to be hashed.

    Returns:
        str: The hashed data.
    """
    hash = pwd_context.hash(data)
    return hash

def verify(plain_pwd: str, hashed_pwd: str) -> bool:
    """
    Verify the plain password against the hashed password.

    Parameters:
        plain_pwd (str): The plain password to be verified.
        hashed_pwd (str): The hashed password.

    Returns:
        bool: True if the verification is successful, False otherwise.
    """
    return pwd_context.verify(plain_pwd, hashed_pwd)

def row_to_dict(row) -> dict:
    """
    Convert a SQLAlchemy model row to a dictionary.

    Parameters:
        row: The SQLAlchemy model row.

    Returns:
        dict: A dictionary representation of the row.
    """
    converted_dict = {}
    for column in row.__table__.columns:
        converted_dict[column.name] = getattr(row, column.name)

    return converted_dict

class Search:

    @staticmethod
    def linear_search_id(arr: list, target: str) -> int:
        """
        Perform a linear search to find the index of the target ID in a list.

        Parameters:
            arr (list): The list to be searched.
            target (str): The target ID to be searched.

        Returns:
            int: The index of the target ID if found, otherwise -1.
        """
        for i in range(len(arr)):
            if arr[i]['id'] == target:
                return i

        return -1
