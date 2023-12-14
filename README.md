# Task Completion Time Estimator API

This project was created to accomodate [Project Management System](https://github.com/wisuja/laravel-project-management-system) on predicting time needed to complete a specific task based on number of people and task type.
<br>

This project was built using Flask as the API server.
The model used in this application was a model I trained using historical data and Linear Regression algorithm.

## Steps to run this application:

1. Click on `<> Code` button
2. Copy the HTTPS/SSH repository link
3. Run `git clone` command on your terminal.
4. Create virtual environment by using `python -m venv ./env`
5. Install the necessary dependencies with `pip install -r requirements.txt`
6. Run the API server with `python run.py`

### Project Management System repository: [Click here](https://github.com/wisuja/laravel-project-management-system)

---

### API Documentation

```
POST

Request
{
  "task_type" : 1, // Integer, Required
  "number_of_peoples": 1 // Integer, Required
}

Response
{
  "prediction": 100 // Float (Time estimated in minutes)
}
```
