# rest-mobile-phone
REST-based application which can store and present information about mobile phones

I have created the RESTApi using the `FastAPI` framework in Python. (https://fastapi.tiangolo.com)
It uses `Uvicorn` server.(https://www.uvicorn.org)

In order to run the application you need to install the FastAPI and Uvicorn.

### Command to install `FastAPI` and `Uvicorn`:-
`pip3 install fastapi "uvicorn[standard]"`


### After this you need to run this command from the directory `restApi`:-
`uvicorn main:app --reload`


Now the RESTApi is succfully hosted on the localhost.


### To access the RESTApi documentation go to :- 
`localhost:8000/docs`
or
`localhost:8000/redoc` 



## Test


#### Inside the `testing` directory, you can find the `Jmeter` test plans.






## Test Scenarios using JMeter

We will create test plans to cover all the features of the application:

1. **Test Scenario 1: Adding a new phone**

   - Create a JMeter test plan with an HTTP Request sampler for the `POST /phone_store/` endpoint.
   - Set the request method to `POST` and provide a JSON payload containing phone details (Name, Brand, Release, OS).
   - Validate the response code, which should be `201 Created`.
   - Parse the response body to ensure that the response contains the correct phone details (Name, Brand, Release, OS).
   - Add assertions to verify that the response contains the required fields.

2. **Test Scenario 2: Querying phone information**

   - Create a JMeter test plan with an HTTP Request sampler for the `GET /phone_store/<id>` endpoint.
   - Set the request method to `GET` and provide the ID of an existing phone in the URL.
   - Validate the response code, which should be `200 OK`.
   - Parse the response body to ensure that the response contains the correct phone details (Name, Brand, Release, OS).
   - Add assertions to verify that the response contains the required fields.

3. **Test Scenario 3: Listing phones**

   - Create a JMeter test plan with an HTTP Request sampler for the `GET /phone_store/` endpoint.
   - Set the request method to `GET`.
   - Validate the response code, which should be `200 OK`.
   - Parse the response body to ensure that the response contains an array of phone objects.
   - Add assertions to verify that the response contains the required fields for each phone.

4. **Test Scenario 4: Deleting a phone**

   - Create a JMeter test plan with an HTTP Request sampler for the `DELETE /phone_store/<id>` endpoint.
   - Set the request method to `DELETE` and provide the ID of an existing phone in the URL.
   - Validate the response code, which should be `204 No Content`.

5. **Test Scenario 5: Error Cases**

   - For each endpoint, create additional test cases to cover error scenarios (e.g., missing fields, non-existing IDs).
   - Validate the appropriate response codes and error messages.

6. **Full Lifecycle Tests**

   - Create more comprehensive test plans that simulate the complete lifecycle of the application, including adding multiple phones, querying and listing them, and finally deleting some phones.
