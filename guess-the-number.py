import random
start = input('请输入范围开始值：')
end = input('请输入范围结束值：')
start = int(start)
end = int(end)
count = 0
r = random.randint(start,end)
while True:
	count += 1
	num= input('请猜数字：')
	num= int(num)
	if num == r:
		print('你猜中了')
		print('这是你猜的第',count,'次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('这是你猜的第',count,'次')

