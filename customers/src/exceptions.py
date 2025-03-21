from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class UserIsNotPresentException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User is not present"


class IncorrectEmailOrPasswordException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"


class TokenNotFoundException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token not found"


class IncorrectTokenFormatException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"
