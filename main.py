from fastapi import FastAPI, HTTPException
from starlette import status
from database.db import get_session
from userModel import User, Pydantic_user, Pydantic_login

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register")
async def register(p_user: Pydantic_user):
    session = get_session()
    app_user: User = User(
        firstName=p_user.firstName,
        lastName=p_user.lastName,
        email=p_user.email,
        phoneNumber=p_user.phoneNumber,
        dob=p_user.dob,
        nationality=p_user.nationality,
        password=p_user.password
    )
    session.add(app_user)
    session.commit()

@app.post("/login")
async def login(login: Pydantic_login):
    session = get_session()
    try:
        user = session.query(User) \
            .filter(User.email.ilike(login.email)) \
            .first()
        if user is not None:
            print(f'user found is : {user.firstName} with number {user.phoneNumber}')
            if user.password == login.password:
                return user
            else:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        else:
            print("No users found")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except NameError:
        pass

    return user