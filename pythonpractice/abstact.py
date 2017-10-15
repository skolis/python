from abc import ABC, abstractmethod

class Employee(ABC):
  @abstractmethod

  def cal_salary(self, sal):
    pass


class Developer(Employee):
  def cal_salary(self, sal):
    finalsalary = sal * 1.10
    return finalsalary

emp1 = Developer()
print (emp1.cal_salary(10000))

