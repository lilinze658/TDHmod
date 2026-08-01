import pyradox as pyx
from pathlib import Path
import random

def process_file():
	"""处理目录下的所有txt文件"""
	input_dir = Path.cwd()

	subideo = []
	ideo_totol = 100
	# 递归遍历所有txt文件
	for file_path in input_dir.rglob("*.txt"):
		try:
			with file_path.open('r', encoding='utf-8') as f:
				print(file_path)
				randomInt = random.randint(100000, 50000000)
				manpowerValue = []
				categoryValue = []
				content = f.read()
				pyxContent = pyx.parse(content)
				stateNode = pyxContent["state"]
				manpowerValue = [v for k, v in stateNode.items() if k == "manpower"]
				categoryValue = [v for k, v in stateNode.items() if k == "state_category"]
				if not manpowerValue:
					stateNode["manpower"] = randomInt
				if not categoryValue:
					stateNode["state_category"] = "city"
				print("\n")
			newcontent = str(pyxContent)
			print(newcontent)
			newcontent2 = newcontent.replace("    ", "\t")
			# 构建输出路径
			#categoryValueprint(newcontent2)
			# 写入新文件
			with file_path.open('w+', encoding='utf-8') as f:
				f.write(newcontent2)

		except Exception as e:
			print(f"处理 {file_path.name} 时出错: {str(e)}")

def reorder_parallel_lists(a, b, new_order):
	order_map = {element: idx for idx, element in enumerate(new_order)}
	combined = list(zip(a, b))
	sorted_combined = sorted(combined, key=lambda pair: order_map[pair[0]])
	sorted_a, sorted_b = zip(*sorted_combined)

	return list(sorted_a), list(sorted_b)

def manpowerSet():
	input_dir = Path.cwd()

	subideo = []
	ideo_totol = 100
	# 递归遍历所有txt文件
	for file_path in input_dir.rglob("*.txt"):
		try:
			with file_path.open('r', encoding='utf-8') as f:
				print(file_path)
				randomInt = random.randint(100000, 50000000)
				content = f.read()
				newcontent = content.replace("manpower = 0", f"manpower = {randomInt}")
				print("\n")
			print(newcontent)
			newcontent2 = newcontent.replace("    ", "\t")
			# 构建输出路径
			#categoryValueprint(newcontent2)
			# 写入新文件
			with file_path.open('w+', encoding='utf-8') as f:
				f.write(newcontent2)

		except Exception as e:
			print(f"处理 {file_path.name} 时出错: {str(e)}")


if __name__ == "__main__":
	print("开始处理文件...")
	manpowerSet()
	print("处理完成！结果保存在:", Path.cwd())