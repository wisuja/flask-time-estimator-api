# Task Completion Time Estimator API

### Built using Flask and Multiple Linear Regression Algorithm

### Link to the repo: [Project Management System](https://github.com/wisuja/Project-Management-System)

---

### Guide

```
POST https://api-time-estimator.herokuapp.com/

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
