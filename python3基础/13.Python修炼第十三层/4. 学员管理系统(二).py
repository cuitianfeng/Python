\学员管理系统: s4day66
# 内容回顾：
	1. 创建Django程序
	2. 新URL方式：
		- 添加
		- 编辑
		- 删除
		
# 今日内容：
	0. 班级管理
		- 添加
		- 编辑
		- 删除
		PS：views中对用户提交的数据进行判断（Form组件）
		
	1. 学生管理（连表查询,用户在查询到学生信息时，不能把学生的班级id展示出来，要展示真实的班级名称）
	    - 查询 sql: select student.id,student.name,class.title from student left join class on student.class_cid = class.id;
		- 添加 
		- 编辑
		- 删除
		
	2. 模态对话框
		班级管理：
			- 添加
				Form表单提交数据，页面会刷新。
	3. Ajax
		引入jQuery
		
		$.ajax({
			url: '要提交的地址',
			type: 'POST', # GET或POST,提交方式
			data: {'k1': 'v1','k2':'v2'}, # 提交的数据
			success:function(data){
				# 当前服务端处理完毕后，自动执行的回调函数
				# data返回的数据
			}
		})
	
	其他：
		1. 模板语言if条件语句
		2. Form表单提交，页面会刷新。
		3. Ajax提交页面不刷新，它会偷偷提交数据。
		4. js实现页面跳转：
			location.href = "要跳转的地址"
		5. 
			模态对话框（Ajax）
				Ajax适用
					- 少量输入框
					- 数据少
					- 登录
			新URL方式
				URL适用
					- 操作多
					- 对于大量的数据以及操作
下午作业：
	1. 班级：
		Ajax删除
	2. 班级
		Ajax编辑
本周作业：
	- 一对多【新url，对话框】 （老师和班级的关系表）
	- 多对多【新url，对话框】 （老师和班级的关系表）
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	