import tkinter as tk

class assessment:

	def __init__(self):
		self.__claimed = 0
		self.__total = 0
		self.__weight = 0
	
	def __init__(self, claimed, total, weight):
		self.__claimed = claimed
		self.__total = total
		self.__weight = weight
	
	
	def get_claimed(self):
		return self.__claimed
	
	def get_total(self):
		return self.__total
	
	def get_weight(self):
		return self.__weight


	def set_claimed(self, claimed):
		self.__claimed = claimed
	
	def set_total(self, total):
		self.__total = total
	
	def set_weight(self, weight):
		self.__weight = weight

class subject:

	def __init__(self):
		self.__assessments = dict()
	
	def __init__(self, assessments):
		count = 0
		self.__assessments = dict()

		for assessment in assessments:
			self.__assessments[count] = assessment
			count += 1
	
	def get_assessments(self):
		return self.__assessments
	
	def get_weight(self):
		weight = 0

		for key, assessment in self.__assessments.items():
			weight += assessment.get_weight()
		
		return weight
	
	def set_assessments(self, assessments):
		self._assessments = assessments
	
	def set_assessment(self, aid, assessment):
		self._assessments[aid] = assessment
	
	def add_assessment(self, assessment):
		self.__assessments.add(assessment)
	
	def calc(self):
		percentage = 0

		for key, assessment in self.__assessments.items():
			percentage += assessment.get_weight() * (assessment.get_claimed() / assessment.get_total())
		
		return percentage

	def calc_reweighted(self):
		return (1 / self.get_weight()) * self.calc()


'''w = tk.Tk()

title = tk.Label(text="Marks Calculator")
title.pack()

subject_entry = tk.Entry(width=50)
subject_entry.pack()

w.mainloop()'''