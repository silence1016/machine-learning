import numpy as np
from .metrics import r2_score

class SimpleLinearRegression1:

	def __init__(self):
		# 初始化 SimpleLinearRegression 模型
		self.a_ = None
		self.b_ = None

	def fit(self, x_train, y_train):
		# 根据训练数据集训练模型
		assert x_train.ndim == 1, "Simple Linear Regression can only solve single feature train data"
		assert len(x_train) == len(y_train), \
			"The size of x_train must be equal to the size of y_train"

		x_mean = np.mean(x_train)
		y_mean = np.mean(y_train)

		num = 0.0  # 分子
		d = 0.0  # 分母
		for x_i, y_i in zip(x_train, y_train):
		    num += (x_i - x_mean) * (y_i - y_mean)
		    d += (x_i - x_mean) ** 2

		self.a_ = num / d
		self.b_ = y_mean - self.a_ * x_mean

		return self

	def predict(self, x_predict):
		# 给定待预测数据集 x_predict ,返回预测的结果向量
		assert x_predict.ndim == 1, \
			"Simple Linear Regression can only solve single feature train data"
		assert self.a_ is not None and self.b_ is not None, \
			"must fit before predict"

		return np.array([self._predict(x) for x in x_predict])

	def _predict(self, x_single):
		# 给定单个待预测数据 x_single, 返回x_single 的预测结果值
		return self.a_ * x_single + self.b_

	def __repr__(self):
		return "SimpleLinearRegression1()"

# 使用向量化实现
class SimpleLinearRegression:

	def __init__(self):
		# 初始化 SimpleLinearRegression 模型
		self.a_ = None
		self.b_ = None

	def fit(self, x_train, y_train):
		# 根据训练数据集训练模型
		assert x_train.ndim == 1, "Simple Linear Regression can only solve single feature train data"
		assert len(x_train) == len(y_train), \
			"The size of x_train must be equal to the size of y_train"

		x_mean = np.mean(x_train)
		y_mean = np.mean(y_train)

		num = (x_train - x_mean).dot(y_train - y_mean)
		d = (x_train - x_mean).dot(x_train - x_mean)

		self.a_ = num / d
		self.b_ = y_mean - self.a_ * x_mean

		return self

	def predict(self, x_predict):
		# 给定待预测数据集 x_predict ,返回预测的结果向量
		assert x_predict.ndim == 1, \
			"Simple Linear Regression can only solve single feature train data"
		assert self.a_ is not None and self.b_ is not None, \
			"must fit before predict"

		return np.array([self._predict(x) for x in x_predict])

	def _predict(self, x_single):
		# 给定单个待预测数据 x_single, 返回x_single 的预测结果值
		return self.a_ * x_single + self.b_

	def score(self, x_test, y_test):
		# 确定当前模型准确度, 返回 R Squared
		y_predict = self.predict(x_test)
		return r2_score(y_test, y_predict)

	def __repr__(self):
		return "SimpleLinearRegression()"