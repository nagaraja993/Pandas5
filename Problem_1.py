import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department.rename(columns = {'name': 'Department'}), 
                        left_on = 'departmentId', right_on = 'id', how = 'left')
    max_salary = df.groupby('departmentId')['salary'].transform('max')
    return df[df['salary'] == max_salary][['Department', 'name', 'salary']]\
            .rename(columns = {'name': 'Employee', 'salary': 'Salary'})